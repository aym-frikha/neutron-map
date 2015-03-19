import time
from neutron.openstack.common import log
from neutron.plugins.map import models
from neutron.plugins.map import db as map_db
from neutron.plugins.map import YenKSP
from neutron.plugins.map import topology_manager
from neutron.plugins.map import nodemanager
from neutron.plugins.map import isolationprovider
from neutron.plugins.map import constants as cst
from neutron.plugins.map import validator
from neutron.plugins.map import driver_manager
from neutron.plugins.map.cli_driver import ios_parser_translator

LOG = log.getLogger(__name__)


class InfrastructureManager(object):
    def __init__(self, resources, l2_services, l3_services):
        self.resources = resources
        self.isolation_provider = \
            isolationprovider.IsolationProvider(resources,
                                                l2_services,
                                                l3_services)
        self.net_segmentation_id = {}
        self.validator = validator.Validator(self.resources)
        self.ios_parser = ios_parser_translator.IOSTranslator(resources)
        self.driver_manager = driver_manager.DriverManager(resources)
        pass

    def connect_vm_to_network(self, session, vm, start_time):
        # Verify if there is other VM on the same virtual network
        vm_list = self._list_connected_vm(session, vm)
        v_net = map_db.get_virtual_net_from_v_node(session, vm)

        topology = {}
        if len(vm_list) > 0:
            # get all virtual nodes of the same virtual network of the VM
            v_nodes = map_db.get_virtual_nodes(session, vm.virtual_network)
            # get the physical network that the VM belongs to
            phys_net = map_db.get_phys_net_from_v_node(session, vm)
            # get all physical nodes from the physical network phys_net
            phys_nodes = map_db.get_physical_nodes(session, phys_net)
            # Create topology dict.
            # The topology dictionary is as follow:
            #{node_id:{neighbor_id:link_cost}}
            for node in v_nodes + phys_nodes:
                topology[node.id] = topology_manager.get_node_neighbors(session,
                                                                        node)
            #TODO: Adapt YenKSP algorithm to be able to manage node objects and
            #TODO: to return paths with node interfaces
            graph = YenKSP.DiGraph()
            graph._data = topology
            paths = YenKSP.algorithms.ksp_yen(graph, vm.id, vm_list[0].id, 1)
            path = []
            for p in paths:
                for node_id in p['path']:
                    node = (session.query(models.VirtualNode).
                            filter_by(id=node_id).first())
                    if not node:
                        node = (session.query(models.PhysicalNode).
                                filter_by(id=node_id).first())
                    path.append(node)
                break

            #Extract Virtual nodes and physical nodes from the path
            path = topology_manager.identify_virtual_physical_paths(session,
                                                                    path)

            path = topology_manager.identify_physical_l2_l3_paths(path)
            # LOG.error(_("Generated path: %s"), path)

            LOG.info(_("The path is : %s"), ' -> '.join([
                '( node: ' + node['node'].name + ' interface: ' + node[
                    'interface'].name + ')' for node in path]))

            #Create service instances for every node
            for node in path:
                self.isolation_provider.create_service_instance(node, path,
                                                                self.net_segmentation_id[
                                                                    v_net.id])
            #Extract instance_service for every node {device_name: List[service_instance]}
            #TODO: Consider other node types like virtual nodes, IDS, IPS ....
            node_services = {}
            instance_services = []
            for node in path:
                if node['type'] == cst.PHYSICAL_NODE and (
                node['node'].type == cst.SWITCH or node['node'].type == cst.ROUTER):
                    instance_services.append(node[cst.SERVICE_INSTANCE])
                    if node['node'] not in node_services.keys():
                        node_services[node['node']] = []
                    node_services[node['node']].append(node[cst.SERVICE_INSTANCE])

            for n in node_services:
                LOG.error(_('node : %s'), n.name)
                for service in node_services[n]:
                    LOG.error(_('services: %s'), service.name)
            #Create configuration for every node {PhysicalNodeObject : Configuration}
            #And deploy instance_service on every node
            node_configurations = {}
            for node in node_services.keys():
                node_configurations[node] = self.resources.get_device_config(
                    node.name)
                for service in node_services[node]:
                    node_configurations[node] = nodemanager.deploy_service(
                        node_configurations[node], service)

            #validate services on devices
            is_valid = self.validator.validate_all(instance_services,
                                                       node_configurations.values())
            # conf = node_configurations.values()
            # If all services are valid, configure equipments
            if is_valid:
                self.driver_manager.configure_equipments(node_configurations)
                # LOG.error(_('conf %s'), conf[1].toDOM().toprettyxml())
                # self.ios_parser.translate_metacli_to_cli(conf[1])
                # LOG.error(_('la configuration cli_driver de %s est  %s'), conf[1].name, self.ios_parser.configuration )

            LOG.error(_('Execution time is: %s'), time.time() - start_time)


    def _list_connected_vm(self, session, vm):
        vm_net_id = vm.virtual_network
        list_vm = (session.query(models.VirtualNode).
                   filter_by(type='vm', virtual_network=vm_net_id))
        list_vm = [vm_extracted for vm_extracted in list_vm if
                   vm_extracted.id != vm.id]
        return list_vm



