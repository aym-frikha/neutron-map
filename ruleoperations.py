#!/usr/bin/env python
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# @author: Aymen Frikha, netvirt
# RuleOperations.py
# 25.07.2013

# # IF IN NEUTRON
from neutron.openstack.common import log as logging
from neutron.plugins.map import resources

LOG = logging.getLogger(__name__)


class RuleOperations():
    def __init__(self):
        self.operations = {
            "NodeValueEqual": self.node_value_equal,
            "NodeNotNull": self.node_not_null,
            "NodeDataEqual": self.node_data_equal,
            "BranchDataEqual": self.branche_data_equal,
            "IPAddressesHaveClassA": self.ip_address_have_class_A,
            "IPAddressesHaveClassB": self.ip_address_have_class_B,
            "IPAddressesHaveClassC": self.ip_address_have_class_C}

    def serialize_node_children(self, src_nodes, node_list):
        if src_nodes == None:
            return
        for node in src_nodes.Node:
            node_list.append(node)
            self.serialize_node_children(node.Children, node_list)

    def ip_address_have_class_C(self, l_node, r_node):
        # TODO: Implement this operation , verify that the ip address belong
        # to the class C
        return

    def ip_address_have_class_B(self, l_node, r_node):
        # TODO: Implement this operation , verify that the ip address belong
        # to the class B
        return

    def ip_address_have_class_A(self, l_node, r_node):
        # TODO: Implement this operation , verify that the ip address belong
        # to the class A
        return

    def branche_data_equal(self, l_node, r_node):
        result = True
        l_node_list = []
        l_node_list.append(l_node)
        self.serialize_node_children(l_node.Children, l_node_list)
        r_node_list = []
        r_node_list.append(r_node)
        self.serialize_node_children(r_node.Children, r_node_list)
        if len(l_node_list) != len(r_node_list):
            result = False
        else:
            l_iterator = iter(l_node_list)
            r_iterator = iter(r_node_list)
            ln = l_iterator.next()
            rn = r_iterator.next()
            while ln != None and rn != None:
                if ln.name != rn.name or ln.Value != rn.Value:
                    result = False
                    break
                try:
                    ln = l_iterator.next()
                    rn = r_iterator.next()
                except StopIteration:
                    pass
        return result

    def node_data_equal(self, l_node, r_node):
        result = False
        if type(l_node) != resources.Device.DevNode:
            return False
        if type(r_node) != resources.Device.DevNode:
            return False
        if l_node.name == r_node.name and l_node.Value == r_node.Value:
            result = True
        return result

    def node_value_equal(self, l_node, r_node):
        result = False
        if type(l_node) == resources.Device.DevNode:
            val1 = l_node.Value
        else:
            val1 = l_node
        if type(r_node) == resources.Device.DevNode:
            val2 = r_node.Value
        else:
            val2 = r_node
        if val1 == val2:
            result = True
        return result

    def node_not_null(self, l_node, r_node):
        result = False
        if type(l_node) == resources.Device.DevNode:
            val1 = l_node.Value
        else:
            val1 = l_node
        if type(r_node) == resources.Device.DevNode:
            val2 = r_node.Value
        else:
            val2 = r_node
        if val1 == val2 and val1 != '':
            result = True
        return result

    def execute_operation(self, op_name, l_node, r_node):
        if op_name == None or l_node == None or r_node == None:
            LOG.info(_("cannot execute operation, invalid arguments !!"))
            return False
        return self.operations[op_name](l_node, r_node)
                
