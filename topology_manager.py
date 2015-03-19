from neutron.openstack.common import log
from neutron.plugins.map import models
from neutron.plugins.map import db as map_db
from neutron.plugins.map import YenKSP
from neutron.plugins.map import constants

LOG = log.getLogger(__name__)


def identify_virtual_physical_paths(session, path):
    result_path = []
    # TODO: Considerate multiple links between two nodes ==> Multiple interfaces
    #Order of adding node in the path is very important
    for index, node in enumerate(path):
        if type(node) is models.VirtualNode:
            if index > 0:
                int_g = get_connected_interface(session, node, path[index - 1])
                result_path.append({'node': node,
                                    'interface': int_g,
                                    'type': constants.VIRTUAL_NODE
                })
            if index < len(path) - 1:
                int_d = get_connected_interface(session, node, path[index + 1])
                result_path.append({'node': node,
                                    'interface': int_d,
                                    'type': constants.VIRTUAL_NODE
                })
        else:
            if index > 0:
                int_g = get_connected_interface(session, node, path[index - 1])
                result_path.append({'node': node,
                                    'interface': int_g,
                                    'type': constants.PHYSICAL_NODE
                })
            if index < len(path) - 1:
                int_d = get_connected_interface(session, node, path[index + 1])
                result_path.append({'node': node,
                                    'interface': int_d,
                                    'type': constants.PHYSICAL_NODE
                })

    return result_path


def identify_physical_l2_l3_paths(path):
    for node in path:
        if node['node'].type == 'switch' or node['node'].type == 'server' or \
                        node['type'] == constants.VIRTUAL_NODE:
            node['domain'] = constants.L2_DOMAIN
        elif node['node'].type == 'router':
            node['domain'] = constants.L3_DOMAIN
    return path


def get_connected_interface(session, node_source, node_dest):
    with session.begin(subtransactions=True):
        if type(node_source) is models.PhysicalNode:
            src_interfaces = (session.query(models.PhysicalInterface).
                              filter(
                models.PhysicalInterface.physical_node == node_source.id))
            if type(node_dest) is models.PhysicalNode:
                dest_interfaces = (session.query(models.PhysicalInterface).
                                   filter(
                    models.PhysicalInterface.physical_node == node_dest.id))

                for src_interface in src_interfaces:
                    for dest_interface in dest_interfaces:
                        if src_interface.physical_link_id == dest_interface.physical_link_id:
                            return src_interface
            elif type(node_dest) is models.VirtualNode:
                dest_interfaces = (session.query(models.VirtualInterface).
                                   filter(
                    models.VirtualInterface.virtual_node == node_dest.id))
                for src_interface in src_interfaces:
                    for dest_interface in dest_interfaces:
                        if src_interface.virtual_link_id == dest_interface.link_id:
                            return src_interface
        elif type(node_source) is models.VirtualNode:
            src_interfaces = (session.query(models.VirtualInterface).
                              filter(
                models.VirtualInterface.virtual_node == node_source.id))
            if type(node_dest) is models.PhysicalNode:
                dest_interfaces = (session.query(models.PhysicalInterface).
                                   filter(
                    models.PhysicalInterface.physical_node == node_dest.id))

                for src_interface in src_interfaces:
                    for dest_interface in dest_interfaces:
                        if src_interface.link_id == dest_interface.virtual_link_id:
                            return src_interface
            elif type(node_dest) is models.VirtualNode:
                dest_interfaces = (session.query(models.VirtualInterface).
                                   filter(
                    models.VirtualInterface.virtual_node == node_dest.id))
                for src_interface in src_interfaces:
                    for dest_interface in dest_interfaces:
                        if src_interface.link_id == dest_interface.link_id:
                            return src_interface
    pass


def get_node_neighbors(session, node):
    neighbors = {}
    with session.begin(subtransactions=True):
        if type(node) is models.PhysicalNode:
            interfaces = (session.query(models.PhysicalInterface).
                          filter(
                models.PhysicalInterface.physical_node == node.id))
            for interface in interfaces:
                if interface.physical_link_id:
                    connected_interface = (
                        session.query(models.PhysicalInterface).filter(
                            models.PhysicalInterface.physical_link_id == interface.physical_link_id,
                            models.PhysicalInterface.id != interface.id).first())
                    link = (session.query(models.PhysicalLink).
                            filter(
                        models.PhysicalLink.id == interface.physical_link_id).one())
                    neighbors[connected_interface.physical_node] = link.cost
                if interface.virtual_link_id:
                    connected_interface = (
                        session.query(models.VirtualInterface).
                        filter(
                            models.VirtualInterface.link_id == interface.virtual_link_id,
                            models.VirtualInterface.id != interface.id).first())
                    link = (session.query(models.VirtualLink).
                            filter(
                        models.VirtualLink.id == interface.virtual_link_id).one())
                    neighbors[connected_interface.virtual_node] = link.cost
        elif type(node) is models.VirtualNode:
            interfaces = (session.query(models.VirtualInterface).
                          filter(
                models.VirtualInterface.virtual_node == node.id).all())
            for interface in interfaces:
                connected_interface = (session.query(models.VirtualInterface).
                                       filter(
                    models.VirtualInterface.id != interface.id,
                    models.VirtualInterface.link_id == interface.link_id).first())
                link = (session.query(models.VirtualLink).
                        filter(
                    models.VirtualLink.id == interface.link_id).first())
                if not connected_interface:
                    connected_interface = (
                        session.query(models.PhysicalInterface).
                        filter(
                            models.PhysicalInterface.virtual_link_id == interface.link_id).first())
                    if connected_interface:
                        neighbors[connected_interface.physical_node] = link.cost
                else:
                    neighbors[connected_interface.virtual_node] = link.cost
                    continue
    return neighbors