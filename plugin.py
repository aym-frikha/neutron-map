import os
from neutron.extensions import providernet as pnet
from oslo.config import cfg
from neutron.agent import securitygroups_rpc as sg_rpc
from neutron.db import db_base_plugin_v2, models_v2
from neutron.openstack.common import log
from neutron.plugins.map import db as map_db
from neutron.plugins.map import models
from neutron.plugins.map import resources
from neutron.plugins.map import infrastructure
from neutron.db import dvr_mac_db
from neutron.db import external_net_db
from neutron.db import securitygroups_rpc_base as sg_db_rpc
from neutron.db import agentschedulers_db
from neutron.db import allowedaddresspairs_db as addr_pair_db
from neutron.db import extradhcpopt_db
from neutron.common import rpc as n_rpc
from neutron.common import topics
from neutron.api.rpc.handlers import dhcp_rpc
from neutron.plugins.map import rpc
from neutron.common import constants as const
from neutron.api.rpc.agentnotifiers import dhcp_rpc_agent_api
from neutron.api.rpc.handlers import dvr_rpc
from neutron.api.rpc.handlers import securitygroups_rpc
from neutron.db import agents_db
from neutron.db import portbindings_base

from neutron.db import l3_gwmode_db

LOG = log.getLogger(__name__)

MAX_BIND_TRIES = 10

class MapPlugin(db_base_plugin_v2.NeutronDbPluginV2,
                dvr_mac_db.DVRDbMixin,
                external_net_db.External_net_db_mixin,
                sg_db_rpc.SecurityGroupServerRpcMixin,
                agentschedulers_db.DhcpAgentSchedulerDbMixin,
                addr_pair_db.AllowedAddressPairsMixin,
                extradhcpopt_db.ExtraDhcpOptMixin,
                portbindings_base.PortBindingBaseMixin,
                l3_gwmode_db.L3_NAT_db_mixin):
    __native_bulk_support = True
    __native_pagination_support = True
    __native_sorting_support = True

    # List of supported extensions
    _supported_extension_aliases = ["provider", "external-net", "binding",
                                    "quotas", "security-group", "agent",
                                    "dhcp_agent_scheduler",
                                    "multi-provider", "allowed-address-pairs",
                                    "extra_dhcp_opt"]

    @property
    def supported_extension_aliases(self):
        if not hasattr(self, '_aliases'):
            aliases = self._supported_extension_aliases[:]
            sg_rpc.disable_security_group_extension_by_config(aliases)
            self._aliases = aliases
        return self._aliases

    ''' Initialize physical infrastructure '''

    def _initialize_infrastructure(self, context):
        session = context.session
        # create target network
        self.target_net = map_db.add_target_network(session)
        #initialize available services
        for service in self.l2_services + self.l3_services:
            if service + '.xml' in self.resource_manager.service_files:
                map_db.add_generic_service(session, os.path.join(
                    self.resource_manager.service_path, service + '.xml'),
                                           service, self.target_net.id)
            else:
                map_db.add_generic_service(session, 'none', service,
                                           self.target_net.id)
                LOG.warning(_("Service %s has no configuration file"), service)
        #initialize physical infrastructure
        matrix = self.resource_manager.get_infrastructure_matrix()
        map_db.init_physical_infrastructure(context, matrix, self.target_net.id,
                                            self.resource_manager)
        self.infrastructure_initialized = True


    def __init__(self):
        self.infrastructure_initialized = False
        self.virtual_infrastructure_initialized = []
        super(MapPlugin, self).__init__()
        self.l2_services = cfg.CONF.map.l2_services
        self.l3_services = cfg.CONF.map.l3_services
        self.network_path = cfg.CONF.map.network_path
        self.resource_manager = resources.ResourceManager()
        self.infrastructure_manager = infrastructure.InfrastructureManager(
            self.resource_manager, self.l2_services, self.l3_services)
        self._setup_rpc()
        LOG.info(_("Modular Adaptive Plugin initialization complete"))

    def _setup_rpc(self):
        self.notifier = rpc.AgentNotifierApi(topics.AGENT)
        self.agent_notifiers[const.AGENT_TYPE_DHCP] = (
            dhcp_rpc_agent_api.DhcpAgentNotifyAPI()
        )

    def start_rpc_listeners(self):
        self.endpoints = [rpc.RpcCallbacks(),
                          securitygroups_rpc.SecurityGroupServerRpcCallback(),
                          dvr_rpc.DVRServerRpcCallback(),
                          dhcp_rpc.DhcpRpcCallback(),
                          agents_db.AgentExtRpcCallback()]
        self.topic = topics.PLUGIN
        self.conn = n_rpc.create_connection(new=True)
        self.conn.create_consumer(self.topic, self.endpoints,
                                  fanout=False)
        return self.conn.consume_in_threads()

    def create_network(self, context, network):
        session = context.session
        if self.infrastructure_initialized is False:
            self._initialize_infrastructure(context)
        with session.begin(subtransactions=True):
            #set up default security groups
            tenant_id = self._get_tenant_id_for_create(
                context, network['network'])
            self._ensure_default_security_group(context, tenant_id)

            net = super(MapPlugin, self).create_network(context, network)
            self._process_l3_create(context, net, network['network'])
            #MAP
            expected_neutron_net = (context.session.query(models_v2.Network).
                                    filter_by(name=net['name']).one())
            #Add mapping between network id and segmentation id
            # #TODO: This line is usuful only for the use cases
            self.infrastructure_manager.net_segmentation_id[
                expected_neutron_net.id] = network['network'][
                pnet.SEGMENTATION_ID]
            map_db.add_virtual_network(context.session, expected_neutron_net.id,
                                       self.target_net.id)
        return net

    def _update_virtual_infrastructure(self, session, virtual_network,
                                       physical_node_name):
        #TODO: This section must writed on the MAP Agent
        """

        :param session:
        :param virtual_network: Neutron Network
        :param physical_node_name:String: Physical Node where the virtual machine
        has been created
        """
        physical_node = (session.query(models.PhysicalNode).
                         filter_by(name=physical_node_name).one())
        #create virtual node group
        v_node_group = map_db.add_virtual_node_group(session, 'virtual_switch',
                                                     virtual_network['id']
                                                     , physical_node.id)
        #create virtual nodes (br_int)
        br_int = map_db.add_virtual_node(session, 'br_int', 'bridge',
                                         virtual_network['id'], v_node_group.id)
        #create virtual link between the bridge and eth1
        v_link = map_db.add_virtual_link(session, 'br_int-eth1',
                                         virtual_network['id'])
        #create virtual interface of the bridge
        v_interface = map_db.add_virtual_interface(session, 'br_int', 'virtio',
                                                   v_link.id, br_int.id)
        #add virtual link to the physical interface of the server
        LOG.error(_("Physical Node is %(phys)s"), {"phys": physical_node.id})
        physical_interface = (
            session.query(models.PhysicalInterface).filter_by(name='eth1',
                                                              physical_node=physical_node.id).one())
        physical_interface.virtual_link_id = v_link.id
        phys_int_dict = map_db.make_phys_interface_dict(physical_interface)
        physical_interface.update(phys_int_dict)
        self.virtual_infrastructure_initialized.append(physical_node_name)

    def _simulate_vm_creation_on_server(self, session, virtual_network,
                                        physical_node_name, start_time):
        """

        :param session:
        :param virtual_network:  Neutron Network
        :param physical_node_name: String: Physical Node where the virtual machine
        has been created
        """

        # Update model's virtual network for the virtual machine creation
        physical_node = (session.query(models.PhysicalNode).
                         filter_by(name=physical_node_name).one())
        v_node_group = (session.query(models.VirtualNodeGroup).
                        filter_by(type='virtual_switch',
                                  physical_node_attached=physical_node.id,
                                  virtual_network=virtual_network[
                                      'id']).first())
        vm = map_db.add_virtual_node(session, 'vm_test', 'vm',
                                     virtual_network['id'], v_node_group.id)
        v_link = map_db.add_virtual_link(session, 'vm-br_int',
                                         virtual_network['id'])
        br_int = (session.query(models.VirtualNode).
                  filter_by(name='br_int', virtual_node_group=v_node_group.id,
                            virtual_network=virtual_network['id']).one())

        map_db.add_virtual_interface(session, 'vm/br_int',
                                                      'virtio', v_link.id,
                                                      vm.id)
        map_db.add_virtual_interface(session, 'br_int/vm',
                                                          'virtio', v_link.id,
                                                          br_int.id)
        #Simulate the creation and deployment of services to connect the virtual
        # machine to the virtual network
        self.infrastructure_manager.connect_vm_to_network(session, vm, start_time)


    def create_port(self, context, port, start_time=0):
        session = context.session
        with session.begin(subtransactions=True):
            result = super(MapPlugin, self).create_port(context, port)
            network = self.get_network(context, result['network_id'])

            #TODO: Use case test for create Port
            server = result['device_owner']
            if server not in self.virtual_infrastructure_initialized:
                self._update_virtual_infrastructure(session, network, server)
                self._simulate_vm_creation_on_server(session, network, server, start_time)
        return result

