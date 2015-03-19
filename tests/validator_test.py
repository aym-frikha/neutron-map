#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Validator_test.py
#  Aymen
#  23.07.2013

from neutron.plugins.map import ruleoperations, resources
from neutron.plugins.map.fake_environment import _
from neutron.plugins.map.fake_environment import log
LOG = log()

class ValidatorTest(resources.DbManager, isolationprovider.IsolationProvider):

    def __init__(self, instances):
        super(Validator, self).__init__()
        self.m_device= resources.Device
        self.m_rule_op= resources.Rule.LogOperation()
        self.m_valid_message=""
        self.m_all_flag= False
        self.m_instances= instances
        self.m_operation= ruleoperations.RuleOperations()
        return
    def serialize_node(self, dev_nodes, ser_nodes):
        if dev_nodes == None:
            return
        for node in dev_nodes.Node:
            ser_nodes.append(node)
            self.serialize_node(node.Children, ser_nodes)
            
    def get_matching_devices(self, rule, tree_index, dev_liste):
        ops= []
        for op in rule.Conditions.Condition:
            if op.LeftTree == tree_index:
                ops.append(op.LeftOperand)
            if op.RightTree == tree_index:
                ops.append(op.RightOperand)
        for op in rule.Actions.Action:
            if op.LeftTree == tree_index:
                ops.append(op.LeftOperand)
            if op.RightTree == tree_index:
                ops.append(op.RightOperand)
        devices = self.get_all_devices()
        for dev in devices:
            has_all = True
            match = False
            dev_nodes=[] 
            self.serialize_node(dev.ConfigTree,dev_nodes)
            for arg in ops:
                found = False
                for tn in dev_nodes:
                    if tn.ReferenceList:
                        for a_ref in tn.ReferenceList.RefNode:
                            instance_name= a_ref.href.split(":")[0]
                            guid= a_ref.href.split(":")[1]
                            service_instance= self.get_instance_service_by_name(instance_name)
                            #print service_instance.InstanceOf.href +"=="+ arg.Node.ServiceRef
                            #print str(guid) +"=="+str(arg.Node.GUID)
                            #print str(service_instance.name in instances)
                            if (str(guid) ==str(arg.Node.GUID) and service_instance != None
                            and str(service_instance.InstanceOf.href)== str(arg.Node.ServiceRef) 
                            and service_instance.name in self.m_instances):
                                found = True
                                match= True
                                break
                has_all = has_all * found
                if has_all== False:
                    break
            if has_all and match:
                dev_liste.append(dev)
                LOG.info(_("Device %s has all nodes for rule %s"),dev.name, rule.name)
        return len(ops) != 0 
        
    def apply_operation(self, op, dev1, dev2):
        is_valid= True
        applied = False
        l_args=op.LeftOperand
        r_args= op.RightOperand
        l_dev= None
        r_dev= None
        if op.LeftTree== 1:
            l_dev= dev1
        if op.LeftTree ==2:
            l_dev = dev2
        if op.RightTree ==1:
            r_dev = dev1
        if op.RightTree ==2:
            r_dev = dev2
        if l_dev ==None:
            LOG.info(_("Failed to apply operation "+op.Operation+" left operand is null"))
            return False
        l_dev_nodes =[]
        self.serialize_node(l_dev.ConfigTree, l_dev_nodes)
        r_dev_nodes = []
        self.serialize_node(r_dev.ConfigTree, r_dev_nodes)
        for ln in l_dev_nodes:
            if ln.ReferenceList:
                for l_ref in  ln.ReferenceList.RefNode:
                    instance_name= l_ref.href.split(":")[0]
                    guid= l_ref.href.split(":")[1]
                    if str(guid)==str(l_args.Node.GUID):
                        l_si= self.get_instance_service_by_name(instance_name)
                        if (l_si != None and str(l_si.InstanceOf.href) == str(l_args.Node.ServiceRef) 
                        and l_si.name in self.m_instances):
                            if r_dev == None:
                                is_valid = is_valid and self.m_operation.execute_operation(op.Operation, ln, op.RightOperand.Value)
                                applied= True
                            else:
                                for rn in r_dev_nodes:
                                    if ln==rn:
                                        continue
                                    if rn.ReferenceList:
                                        for r_ref in rn.ReferenceList.RefNode:
                                            instance_name= r_ref.href.split(":")[0]
                                            guid= r_ref.href.split(":")[1]
                                            if str(guid) == str(r_args.Node.GUID):
                                                r_si = self.get_instance_service_by_name(instance_name)
                                                if (r_si != None and str(r_si.InstanceOf.href) == str(r_args.Node.ServiceRef) 
                                                and r_si.name in self.m_instances):
                                                    is_valid= is_valid and self.m_operation.execute_operation(op.Operation, ln, rn)
                                                    applied= True
        if applied == False:
            LOG.info(_("no matchig operands, could not apply operation" + op.Operation))
        return is_valid
        
    def apply_rule(self, rule, dev1, dev2):
        is_valid= True
        for op in rule.Conditions.Condition:
            result = self.apply_operation(op, dev1, dev2)
            if op.Negated:
                result = not result
            if op.LogicalOp == "and":
                is_valid= is_valid and result
            elif op.LogicalOp == "or":
                is_valid= is_valid or result
            else:
                is_valid = result
        if type(dev2) != type(None):
            message= "Condition for rule " + rule.name + " failed  for device " +dev1.name+ " and " + dev2.name 
        else:
            message= "Condition for rule " + rule.name + " failed  for device " +dev1.name
        if is_valid == False:
            LOG.inf(_(message))
            return is_valid
        
        for op in rule.Actions.Action:
            result = self.apply_operation(op, dev1, dev2)
            if op.Negated:
                result = not result
            if op.LogicalOp == "and":
                is_valid= is_valid and result
            elif op.LogicalOp == "or":
                is_valid= is_valid or result
            else:
                is_valid = result
        if type(dev2) != type(None):
            message= "Action for rule " + rule.name + " failed  for device " +dev1.name+ " and " + dev2.name 
        else:
            message= "Action for rule " + rule.name + " failed  for device " +dev1.name
        if is_valid == False:
            LOG.info(_(message))
            
        return is_valid
        
    def validate_rule(self, rule, dev_liste1, dev_liste2):
        is_valid= True
        if len(dev_liste1) > 0:
            for dev1 in dev_liste1:
                if len(dev_liste2) >0 :
                    for dev2 in dev_liste2:
                        if dev1.name == dev2.name:
                            continue
                        result= False
                        result= self.apply_rule(rule, dev1, dev2)
                        if result== False:
                            LOG.info(_("validation failed for rule "+ rule.name + " on devices" + dev1.name+ "and" + dev2.name))
                        is_valid = is_valid and result 
                else:
                    result= False
                    result = self.apply_rule(rule, dev1, None)
                    if result== False:
                        LOG.info(_("validation failed for rule "+ rule.name + " on device" + dev1.name))
                    is_valid = is_valid and result
        return is_valid
        
    def validate_instances(self):
        is_valid=True
        rules= self.get_all_rules()
        for rule in rules:
            dev_liste1= []
            dev_liste2= []
            found_ops= self.get_matching_devices(rule,1,dev_liste1)
            found_ops =True
            if found_ops and len(dev_liste1) == 0 :
                LOG.info(_("no devices match T1 operands for rule %s" ),rule.name)
            found_ops= self.get_matching_devices(rule,2,dev_liste2)
            if found_ops and len(dev_liste1) == 0 :
                LOG.info(_("no devices match T2 operands for rule %s" ), rule.name)
            is_valid= is_valid and self.validate_rule(rule,dev_liste1, dev_liste2)
        return is_valid
        
    def validate_all(self):
        is_valid=True
        m_all_flag =True
        is_valid= self.validate_instances()
        m_all_flag= False
        if is_valid:
            LOG.info(_("Successfully validated all"))
        
        return is_valid

    
