#!/usr/bin/env python
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# @author: Aymen Frikha, netvirt
# isolationprovider.py
# 23.07.2013

# # IF IN NEUTRON
from neutron.openstack.common import log as logging
from neutron.plugins.map import constants, resources

LOG = logging.getLogger(__name__)

from neutron.plugins.map.map_utils import format_port
from neutron.plugins.map.map_utils import ServiceError
from neutron.plugins.map.DB_Structures import ServiceInstance


class IsolationProvider():
    def __init__(self, resources, l2_services, l3_services):
        self.resources = resources
        self.l2_services = l2_services
        self.l3_services = l3_services
        self.services = {'trunk-allow': self.create_vlan,
                         'eompls_int.xml': self.create_eompls
        }
        return

    def clone_node(self, vm_node):
        new_node = resources.ServiceInstance.InsNode()
        new_node.name = vm_node.name
        if vm_node.BaseParent:
            new_node.BaseParent = resources.ServiceInstance.CTD_ANON_3()
            if vm_node.BaseParent.href:
                new_node.BaseParent.href = vm_node.BaseParent.href
            else:
                new_node.BaseParent.href = ""
        new_node.Value = ""
        new_node.uid = vm_node.uid
        new_node.CimRef = vm_node.CimRef
        new_node.known = vm_node.known
        new_node.parameter = vm_node.parameter
        new_node.shadow = vm_node.shadow
        return new_node


    def vlan_attributes(self, service_instance, segmentation_id, port):
        # parameter[0]: vlan-id
        for node in service_instance.ServiceTree.Node:
            if node.name == 'interface':
                node.Value = port
                for child in node.Children.Node:
                    if child.name == 'switchport access':
                        for ch in child.Parameters.Node:
                            if ch.name == 'vlan':
                                ch.Value = str(segmentation_id)
                    if child.name == 'switchport mode':
                        child.Value = 'trunk'
                    if child.name == 'switchport trunk':
                        child.Value = 'allowed'

                        for ch in child.Parameters.Node:
                            if ch.name == 'vlan':
                                ch.Value = '1,2,1001-1005,'+str(segmentation_id)

    def create_vlan(self, node, path, segmentation_id):
        service_instance = self.create_empty_service_instance(constants.TRUNK_ALLOW,
                                                              segmentation_id,
                                                              node)

        self.vlan_attributes(service_instance, segmentation_id,
                             node['interface'].name)
        node[constants.SERVICE_INSTANCE] = service_instance


    def create_empty_service_instance(self, generic_service_name,
                                      segmentation_id,
                                      node, devices_concerned=0):
        generic_service = self.resources.get_gen_service(generic_service_name)
        service_instance = ServiceInstance.ServiceInstance()
        service_instance.name = (
            node['node'].name + "-" + node['interface'].name + "-"
            + generic_service_name + "-" + str(segmentation_id))
        service_instance.Description = ""
        service_instance.InstanceOf = ServiceInstance.CTD_ANON_()
        service_instance.InstanceOf.href = generic_service.name
        service_instance.ServiceTree = ServiceInstance.CTD_ANON_2()
        self.build_nodes_from_data(service_instance.ServiceTree,
                                   generic_service.ServiceTree, None,
                                   devices_concerned, False)
        return service_instance

    def build_nodes_from_data(self, src_nodes, nodes, parent,
                              devices_concerned, parameter):
        loop_length = 2
        for vm_node in nodes.Node:
            new_node = self.clone_node(vm_node)
            if vm_node.cardinality and vm_node.cardinality == "1N":
                if isinstance(devices_concerned, int):
                    loop_length = devices_concerned
                elif devices_concerned.isdigit():
                    loop_length = int(devices_concerned)
                else:
                    LOG.error(
                        ("build_node called with wrong devices_concerned: %s"),
                        devices_concerned)
            if parent == None:
                for x in range(1, loop_length):
                    if x != 1:
                        src_nodes.append(self.clone_node(vm_node))
                    else:
                        src_nodes.append(new_node)
                loop_length = 2
            else:
                for x in range(1, loop_length):
                    if x != 1:
                        if not parameter:
                            parent.Children.append(self.clone_node(vm_node))
                        else:
                            parent.Parameters.append(self.clone_node(vm_node))
                    else:
                        if not parameter:
                            parent.Children.append(new_node)
                        else:
                            parent.Parameters.append(new_node)
                loop_length = 2
            if vm_node.Children:
                new_node.Children = ServiceInstance.CTD_ANON_5()
                self.build_nodes_from_data(src_nodes, vm_node.Children,
                                           new_node, devices_concerned, False)
            if vm_node.Parameters:
                new_node.Parameters = ServiceInstance.CTD_ANON_4()
                self.build_nodes_from_data(src_nodes, vm_node.Parameters,
                                           new_node, devices_concerned, True)


    def extract_eompls_node_position(self, principal_node, path):
        l3_nodes = [node for node in path if
                    node['domain'] == constants.L3_DOMAIN]
        node_index = l3_nodes.index(principal_node)
        if node_index == 0:
            return constants.FIRST
        elif node_index == len(l3_nodes) - 1:
            return constants.LAST
        elif node_index == 1 or node_index == len(l3_nodes) - 1:
            return None
        else:
            return constants.CENTER

    def create_eompls(self, node, path, segmentation_id):
        # Extract node position
        l3_nodes = [n for n in path if n['domain'] == constants.L3_DOMAIN]
        node_index = l3_nodes.index(node)
        if node_index == 0:
            # For the first node of eompls service, the remote node, is the last
            # node of the path
            eompls_ext = self.create_empty_service_instance(
                constants.EoMPLS_EXT,
                segmentation_id,
                node)
            # Add attributes for eompls_ext
            self.eompls_ext_attributes(eompls_ext, node, segmentation_id,
                                       l3_nodes[-1])
            node[constants.SERVICE_INSTANCE] = eompls_ext
            eompls_int = self.create_empty_service_instance(
                constants.EoMPLS_INT,
                segmentation_id,
                l3_nodes[node_index + 1])
            # Add attributes for eompls_int
            self.eompls_int_attributes(eompls_int, l3_nodes[node_index + 1],
                                       segmentation_id,
                                       l3_nodes[-1])
            l3_nodes[node_index + 1][constants.SERVICE_INSTANCE] = eompls_int
        elif node_index == len(l3_nodes) - 1:
            eompls_ext = self.create_empty_service_instance(
                constants.EoMPLS_EXT,
                segmentation_id,
                node)
            # Add attributes for eompls_ext
            self.eompls_ext_attributes(eompls_ext, node, segmentation_id,
                                       l3_nodes[0])
            node[constants.SERVICE_INSTANCE] = eompls_ext
            eompls_int = self.create_empty_service_instance(
                constants.EoMPLS_INT,
                segmentation_id,
                l3_nodes[node_index - 1])
            # Add attributes for eompls_int
            self.eompls_int_attributes(eompls_int, l3_nodes[node_index - 1],
                                       segmentation_id,
                                       l3_nodes[0])
            l3_nodes[node_index - 1][constants.SERVICE_INSTANCE] = eompls_int
        elif node_index == 1 or node_index == len(l3_nodes) - 1:
            pass
        else:
            # TODO: Implement service for core mpls routers
            pass

    def eompls_int_attributes(self, service_instance, device, segmentation_id,
                              remote_node):
        # loop_interface_configured = False
        """

        :param service_instance:
        :param device:
        :param segmentation_id:
        :param remote_node:
        """
        for node in service_instance.ServiceTree.Node:
            for child in node.Children.Node:
                if child.name == 'ip ospf network':
                    child.Value = 'point-to-point'
                    node.Value = 'Loopback0'

                # Get same value of the ip address from the device configuration
                if child.name == 'ip address':
                    dev_conf = self.resources.get_device_config(
                            device['node'].name)
                    for dev_node in dev_conf.ConfigTree.Node:
                        if dev_node.name == 'interface' and dev_node.Value == 'Loopback0':
                            for node_child in dev_node.Children.Node:
                                if node_child.name == 'ip address':
                                    child.Value = node_child.Value
                if child.name == 'mpls ip':
                    node.Value = device['interface'].name

        pass

    def eompls_ext_attributes(self, service_instance, device, segmentation_id,
                              remote_device):
        for node in service_instance.ServiceTree.Node:
            if node.name == 'interface':
                node.Value = device['interface'].name
                for child in node.Children.Node:
                    if child.name == 'xconnect':
                        conf_rm_dev = self.resources.get_device_config(
                            remote_device['node'].name)
                        loop_interface = None
                        for remote_node in conf_rm_dev.ConfigTree.Node:

                            # LOG.error(_("interface found for device %s"), remote_device['node'].name)
                            if remote_node.name == 'interface' and remote_node.Value == 'Loopback0':

                                for remote_ch in remote_node.Children.Node:
                                    if remote_ch.name == 'ip address':
                                        loop_interface = remote_ch.Value
                        child.Value = loop_interface
                        if child.Parameters:
                            for ch in child.Parameters.Node:
                                if ch.name == 'vcid':
                                    #TODO Segmentation id
                                    ch.Value = str(15)
                                if ch.name == 'encapsulation':
                                    ch.Value = 'mpls'
            # TODO: These parameters must be configurable and adaptable to the
            # network
            if node.name == 'router ospf':
                node.Value = '1'
                for child in node.Children.Node:
                    if child.name == 'passive-interface':
                        child.Value = device['interface'].name
                    if child.name == 'network':
                        child.Value = '0.0.0.0 255.255.255.255'
                        for param in child.Parameters.Node:
                            if param.name == 'area':
                                param.Value = '0'

        pass

    # def extract_ip(self, devices_concerned, interface):
    # for dev_name in devices_concerned:
    # dev = self.resources.get_device_by_name(dev_name)
    # for node_neighbor in dev.ConfigTree.Node:
    #             if node_neighbor.name == "interface" and (
    #                         node_neighbor.Value == interface):
    #                 for child_neighbor in node_neighbor.Children.Node:
    #                     if child_neighbor.name == "ip address":
    #                         del devices_concerned[dev_name]
    #                         return child_neighbor.Value
    #
    # def vpls_attributes1(self, service_instance, parameters, device_name, port,
    #                      devices_ports):
    #     # parameters[0] ==> vlan allowed on this service
    #     # parameters[1] ==> VPN id
    #     devices_concerned = devices_ports.copy()
    #     del devices_concerned[device_name]
    #     applicable = False
    #     device = self.resources.get_device_by_name(device_name)
    #     for device_node in device.ConfigTree.Node:
    #         if device_node.name == "interface" and (
    #                     device_node.Value == "loopback0"):
    #             for device_node_child in device_node.Children.Node:
    #                 if device_node_child.name == "ip address":
    #                     applicable = True
    #     if applicable:
    #         for node in service_instance.ServiceTree.Node:
    #             if node.Children:
    #                 for child in node.Children.Node:
    #                     if child.name == 'vpn id':
    #                         child.Value = parameters[1]
    #                         node.Value = parameters[0]
    #                     if child.name == 'neighbor' and child.Value == "":
    #                         child.Value = self.extract_ip(devices_concerned,
    #                                                       "loopback0")
    #                         LOG.info(_("%r"), child.Value)
    #                     if child.name == 'trunk vlan':
    #                         node.Value = port
    #                         child.Value = parameters[1]
    #                     if child.name == 'xconnect vfi':
    #                         child.Value = parameters[0]
    #                         node.Value = parameters[1]
    #                     if child.name == 'ip address':
    #                         node.Value = 'loopback0'
    #                         device_conc = {}
    #                         device_conc.update({device_name: port})
    #                         child.Value = self.extract_ip(device_conc,
    #                                                       "loopback0")
    #     else:
    #         LOG.error(_("Service VPLS is not applicable on %s"),
    #                   device_name)
    #         raise ServiceError(_("VPLS can not be installed on %s."
    #                              + " Please add manually a loopback0 interface"),
    #                            device_name)
    #
    # def create_vpls(self, parameters, device_name, port, devices_ports):
    #     service_id = parameters[0]
    #     LOG.debug(_(constants.VPLS))
    #     service_instance = self.create_empty_service_instance(constants.VPLS,
    #                                                           parameters, len(
    #             devices_ports), device_name, port)
    #     self.vpls_attributes1(service_instance, parameters, device_name, port,
    #                           devices_ports)
    #     self.resources.write_service_instance(service_instance, "VPLS",
    #                                           device_name,
    #                                           format_port(port), service_id)
    #     return device_name + "-" + format_port(port) + "-VPLS-" + service_id
    #
    # def trunk_attribute(self, service_instance, service_id, port):
    #     for node in service_instance.ServiceTree.Node:
    #         if node.name == 'interface':
    #             node.Value = port
    #             for child in node.Children.Node:
    #                 if child.name == 'mode':
    #                     child.Value = 'trunk'
    #                 if child.name == 'encapsulation':
    #                     child.Value = "dot1q"
    #
    # def create_trunk(self, parameters, device_name, port, devices_ports):
    #     LOG.debug(_(constants.TRUNK))
    #     service_id = parameters[0]
    #     service_instance = self.create_empty_service_instance(constants.TRUNK,
    #                                                           [""],
    #                                                           len(
    #                                                               devices_ports),
    #                                                           device_name, port)
    #     self.trunk_attribute(service_instance, service_id, port)
    #     f = open(
    #         self.resources.networkpath + "ServiceInstance - " + device_name + "-"
    #         + format_port(port) + "-Trunk" + ".xml", 'w+')
    #     f.write(service_instance.toDOM().toprettyxml())
    #     f.close()
    #     return device_name + "-" + format_port(port) + "-Trunk"
    #
    # def trunk_allow_attribute(self, service_instance, parameters, port):
    #     # parameter[0]: vlan-ids
    #     for node in service_instance.ServiceTree.Node:
    #         if node.name == 'interface':
    #             node.Value = port
    #             for child in node.Children.Node:
    #                 if child.name == 'trunk vlan':
    #                     child.Value = '1,2,1002-1005,' + parameters[0]
    #                     # child.Value = "allow"
    #                     # for child2 in child.Children.Node:
    #                     #    if child2.name == "vlan":
    #                     #        child2.Value = parameters[0]
    #
    # def create_trunk_allow(self, parameters, device_name, port, devices_ports):
    #     LOG.debug(_(constants.TRUNK_ALLOW))
    #     service_instance = self.create_empty_service_instance(
    #         constants.TRUNK_ALLOW, parameters, len(devices_ports), device_name,
    #         port)
    #     self.trunk_allow_attribute(service_instance, parameters, port)
    #     # self.trunk_allow_attribute(service_instance, parameters[0], port)
    #     self.resources.write_service_instance(service_instance, "trunk-allow",
    #                                           device_name,
    #                                           format_port(port), parameters[0])
    #     instance = (device_name + "-" + format_port(port) + "-trunk-allow-"
    #                 + parameters[0])
    #     return instance
    #
    # def OTV_attributes(self, service_instance, parameters, device_name,
    #                    port):
    #     # parameters[0] ==> OTV id
    #     # parameters[1] ==> vlan allowed on this service
    #     # parameters[2] ==> multicast ip address : @ip
    #     # parameters[3] ==> multicast range ip address : @ip/mask
    #
    #     for node in service_instance.ServiceTree.Node:
    #         if node.name == 'interface':
    #             node.Value = port
    #             for child in node.Children.Node:
    #                 if child.name == 'ip igmp version':
    #                     child.Value = '3'
    #         if node.name == 'vlan':
    #             node.Value = parameters[1]
    #         if node.name == 'otv site-identifier':
    #             node.Value = parameters[0]
    #         if node.name == 'interface overlay':
    #             node.Value = '1'
    #             for child in node.Children.Node:
    #                 if child.name == 'otv control-group':
    #                     child.Value = parameters[2]
    #                 if child.name == 'otv data-group':
    #                     child.Value = parameters[3]
    #                 if child.name == 'otv join-interface':
    #                     child.Value = port
    #                 if child.name == 'otv extend-vlan':
    #                     child.Value = parameters[0]
    #
    #
    # def create_OTV(self, parameters, device_name, port, devices_ports):
    #     LOG.debug(_(constants.OTV))
    #     service_instance = self.create_empty_service_instance(
    #         constants.OTV, parameters, len(devices_ports), device_name,
    #         port)
    #     self.OTV_attributes(service_instance, parameters, device_name,
    #                         port)
    #     f = open(self.resources.networkpath + "ServiceInstance - " + device_name
    #              + "-" + format_port(port) + "-OTV-" + parameters[0]
    #              + ".xml", 'w+')
    #     f.write(service_instance.toDOM().toprettyxml())
    #     f.close()
    #     instance = (device_name + "-" + format_port(port) + "-OTV-"
    #                 + parameters[0])
    #     return instance

    def _verify_l3_domain_existance(self, path):
        l3_nodes = [node for node in path if
                    node['domain'] == constants.L3_DOMAIN]
        if l3_nodes[0]['node'].id != l3_nodes[-1]['node'].id:
            return True
        else:
            return False

    def create_service_instance(self, node, path, segmentation_id):
        """Create an instance from a Generic_Service"""
        if node['type'] == constants.PHYSICAL_NODE and node[
            'node'].type == constants.SWITCH or node[
            'node'].type == constants.ROUTER:
            if node['domain'] == constants.L2_DOMAIN:
                self.services[self.l2_services[0]](
                    node, path,
                    segmentation_id)
            elif node[
                'domain'] == constants.L3_DOMAIN and self._verify_l3_domain_existance(
                    path):
                self.services[self.l3_services[0]](
                    node, path,
                    segmentation_id)

        return node

        # def transactional(self, service_name):
        # generic_service = self.get_service(service_name)
        # return generic_service.Priority == 'True'
