#!/usr/bin/env python
#
#  tests_domainkeeper.py
#  clement
#  17.07.2013

import copy

from neutron.plugins.map import domainkeeper
import topologymanager
from oslo.config import cfg


class TestDomainKeeper(object):

    def __init__(self):
        self.tm = topologymanager.TopologyManager()
        self.dk = domainkeeper.DomainKeeper(self.tm)
        self.last_test = ''
    
    """Load the topology from database"""
    def __test_load_db__(self, topo):
        self.tm.portmatrix = {}
        self.tm.next_broad_id = 0
        self.tm.broad_list = list()
        self.tm.broadcastmatrix = {}
        self.tm.__load_db__(topo)
        self.tm.update_broadcast_space(0)
    
    def test_add_domain(self):
        #~ add None domain
        self.t("add None domain")
        old_dom = copy.deepcopy(self.dk.domains)
        self.dk.add_domain(None, None, None, None, None)
        if not old_dom == self.dk.domains:
            return self.f()
        self.o()
        
        # add domain
        self.t("add domain")
        old_dom = copy.deepcopy(self.dk.domains)
        #domain_id, network_id, method, meth_id, port_list
        self.dk.add_domain('1', '42', 'FOO', '12','Fa0/1')
        for domain in self.dk.domains:
            for value in self.dk.domains[domain]:
                if not self.dk.domains[domain][value] == old_dom[domain][value] and domain != '1':
                    return self.f()
        if not self.dk.domains['1']['nodes'] == old_dom['1']['nodes']:
            return self.f()
        if not self.dk.domains['1']['type'] == old_dom['1']['type']:
            return self.f()
        for isolation in self.dk.domains['1']['isolations']:
            if not isolation['network_id'] == '42':
                if not isolation in old_dom['1']['isolations']:
                    return self.f()
            else:
                if not isolation == {'network_id': '42', 
                                     'method': ('FOO', '12', 'Fa0/1')}:
                    return self.f()
        self.o()
        return True

    def test_get_domain(self):
        # topologie vide
        #~ self.__test_load_db__("TopologyManagerDB/topo.db")
        #~ self.dk = domainkeeper.DomainKeeper(self.tm)
        #tests get none domain
        self.t("get none domain")
        domain = self.dk.get_domain(None)
        if not domain == None:
            return self.f()
        self.o()
        
        #tests get non existing domain
        self.t("get non existing domain")
        domain = self.dk.get_domain('-1')
        if not domain == []:
            return self.f()
        self.o()
        
        #tests get existing domain
        self.t("get existing domain")
        node = self.dk.topology_manager.portmatrix.keys()[0]
        domains = self.dk.get_domain([node])
        for domain in domains:
            if not node in self.dk.domains[domain]['nodes']:
                return self.f()
        for other_domain in self.dk.domains:
            if other_domain not in domains:
                if node in other_domain:
                    return self.f()
        self.o()

        return True

    def get_isolation(self, domain, network):
        return True
   
    def get_type(self, domain_id):
        return True

    def get_isolation_nextid(self, domain, method):
        return True
        
    def get_port_list(self, hotes):
        return True

    def recalculate_domains(self):
        #tests get no change on domain
        self.t("get no change on domain")
        self.dk.recalculate_domains()
        old = str(self.dk.domains)
        self.dk.recalculate_domains()
        if not str(self.dk.domains) == old:
            print str(self.dk.domains)
            print old
            return self.f()
        self.o()
        return True

    def f(self):
        print "[FAIL]", self.last_test
        return False

    def o(self):
        print "[OK]", self.last_test

    def t(self, test_text):
        self.last_test = test_text
        
if __name__ == "__main__":
    cfg.CONF(args=['--config-file', 'example_conf.ini'], project='neutron', version='1')
    dk = TestDomainKeeper()
    nbTest = 0.0
    nbFail = 0.0

    # tests add domain
    print "\n##Test add domain##"
    nbTest+=1
    if not dk.test_add_domain():
        print "Test add domain\t[FAIL]"
        nbFail+=1
    else: print "Test add domain\t[OK]"
    
    # tests get domain
    print "\n##Test get domain##"
    nbTest+=1
    if not dk.test_get_domain():
        print "Test get domain\t[FAIL]"
        nbFail+=1
    else: print "Test get domain\t[OK]"
    
    # tests recalculate_domains
    print "\n##Test recalculate_domains##"
    nbTest+=1
    if not dk.recalculate_domains():
        print "Test recalculate_domains\t[FAIL]"
        nbFail+=1
    else: print "Test recalculate_domains\t[OK]"
    
    print "\nResults: %d%% success !" % ((nbTest - nbFail)/ nbTest *100.0)
