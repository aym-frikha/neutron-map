

__author__ = 'aymen'

from sqlalchemy.orm import exc
from oslo.db import exception as db_exc
from neutron.db import models_v2
from neutron.openstack.common import log
from neutron.plugins.map import models
from novaclient.client import Client
from oslo.config import cfg
import os
LOG = log.getLogger(__name__)


def add_target_network(session, target_network_id=None):
    try:
        with session.begin(subtransactions=True):
            if target_network_id is None:
                record = models.TargetNetwork()
            else:
                record = models.TargetNetwork(id=target_network_id)
            session.add(record)
        LOG.info(_("Added target network "
                   " %(network_id)s"),
                 {'network_id': record.id})
        return record
    except db_exc.DBDuplicateEntry:
        LOG.debug("Target network %s already bound", target_network_id)
        return (session.query(models.TargetNetwork).
                filter_by(id=target_network_id).one())
    except db_exc:
        LOG.debug("Target network cannot be added")


def add_generic_service(session, config, service, target_network):
    try:
        with session.begin(subtransactions=True):
            record = models.GenericService(
                name=service,
                target_network=target_network,
                config=config
            )
            session.add(record)
        LOG.info(_("Added generic service "
                   " %(service)s"),
                 {'service': service})
        return record
    except db_exc.DBDuplicateEntry:
        LOG.debug("Generic service %s already bound", service)
        return (session.query(models.GenericService).
                filter_by(name=service).one())
    except db_exc:
        LOG.debug("Generic service cannot be added")
    pass


def add_virtual_network(session, id, target_network):
    try:
        with session.begin(subtransactions=True):
            record = models.VirtualNetwork(
                id=id,
                target_network=target_network,
            )
            session.add(record)
        LOG.info(_("Added virtual network "
                   " %(v_net)s"),
                 {'v_net': id})
        return record
    except db_exc.DBDuplicateEntry:
        LOG.debug(" Virtual Network is %s already bound", record.id)
        return (session.query(models.VirtualNetwork).
                filter_by(id=record.id).one())
    except db_exc:
        LOG.debug("Virtual Network cannot be added")
    pass


def add_virtual_node(session, name, type, virtual_network, virtual_node_group):
    try:
        with session.begin(subtransactions=True):
            record = models.VirtualNode(
                name=name,
                type=type,
                virtual_network=virtual_network,
                virtual_node_group=virtual_node_group
            )
            session.add(record)
        LOG.info(_("Added virtual node "
                   " %(v_node)s"),
                 {'v_node': record.id})
        return record
    except db_exc.DBDuplicateEntry:
        LOG.debug(" Virtual Node is %s already bound", record.id)
        return (session.query(models.VirtualNode).
                filter_by(id=record.id).one())
    except db_exc:
        LOG.debug("Virtual Node cannot be added")
    pass


def add_virtual_link(session, name, virtual_network, cost=1):
    try:
        with session.begin(subtransactions=True):
            record = models.VirtualLink(
                name=name,
                cost=cost,
                virtual_network=virtual_network,
            )
            session.add(record)
        LOG.info(_("Added virtual link "
                   " %(v_link)s"),
                 {'v_link': record.id})
        return record
    except db_exc.DBDuplicateEntry:
        LOG.debug(" Virtual Link is %s already bound", record.id)
        return (session.query(models.VirtualLink).
                filter_by(id=record.id).one())
    except db_exc:
        LOG.debug("Virtual Link cannot be added")
    pass


def add_virtual_interface(session, name, type, link_id, virtual_node_id):
    try:
        with session.begin(subtransactions=True):
            record = models.VirtualInterface(
                name=name,
                type=type,
                link_id=link_id,
                virtual_node=virtual_node_id
            )
            session.add(record)
        LOG.info(_("Added virtual interface "
                   " %(v_interface)s"),
                 {'v_interface': record.id})
        return record
    except db_exc.DBDuplicateEntry:
        LOG.debug(" Virtual Interface is %s already bound", record.id)
        return (session.query(models.VirtualInterface).
                filter_by(id=record.id).one())
    except db_exc:
        LOG.debug("Virtual Interface cannot be added")
    pass


def add_virtual_node_group(session, type, virtual_network,
                           physical_node_attached):
    try:
        with session.begin(subtransactions=True):
            record = models.VirtualNodeGroup(
                type=type,
                virtual_network=virtual_network,
                physical_node_attached=physical_node_attached
            )
            session.add(record)
        LOG.info(_("Added virtual node group"
                   " %(v_node_group)s"),
                 {'v_node_group': record.id})
        return record
    except db_exc.DBDuplicateEntry:
        LOG.debug(" Virtual Node Group is %s already bound", id)
        return (session.query(models.VirtualNodeGroup).
                filter_by(id=record.id).one())
    except db_exc:
        LOG.debug("Virtual Node Group cannot be added")
    pass


def del_virtual_network(session, id, target_network):
    try:
        with session.begin(subtransactions=True):
            query = (session.query(models.VirtualNetwork).filter_by(id=id))
            query.delete()

            # record = models.VirtualNetwork(
            # id=id,
            # target_network=target_network,
            # )
            # session.delete(record)
        LOG.info(_("Removed virtual network "
                   " %(v_net)s"),
                 {'v_net': id})
        # return record
    except db_exc:
        LOG.debug("Virtual Network cannot be deleted")
    pass


def _add_physical_network(session, target_network, phys_net_name):
    try:
        with session.begin(subtransactions=True):
            if phys_net_name is None:
                phys_net_name = 'Default'
            record = models.PhysicalNetwork(
                name=phys_net_name,
                target_network=target_network
            )
            session.add(record)
        LOG.info(_("Added physical network "
                   " %(phys_net)s"),
                 {'phys_net': record.id})
        return record
    except db_exc.DBDuplicateEntry:
        LOG.debug("Physical Network %s already bound", phys_net_name)
        return (session.query(models.PhysicalNetwork).
                filter_by(name=phys_net_name).one())
    except db_exc:
        LOG.debug("Physical Network cannot be added")
    pass


def _add_phys_node_group(session, phys_net):
    try:
        with session.begin(subtransactions=True):
            record = models.PhysicalNodeGroup(
                physical_network=phys_net
            )
            session.add(record)
        LOG.info(_("Added physical node group"
                   " %(phys_node)s"),
                 {'phys_node': record.id})
        return record
    except db_exc.DBDuplicateEntry:
        LOG.debug("Physical Node Group %s already bound", record.id)
        return (session.query(models.PhysicalNodeGroup).
                filter_by(name=record.id).one())
    except db_exc:
        LOG.debug("Physical Node Group cannot be added")
    pass


def _add_phys_node(session, phys_net, phys_node, config, phys_group):
    try:
        with session.begin(subtransactions=True):
            record = models.PhysicalNode(
                name=phys_node[0],
                type=phys_node[2],
                address=phys_node[1],
                login=phys_node[3],
                password=phys_node[4],
                config=config,
                physical_network=phys_net,
                physical_node_group=phys_group
            )
            session.add(record)
        LOG.info(_("Added physical node "
                   " %(phys_node)s"),
                 {'phys_node': record.id})
        return record
    except db_exc.DBDuplicateEntry:
        LOG.debug("Physical Node %s already bound", record.id)
        return (session.query(models.PhysicalNode).
                filter_by(id=record.id).one())
    except db_exc:
        LOG.debug("Physical Node cannot be added")
    pass


def get_virtual_nodes(session, v_net):
    with session.begin(subtransactions=True):
        v_nodes = (session.query(models.VirtualNode).
                   filter(models.VirtualNode.virtual_network == v_net))
    if not v_nodes:
        LOG.debug("No virtual nodes present on the virtual network "
                  "%(v_net)s", {'v_net': v_net})
    return v_nodes.all()


def get_physical_nodes(session, phy_net):
    with session.begin(subtransactions=True):
        phy_nodes = (session.query(models.PhysicalNode).
                     filter(models.PhysicalNode.physical_network == phy_net))
    if not phy_nodes:
        LOG.debug("No physical nodes present on the physical network "
                  "%(phy_net)s", {'phy_net': phy_net})
    return phy_nodes.all()


def get_phys_net_from_v_node(session, v_node):
    with session.begin(subtransactions=True):
        v_node_group = session.query(models.VirtualNodeGroup).filter(
            models.VirtualNodeGroup.id == v_node.virtual_node_group).first()
        if v_node_group:
            phys_node_attached = session.query(models.PhysicalNode).filter(
                models.PhysicalNode.id == v_node_group.physical_node_attached).first()
            if not phys_node_attached:
                LOG.debug(
                    "The virtual node group %s doesn't belong to any physical node",
                    phys_node_attached.id)
    if not v_node_group:
        LOG.debug(
            "The virtual node %s doesn't belong to any virtual node group",
            v_node.id)
    return phys_node_attached.physical_network


def get_virtual_net_from_v_node(session, v_node):
    with session.begin(subtransactions=True):
        net = session.query(models_v2.Network).filter_by(
            id=v_node.virtual_network
        ).first()
    if not net:
        LOG.debug(
            "The virtual node %s doesn't belong to any virtual network",
            v_node.id)
    return net


def _add_phys_link(session, name, phys_net, cost=1, description=None):
    try:
        with session.begin(subtransactions=True):
            record = models.PhysicalLink(
                name=name,
                description=description,
                cost=cost,
                physical_network=phys_net,
            )
            session.add(record)
            LOG.info(_("Added physical link "
                       " %(phys_link)s"),
                     {'phys_link': record.id})
        return record
    except db_exc.DBDuplicateEntry:
        LOG.debug("Physical Link %s already bound", record.id)
        return (session.query(models.PhysicalLink).
                filter_by(id=record.id).one())
    except db_exc:
        LOG.debug("Physical Link cannot be added")
    pass


def _add_phys_interface(session, name, phys_link, phys_node, description=None,
                        type='ethernet', virtual_link_id=None,
                        physical_interface_group=None):
    try:
        with session.begin(subtransactions=True):
            record = models.PhysicalInterface(
                name=name,
                description=description,
                type=type,
                physical_link_id=phys_link,
                virtual_link_id=virtual_link_id,
                physical_node=phys_node,
                physical_interface_group=physical_interface_group
            )
            session.add(record)
            LOG.info(_("Added physical interface "
                       " %(phys_int)s"),
                     {'phys_int': record.id})
        return record
    except db_exc.DBDuplicateEntry:
        LOG.debug("Physical interface %s already bound", record.id)
        return (session.query(models.PhysicalInterface).
                filter_by(id=record.id).one())
    except db_exc:
        LOG.debug("Physical Interface cannot be added")
    pass




def make_phys_interface_dict(port):
    updated_port = {}
    updated_port['name'] = port.name
    updated_port['type'] = port.type
    updated_port['physical_link_id'] = port.physical_link_id
    updated_port['virtual_link_id'] = port.virtual_link_id
    updated_port['physical_node'] = port.physical_node
    updated_port['physical_interface_group'] = port.physical_interface_group
    return updated_port


def init_physical_infrastructure(context, matrix, target_network,
                                 resource_manager, phys_net_name=None):
    session = context.session
    if phys_net_name is None:
        phys_net_name = 'Default'
    phys_net = _add_physical_network(session, target_network, phys_net_name)
    phys_group = _add_phys_node_group(session, phys_net.id)
    phys_nodes = []
    # Add physical nodes from the configuration file to the data base
    for node in matrix[0]:
        node_info = node.split(',')
        if not  '#' in node_info[0]:
            node_name = node_info[0]
            if node_name + '.xml' in resource_manager.network_files:
                phys_nodes.append(
                    _add_phys_node(session, phys_net.id, node_info,
                                   os.path.join(resource_manager.
                                                service_path,
                                                node_name + '.xml'
                                   ), phys_group.id))
            else:
                LOG.info(_("le probleme est dans %s"),
                            node_info[0])
                phys_nodes.append(
                    _add_phys_node(session, phys_net.id, node_info,
                                   'none', phys_group.id))
                LOG.warning(_("Physical node %s has no configuration file"),
                            node_name)
    # Add Links and Interfaces to the data base
    for index in range(1, len(matrix)):
        for index_connection, connection in enumerate(matrix[index]):
            if index_connection != 0 and  not '#'  in connection:
                connection_info = connection.split(',')
                # query = session.query(models.PhysicalLink).filter_by(name=connection_info[0])
                # link_founded = session.query(literal(True)).filter(query.exists()).scalar()
                # Add links
                nbr_link_founded = (session.query(models.PhysicalLink).
                                    filter_by(name=connection_info[0])).count()
                # LOG.warning(_("nombre de liens trouve %s, pour le lien %s"),
                # nbr_link_founded, connection_info[0])
                if nbr_link_founded > 0:
                    phys_link = (session.query(models.PhysicalLink).
                                 filter_by(name=connection_info[0]).one())
                else:
                    phys_link = _add_phys_link(session, connection_info[0],
                                               phys_net.id)
                LOG.error(_("ligne est  %s, le contenu est %s"),index, connection)
                LOG.error(_("colonne est  %s"),index_connection)
                # Add first interface
                nbr_phys_int_founded = (session.query(models.PhysicalInterface).
                                        filter_by(
                    name=connection_info[1], physical_link_id=phys_link.id,
                    physical_node=phys_nodes[index - 1].id)).count()
                # LOG.warning(_("nombre de interface trouve %s, pour l'interface %s"),
                # nbr_phys_int_founded, connection_info[1])
                if nbr_phys_int_founded == 0:
                    _add_phys_interface(session, connection_info[1],
                                        phys_link.id,
                                        phys_nodes[index - 1].id)
                # Add second interface
                nbr_phys_int_founded = (session.query(models.PhysicalInterface).
                                        filter_by(
                    name=connection_info[2], physical_link_id=phys_link.id,
                    physical_node=phys_nodes[index_connection - 1].id)).count()
                # LOG.warning(_("nombre de interface trouve %s, pour l'interface %s"),
                # nbr_phys_int_founded, connection_info[2])
                if nbr_phys_int_founded == 0:
                    _add_phys_interface(session, connection_info[2],
                                        phys_link.id,
                                        phys_nodes[index_connection - 1].id)


def _get_hosts_info():
    # Extract Servers information from Nova
    try:
        keystone_conf = cfg.CONF.keystone_authtoken
        neutron_user = keystone_conf.admin_user
        neutron_password = keystone_conf.admin_password
        neutron_tenant = keystone_conf.admin_tenant_name
        neutron_endpoint = (keystone_conf.auth_protocol + '://'
                            + keystone_conf.auth_host
                            + ':' + repr(keystone_conf.auth_port) + '/v2.0')
        nova = Client('2', neutron_user, neutron_password, neutron_tenant,
                      neutron_endpoint)
        host_list = []

        hosts = nova.hosts.list()
        for host in hosts:
            if host.service == 'compute':
                host_list.append(host)
                LOG.debug(_("Nova host_name: %s"), host.host_name)
        return host_list
    except exc.NoResultFound:
        LOG.debug(_("MAP: got no result for Nova hosts"))
        return
    except Exception:
        LOG.exception(_("MAP: Exception!!"))



