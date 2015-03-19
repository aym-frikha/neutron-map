#!/usr/bin/env python
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# @author: Aymen Frikha, netvirt
# nodemanager.py
# 23.07.2013

# # IF IN NEUTRON
from neutron.openstack.common import log as logging
LOG = logging.getLogger(__name__)


from neutron.plugins.map.DB_Structures import Device


def _remove_reference(node, service_name):
    del_ref = None
    found = False
    if node.ReferenceList:
        for ref in node.ReferenceList.RefNode:
            tab = ref.href.split(':')
            if tab[0] == service_name:
                del_ref = ref
                found = True
                break
    if found:
        del del_ref


def _remove_service_from_list(device, instance_service_name):
    for service in device.Services.Service:
        if service.href == instance_service_name:
            device.Services.Service.remove(service)


def _remove_only_reference(node, inst_service_name):
    if node.ReferenceList:
        del_ref = None
        for service in node.ReferenceList.RefNode:
            if service.href.split(':')[0] == inst_service_name:
                del_ref = service
        del del_ref


def _has_other_references(node, inst_service_name):
    if node.ReferenceList:
        for service in node.ReferenceList.RefNode:
            if service.href.split(':')[0] != inst_service_name:
                return True

        return False


def _has_reference(node):
    if node.ReferenceList:
        for services in node.ReferenceList.RefNode:
            if services != None:
                return True
        return False


def _has_reference_by_name(node, instance_service_name):
    if node.ReferenceList:
        if node.ReferenceList.RefNode:
            for services in node.ReferenceList.RefNode:
                tab = services.href.split(':')
                if tab[0] == instance_service_name:
                    node.ReferenceList.RefNode.remove(services)
                    return True
    return False


def _add_serv_instance(device, instance_service_name):
    for service in device.Services.Service:
        if service.href == instance_service_name:
            return
    inst_service = Device.CTD_ANON_3()
    inst_service.href = instance_service_name
    device.Services.append(inst_service)


def _clone_node(device_node, service_node):
    device_node.name = service_node.name
    device_node._CimRef = service_node.CimRef
    device_node.known = service_node.known
    device_node.parameter = service_node.parameter
    device_node.uid = service_node.uid
    device_node.cardinality = service_node.cardinality
    device_node.shadow = service_node.shadow
    if service_node.BaseParent:
        device_node.BaseParent = Device.CTD_ANON_5()
        device_node.BaseParent.href = service_node.BaseParent.href
    device_node.Value = service_node.Value
    return device_node


def _add_reference(atnode, instance_service_name, uid, device):
    if device != None:
        for service in device.Services.Service:
            if service.href == instance_service_name:
                return
    if atnode.ReferenceList:
        refnode = Device.CTD_ANON_8()
        refnode.href = instance_service_name + ":" + str(uid)
        atnode.ReferenceList.append(refnode)
    else:
        atnode.ReferenceList = Device.CTD_ANON_7()
        refnode = Device.CTD_ANON_8()
        refnode.href = instance_service_name + ":" + str(uid)
        atnode.ReferenceList.append(refnode)


def _device_supported(versions, device):
    for version in versions:
        if version == device.Properties.IOSVersion:
            return True
    return False


def _version_supported(command, mode, reference):
    versions = []
    for command_supported in reference.CommandList.Command:
        if command_supported.name == command and (
                    command_supported.mode == mode):
            for syntax in command_supported.Syntax:
                versions.append(syntax.version)
    return versions

def _deploy_node( src_node, parent_node, instance_service_name,
                last_node, device, is_parameter = False):
    added = False
    atnode = Device.DevNode()
    node_list = []
    if type(parent_node) != Device.DevNode:
        node_list = parent_node.ConfigTree
    else:
        if not is_parameter:
            node_list = parent_node.Children
        else:
            node_list = parent_node.Parameters
    new_node = Device.DevNode()
    new_node = _clone_node(new_node, src_node)
    if node_list:
        for lnode in node_list.Node:
            if lnode.name == new_node.name:
                if (new_node.parameter == lnode.parameter
                    and new_node.Value != None
                    and lnode.Value != None
                    and lnode.Value == new_node.Value
                    and len(new_node.Value) != 0
                    and len(lnode.Value) != 0):
                    atnode = lnode
                    added = True
                    break
                if new_node.name == "end":
                    last_node = lnode
        if not added:
            if not is_parameter:
                if type(parent_node) != Device.DevNode:
                   parent_node.ConfigTree.append(new_node)
                else:
                    parent_node.Children.append(new_node)
            elif is_parameter:
                parent_node.Parameters.append(new_node)
            atnode = new_node
    _add_reference(atnode, instance_service_name, new_node.uid, device)
    if src_node.Children:
        if atnode.Children:
            for node in src_node.Children.Node:
                _deploy_node(node, atnode, instance_service_name, None,
                                 device)
        else:
            atnode.Children = Device.CTD_ANON_10()
            for node in src_node.Children.Node:
                _deploy_node(node, atnode, instance_service_name, None,
                                 device)
    if src_node.Parameters:
        if atnode.Parameters:
            for node in src_node.Parameters.Node:
                _deploy_node(node, atnode, instance_service_name, None,
                                 device, is_parameter=True)
        else:
            atnode.Parameters =  Device.CTD_ANON_9()
            for node in src_node.Parameters.Node:
                _deploy_node(node, atnode, instance_service_name, None,
                                 device, is_parameter=True)

    return atnode

    ''' Deploy instance services on configuration nodes '''

def deploy_service( device, inst_service):
    """ Deploy a Service_instance on a Device
    :param device: Device object
    :param inst_service: ServiceInstance object
    :return:device: Device object
    """
    present = False
    for service_name in device.Services.Service:
       if service_name.href == inst_service.name:
           LOG.info("Service '%s' is already deployed on '%s'",
                     service_name.href, device.name)
           present = True
    stack = []
    if not present:
        for node_service in inst_service.ServiceTree.Node:
            stack.append(node_service)
    last_node = None
    while len(stack) > 0:
       node_service = stack.pop()
       added = False
       if node_service.BaseParent.href != "" and (
                    node_service.BaseParent != None):
            for node_device in device.ConfigTree.Node:
                if node_device.name == node_service.name:
                   last_node = _deploy_node(node_service, node_device,
                                                 inst_service.name,
                                                 last_node, device)
                   added = True
                   break
       if added == False:
           last_node = _deploy_node(node_service, device,
                                         inst_service.name,
                                         last_node, device)
    _add_serv_instance(device, inst_service.name)
    if not present:
        LOG.info("Service '%s' is deployed on '%s'",
                 inst_service.name, device.name)
    # print(device)
    # self.db_manager.set_device_config(device)
    return device

def _remove_services_in_nodes( nodes, instance_service_name):
    """

   :param nodes:List of device configuration nodes (Meta_CLi format)
   :param instance_service_name: String
    """
    remove_nodes = []
    for node in nodes.Node:
       if node.Children:
           _remove_services_in_nodes(node.Children,
                                         instance_service_name)
       if _has_reference_by_name(node, instance_service_name):
           if _has_other_references(node, instance_service_name):
               _remove_only_reference(node, instance_service_name)
           else:
               remove_nodes.append(node)

           # if not self.has_reference(node):

    for node1 in remove_nodes:
        nodes.Node.remove(node1)

    '''Remove service instance from device '''

def remove_service( device, instance_service_name):
    """

    :param device:Device object
    :param instance_service_name: String
    :return: device: Device object
    """
    if not device.Services.Service:
        LOG.error("No services are deployed on '%s'", device.name)
        exit()
    found = False
    for service in device.Services.Service:
        if service.href == instance_service_name:
            _remove_services_in_nodes(device.ConfigTree,
                                            instance_service_name)
            _remove_service_from_list(device, instance_service_name)
            found = True
    if found == False:
        LOG.error("Service '%s' not found on '%s'",
                    instance_service_name, device.name)
        exit()
    else:
        LOG.info("Service '%s' removed from '%s'",
                    instance_service_name, device.name)
    return device

def _has_reference_discover( node, service_name):
    if node.ReferenceList:
        for ref in node.ReferenceList.RefNode:
            tab = ref.href.split(':')
            if tab[0] == service_name:
                return True
    return False

def _find_node_in_children( node, children, service_name):
    if children == None or len(children.Node) == 0:
        return False
    all_found = False
    l_cnode = None
    for c_node in children.Node:
        if (c_node.name == node.name
            and c_node.parameter == node.parameter
            and _has_reference_discover(c_node,
                                            service_name) is True and c_node.Value == node.Value):
            l_cnode = c_node
            _add_reference(c_node, service_name, node.uid, None)
            inst_found = True
            if node.Children:
                for t_node in node.Children.Node:
                    inst_found = _find_node_in_children(t_node,
                                                            c_node.Children, service_name)
            if inst_found == True:
                all_found = True
                break
            else:
                 _remove_reference(l_cnode, service_name)

    if all_found == False and l_cnode != None:
        _remove_reference(l_cnode, service_name)
    if all_found == False and (node.cardinality == "01"
                                or node.cardinality == "0N"):
        all_found = True

    return all_found

    ''' Discovering services on devices '''

def discover_service( device, inst_service):
    """

    :param device:Device object
    :param inst_service: ServiceInstance object
    :return: all_found: Boolean
    """
    all_found = True
    for s_node in inst_service.ServiceTree.Node:
        parent = None
        nodes = []
        if (s_node.BaseParent and s_node.BaseParent.href
            and s_node.BaseParent.href != ""):
            for d_node in device.ConfigTree.Node:
                if d_node.name == s_node.BaseParent.href:
                    parent = d_node
                    break
            if parent == None:
                LOG.info("attachement parent for node %r was not found",
                            s_node.name)
                all_found = False
            else:
                nodes = parent.Children.Node
        else:
            nodes = device.ConfigTree
        if len(nodes.Node) != 0:
            all_found = _find_node_in_children(s_node, nodes,
                                                    inst_service.name)
        if all_found == False:
            break
    return all_found


