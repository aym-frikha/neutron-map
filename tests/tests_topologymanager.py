#!/usr/bin/env python
#
#  tests_topologymanager.py
#  clement
#  16.07.2013
import copy

from neutron.plugins.map import topologymanager

class TestTopologyManager(object):

    def __init__(self):
        self.tm = topologymanager.TopologyManager()
        self.last_test = ''

    def test_get_paths(self):
        # topologie vide
        self.__test_load_db__("TopologyManagerDB/vide.db")
        self.t("get path None")
        path = self.tm.get_paths(None)
        if not path == []:
            return self.f()
        self.o()
        
        self.t("get path unexisting hote")
        path = self.tm.get_paths(['1'])
        if not path == []:
            return self.f()
        self.o()
        
        self.t("get path 2 unexisting hotes")
        path = self.tm.get_paths(['1', '2'])
        if not path == []:
            return self.f()
        self.o()
        
        # topologie existante
        self.__test_load_db__("TopologyManagerDB/topo.db")
        self.t("get path None")
        path = self.tm.get_paths(None)
        if not path == []:
            return self.f()
        self.o()
        
        self.t("get path unexisting hote")
        path = self.tm.get_paths(['-1'])
        if not path == []:
            return self.f()
        self.o()
        
        self.t("get path 2 unexisting hotes")
        path = self.tm.get_paths(['-1', '-2'])
        if not path == []:
            return self.f()
        self.o()
        
        self.t("get path existing hote")
        path = self.tm.get_paths(['1'])
        if not path == []:
            return self.f()
        self.o()
        
        self.t("get path 2 existing hotes")
        path = self.tm.get_paths(['1', '2'])
        if not path == [[('1', 'Fa0/0'), ('3', 'Fa0/0'), ('3', 'Fa0/1'), ('2', 'Fa0/0')]]:
            return self.f()
        self.o()
        
        #add broadcast
        self.tm.add_broadcast_space(['1','3','2'])
        self.t("get path None")
        path = self.tm.get_paths(None)
        if not path == []:
            return self.f()
        self.o()
        
        self.t("get path unexisting hote")
        path = self.tm.get_paths(['-1'])
        if not path == []:
            return self.f()
        self.o()
        
        self.t("get path 2 unexisting hotes")
        path = self.tm.get_paths(['-1', '-2'])
        if not path == []:
            return self.f()
        self.o()
        
        self.t("get path existing hote")
        path = self.tm.get_paths(['1'])
        if not path == []:
            return self.f()
        self.o()
        
        self.t("get path 2 existing hotes")
        path = self.tm.get_paths(['1', '2'])
        if not path == [[('1', ['Fa0/0']), ('2', ['Fa0/0'])]]:
            return self.f()
        self.o()
        
        self.t("get path 2 existing hotes")
        path = self.tm.get_paths(['3', '1'])
        if not path == [[('3', ['Fa0/0','Fa0/1']), ('1', ['Fa0/0'])]]:
            print path
            return self.f()
        self.o()
        return True

    def test_update_node(self):
        # topologie vide
        self.__test_load_db__("TopologyManagerDB/vide.db")
        
        # add None node
        self.t("add None node")
        tmold = copy.deepcopy(self.tm)
        self.tm.update_node(None, "ADD")
        if self.tm.portmatrix != tmold.portmatrix:
            return self.f()
        self.o()
        
        # add node
        self.t("add node")
        self.tm.update_node("Node1", "ADD")
        if not len(self.tm.portmatrix.keys()) == 1:
            return self.f()
        for node in self.tm.portmatrix.keys():
            if node != "Node1":
                return self.f()
        self.o()
        
        # del None node
        self.t("del None node")
        tmold = copy.deepcopy(self.tm)
        self.tm.update_node(None, "DEL")
        if tmold.portmatrix != self.tm.portmatrix:
            return self.f()
        self.o()
        
        #del existing node
        self.t("del node")
        tmold = copy.deepcopy(self.tm)
        self.tm.update_node("Node1", "DEL")
        if len(self.tm.portmatrix) != (len(tmold.portmatrix)-1):
            return self.f()
        for node in self.tm.portmatrix.keys():
            if node not in tmold.portmatrix:
                return self.f()
        for node in tmold.portmatrix.keys():
            if node not in self.tm.portmatrix and node != "Node1":
                return self.f()
        self.o()
        
        #del non-existing node
        self.t("del non-existing node")
        tmold = copy.deepcopy(self.tm)
        self.tm.update_node("Node2", "DEL")
        if len(self.tm.portmatrix) != len(tmold.portmatrix):
            return self.f()
        for node in self.tm.portmatrix.keys():
            if node not in tmold.portmatrix:
                return self.f()
        for node in tmold.portmatrix.keys():
            if node not in self.tm.portmatrix:
                return self.f()
        self.o()
        
        # topologie existante
        self.__test_load_db__("TopologyManagerDB/topo.db")
        
        # add None node
        self.t("add None node")
        self.tm.update_node(None, "ADD")
        if len(self.tm.portmatrix.keys()) == 1:
            return self.f()
        for node in self.tm.portmatrix.keys():
            if node == None:
                return self.f()
        self.o()
        
        # add node
        self.t("add node")
        tmold = copy.deepcopy(self.tm)
        self.tm.update_node("Node1", "ADD")
        if not len(self.tm.portmatrix.keys()) == (len(tmold.portmatrix.keys())+1):
            return self.f()
        for node in self.tm.portmatrix.keys():
            if node != "Node1" and node not in tmold.portmatrix.keys():
                self.f()
        for node in tmold.portmatrix.keys():
            if node not in self.tm.portmatrix.keys():
                self.f()
        self.o()
        
        # del None node
        self.t("del None node")
        tmold = copy.deepcopy(self.tm)
        self.tm.update_node(None, "DEL")
        if tmold.portmatrix != self.tm.portmatrix:
            return self.f()
        self.o()
        
        #del existing node
        self.t("del node")
        tmold = copy.deepcopy(self.tm)
        self.tm.update_node("Node1", "DEL")
        if len(self.tm.portmatrix) != (len(tmold.portmatrix)-1):
            return self.f()
        for node in self.tm.portmatrix.keys():
            if node not in tmold.portmatrix:
                return self.f()
        for node in tmold.portmatrix.keys():
            if node not in self.tm.portmatrix and node != "Node1":
                return self.f()
        self.o()
        
        #del non-existing node
        self.t("del non-existing node")
        tmold = copy.deepcopy(self.tm)
        self.tm.update_node("Node2", "DEL")
        if len(self.tm.portmatrix) != len(tmold.portmatrix):
            return self.f()
        for node in self.tm.portmatrix.keys():
            if node not in tmold.portmatrix:
                return self.f()
        for node in tmold.portmatrix.keys():
            if node not in self.tm.portmatrix:
                return self.f()
        self.o()
        
        #other state than ADD or DEL
        self.t("other state")
        tmold = copy.deepcopy(self.tm)
        self.tm.update_node(None, "FOO")
        for node in self.tm.portmatrix.keys():
            if node not in tmold.portmatrix:
                return self.f()
        for node in tmold.portmatrix.keys():
            if node not in self.tm.portmatrix:
                return self.f()
        self.o()
        return True

    def test_update_link(self):
        # topologie vide
        self.__test_load_db__("TopologyManagerDB/vide.db")
        
        # update None link
        self.t("up None link")
        self.tm.update_link(None, None, None, None, "UP")
        if len(self.tm.portmatrix.keys()) == 1:
            return self.f()
        for node in self.tm.portmatrix.keys():
            if node == None:
                return self.f()
        self.o()
        
        # up link
        self.t("up link with non existing node")
        self.tm.update_link("Node1", "Port1", "Node2", "Port2", "UP")
        if not len(self.tm.portmatrix.keys()) == 0:
            return self.f()
        self.o()
        
        # update None link
        self.t("down None link")
        self.tm.update_link(None, None, None, None, "DOWN")
        if len(self.tm.portmatrix.keys()) == 1:
            return self.f()
        for node in self.tm.portmatrix.keys():
            if node == None:
                return self.f()
        self.o()
        
        # topologie existante
        self.__test_load_db__("TopologyManagerDB/topo.db")
        
        # up link None node
        self.t("link None node")
        tmold = copy.deepcopy(self.tm)
        self.tm.update_link(None, None, None, None, "UP")
        if not len(self.tm.portmatrix.keys()) == len(tmold.portmatrix.keys()):
            return self.f()
        for node in self.tm.portmatrix:
            if node not in tmold.portmatrix:
                return self.f()
            for dest in self.tm.portmatrix[node].keys():
                if self.tm.portmatrix[node][dest] != tmold.portmatrix[node][dest]:
                    return self.f()
        for node in tmold.portmatrix:
            if node not in self.tm.portmatrix:
                return self.f()
            for dest in tmold.portmatrix[node].keys():
                if self.tm.portmatrix[node][dest] != tmold.portmatrix[node][dest]:
                    return self.f()
        self.o()
        
        # up link
        self.t("up link")
        tmold = copy.deepcopy(self.tm)
        self.tm.update_link("1", "1/2", "2", "2/1", "UP")
        if not self.tm.portmatrix.has_key("1"):
            return self.f()
        if not self.tm.portmatrix["1"].has_key("2"):
            return self.f()
        if not self.tm.portmatrix["1"]["2"] == {'port':"1/2"}:
            return self.f()

        if not self.tm.portmatrix.has_key("2"):
            return self.f()
        if not self.tm.portmatrix["2"].has_key("1"):
            return self.f()
        if not self.tm.portmatrix["2"]["1"] == {'port':"2/1"}:
            return self.f()
        for node in self.tm.portmatrix.keys():
            if node not in tmold.portmatrix:
                return self.f()
        for node in tmold.portmatrix.keys():
            if node not in self.tm.portmatrix:
                return self.f()
        self.o()
        
        # down None link
        self.t("down None link")
        tmold = copy.deepcopy(self.tm)
        self.tm.update_link(None, None, None, None, "DOWN")
        if not len(self.tm.portmatrix.keys()) == len(tmold.portmatrix.keys()):
            return self.f()

        for node in self.tm.portmatrix:
            if node not in tmold.portmatrix:
                return self.f()
            for dest in self.tm.portmatrix[node].keys():
                if self.tm.portmatrix[node][dest] != tmold.portmatrix[node][dest]:
                    return self.f()
        for node in tmold.portmatrix:
            if node not in self.tm.portmatrix:
                return self.f()
            for dest in tmold.portmatrix[node].keys():
                if self.tm.portmatrix[node][dest] != tmold.portmatrix[node][dest]:
                    return self.f()
        self.o()
        
        #down existing link
        self.t("down existing link")
        tmold = copy.deepcopy(self.tm)
        self.tm.update_link("1", "1/2", "2", "2/1", "DOWN")
        if not len(self.tm.portmatrix.keys()) == (len(tmold.portmatrix.keys())):
            return self.f()
        
        if not self.tm.portmatrix.has_key("1"):
            return self.f()
        if self.tm.portmatrix["1"].has_key("2"):
            return self.f()

        if not self.tm.portmatrix.has_key("2"):
            return self.f()
        if self.tm.portmatrix["2"].has_key("1"):
            return self.f()

        for node in self.tm.portmatrix.keys():
            if node not in tmold.portmatrix:
                return self.f()
        for node in tmold.portmatrix.keys():
            if node not in self.tm.portmatrix:
                return self.f()
        self.o()

        #down existing link, unknown ports
        self.t("down existing link, none port")
        tmold = copy.deepcopy(self.tm)
        self.tm.update_link("1", None, "2", None, "DOWN")
        if not len(self.tm.portmatrix.keys()) == (len(tmold.portmatrix.keys())):
            return self.f()
        
        if not self.tm.portmatrix.has_key("1"):
            return self.f()
        if self.tm.portmatrix["1"].has_key("2"):
            return self.f()

        if not self.tm.portmatrix.has_key("2"):
            return self.f()
        if self.tm.portmatrix["2"].has_key("1"):
            return self.f()

        for node in self.tm.portmatrix:
            if node not in tmold.portmatrix:
                return self.f()
            for dest in self.tm.portmatrix[node].keys():
                if self.tm.portmatrix[node][dest] != tmold.portmatrix[node][dest]:
                    return self.f()
        for node in tmold.portmatrix:
            if node not in self.tm.portmatrix:
                return self.f()
            for dest in tmold.portmatrix[node].keys():
                if self.tm.portmatrix[node][dest] != tmold.portmatrix[node][dest]:
                    return self.f()
        self.o()
        
        #down unexisting link
        self.t("down unexisting link, none port")
        tmold = copy.deepcopy(self.tm)
        self.tm.update_link("1", None, "4", None, "DOWN")
        if not len(self.tm.portmatrix.keys()) == (len(tmold.portmatrix.keys())):
            return self.f()

        for node in self.tm.portmatrix:
            if node not in tmold.portmatrix:
                return self.f()
            for dest in self.tm.portmatrix[node].keys():
                if self.tm.portmatrix[node][dest] != tmold.portmatrix[node][dest]:
                    return self.f()
        for node in tmold.portmatrix:
            if node not in self.tm.portmatrix:
                return self.f()
            for dest in tmold.portmatrix[node].keys():
                if self.tm.portmatrix[node][dest] != tmold.portmatrix[node][dest]:
                    return self.f()
        
        self.o()
        
        #other state than ADD or DEL
        self.t("other state")
        tmold = copy.deepcopy(self.tm)
        self.tm.update_link(None, None, None, None, "FOO")
        for node in self.tm.portmatrix:
            if node not in tmold.portmatrix:
                return self.f()
            for dest in self.tm.portmatrix[node].keys():
                if self.tm.portmatrix[node][dest] != tmold.portmatrix[node][dest]:
                    return self.f()
        for node in tmold.portmatrix:
            if node not in self.tm.portmatrix:
                return self.f()
            for dest in tmold.portmatrix[node].keys():
                if self.tm.portmatrix[node][dest] != tmold.portmatrix[node][dest]:
                    return self.f()
        self.o()
        return True

    def test_add_broadcast_space(self):
        # topologie vide
        self.__test_load_db__("TopologyManagerDB/vide.db")
        # add None devices
        self.t("add None devices")
        self.tm.add_broadcast_space(None, None)
        if not len(self.tm.portmatrix.keys()) == 0:
            return self.f()
        for node in self.tm.portmatrix.keys():
            if node == None:
                return self.f()
        if not len(self.tm.broadcastmatrix.keys()) == 0:
            return self.f()
        for node in self.tm.broadcastmatrix.keys():
            if node == None:
                return self.f()
        self.o()
        
        # add unexisting devices
        self.t("add unexisting devices")
        self.tm.add_broadcast_space(['1'], ['1'])
        if not len(self.tm.portmatrix.keys()) == 0:
            return self.f()
        for node in self.tm.portmatrix.keys():
            if node == None:
                return self.f()
        if not len(self.tm.broadcastmatrix.keys()) == 0:
            return self.f()
        for node in self.tm.broadcastmatrix.keys():
            if node == None:
                return self.f()
        self.o()

        # topologie existante
        self.__test_load_db__("TopologyManagerDB/topo.db")
        
        # add None devices
        self.t("add None devices")
        oldpm = copy.deepcopy(self.tm.portmatrix)
        oldbm = copy.deepcopy(self.tm.broadcastmatrix)
        self.tm.add_broadcast_space(None, None)
        if oldpm != self.tm.portmatrix:
            return self.f()
        if oldbm != self.tm.broadcastmatrix:
            return self.f()
        self.o()
        
        # add unexisting devices
        self.t("add unexisting devices")
        oldpm = copy.deepcopy(self.tm.portmatrix)
        oldbm = copy.deepcopy(self.tm.broadcastmatrix)
        self.tm.add_broadcast_space(['-1'], ['-1'])
        if oldpm != self.tm.portmatrix:
            return self.f()
        if oldbm != self.tm.broadcastmatrix:
            return self.f()
        self.o()
        
        # add existing devices
        self.t("add existing devices")
        oldpm = copy.deepcopy(self.tm.portmatrix)
        self.tm.add_broadcast_space(['1', '2', '3'])
        if oldpm != self.tm.portmatrix:
            return self.f()
        if not self.tm.broadcastmatrix.has_key('b0'):
            return self.f()
        for key in ['1','2','3']:
            if not self.tm.broadcastmatrix['b0'].has_key(key):
                return self.f()
            if not self.tm.broadcastmatrix['b0'][key] == {'port':[]}:
                return self.f()
        for key in ['1','2']:
            if not self.tm.broadcastmatrix[key].has_key('b0'):
                return self.f()
            if not self.tm.broadcastmatrix[key]['b0'] == {'port':['Fa0/0']}:
                return self.f()
        for key in ['3']:
            if not self.tm.broadcastmatrix[key].has_key('b0'):
                return self.f()
            if not self.tm.broadcastmatrix[key]['b0'] == {'port':['Fa0/0','Fa0/1']}:
                return self.f()
        self.o()
        
        # merge broadcast spaces
        self.t("add existing devices, merge")
        oldpm = copy.deepcopy(self.tm.portmatrix)
        self.tm.add_broadcast_space(['1', '4'], ['1'])
        if oldpm != self.tm.portmatrix:
            return self.f()
        if not self.tm.broadcastmatrix.has_key('b0'):
            return self.f()
        for key in ['1', '2', '3', '4']:
            if not self.tm.broadcastmatrix['b0'].has_key(key):
                return self.f()
            if not self.tm.broadcastmatrix['b0'][key] == {'port':[]}:
                return self.f()
        self.o()
        return True

    def test_update_broadcast_space(self):
        # topologie vide
        self.__test_load_db__("TopologyManagerDB/vide.db")
        # update None space
        self.t("update None space")
        self.tm.update_broadcast_space(None)
        if not len(self.tm.portmatrix.keys()) == 0:
            return self.f()
        for node in self.tm.portmatrix.keys():
            if node == None:
                return self.f()
        if not len(self.tm.broadcastmatrix.keys()) == 0:
            return self.f()
        for node in self.tm.broadcastmatrix.keys():
            if node == None:
                return self.f()
        self.o()
        
        # update unexisting space
        self.t("update unexisting space")
        self.tm.update_broadcast_space('-1')
        if not len(self.tm.portmatrix.keys()) == 0:
            return self.f()
        for node in self.tm.portmatrix.keys():
            if node == None:
                return self.f()
        if not len(self.tm.broadcastmatrix.keys()) == 0:
            return self.f()
        for node in self.tm.broadcastmatrix.keys():
            if node == None:
                return self.f()
        self.o()

        # topologie existante
        self.__test_load_db__("TopologyManagerDB/topo.db")
        
        # update None space
        self.t("update None spaces")
        oldpm = copy.deepcopy(self.tm.portmatrix)
        oldbm = copy.deepcopy(self.tm.broadcastmatrix)
        self.tm.update_broadcast_space(None)
        if oldpm != self.tm.portmatrix:
            return self.f()
        if oldbm != self.tm.broadcastmatrix:
            return self.f()
        self.o()
        
        # update unexisting space
        self.t("update unexisting space")
        oldpm = copy.deepcopy(self.tm.portmatrix)
        oldbm = copy.deepcopy(self.tm.broadcastmatrix)
        self.tm.update_broadcast_space('-1')
        if oldpm != self.tm.portmatrix:
            return self.f()
        if oldbm != self.tm.broadcastmatrix:
            return self.f()
        self.o()
        
        # update unexisting space
        self.t("update unexisting space")
        oldpm = copy.deepcopy(self.tm.portmatrix)
        oldbm = copy.deepcopy(self.tm.broadcastmatrix)
        self.tm.update_broadcast_space('1')
        if oldpm != self.tm.portmatrix:
            return self.f()
        if oldbm != self.tm.broadcastmatrix:
            return self.f()
        self.o()
        
        # update existing space
        self.t("update existing space")
        self.tm.add_broadcast_space(['1','2','3'])
        self.tm.update_node('9','ADD')
        oldpm = copy.deepcopy(self.tm.portmatrix)
        self.tm.update_broadcast_space('b0')
        if oldpm != self.tm.portmatrix:
            return self.f()
        if not self.tm.broadcastmatrix.has_key('b0'):
            return self.f()
        if not self.tm.broadcastmatrix.has_key('9'):
            return self.f()
        for key in ['1','2','3']:
            if not self.tm.broadcastmatrix['b0'].has_key(key):
                return self.f()
            if not self.tm.broadcastmatrix['b0'][key] == {'port':[]}:
                return self.f()
        for key in ['1','2']:
            if not self.tm.broadcastmatrix[key].has_key('b0'):
                return self.f()
            if not self.tm.broadcastmatrix[key]['b0'] == {'port':['Fa0/0']}:
                print self.tm.broadcastmatrix[key]['b0'], key
                return self.f()
        for key in ['3']:
            if not self.tm.broadcastmatrix[key].has_key('b0'):
                return self.f()
            if not self.tm.broadcastmatrix[key]['b0'] == {'port':['Fa0/0','Fa0/1']}:
                return self.f()
        self.o()
        return True

    def test_get_port(self):
        # topologie vide
        self.__test_load_db__("TopologyManagerDB/vide.db")

        # get None port
        self.t("get None port")
        port = self.tm.get_port(None, None, None)
        if port != None:
            return self.f()
        self.o()
        
        # get unexisting port
        self.t("get unexisting port")
        port = self.tm.get_port('1', '2', None)
        if port != None:
            return self.f()
        self.o()

        # topologie existante
        self.__test_load_db__("TopologyManagerDB/topo.db")
        
        # get None port
        self.t("get None port")
        port = self.tm.get_port(None, None, None)
        if port != None:
            return self.f()
        self.o()
        
        # get unexisting port
        self.t("get unexisting port")
        port = self.tm.get_port('1', '2', None)
        if port != None:
            return self.f()
        self.o()
        
        # get existing port
        self.t("get existing port")
        port = self.tm.get_port('1', '3', None)
        if port != 'Fa0/0':
            return self.f()
        self.o()
        return True

    def test_intersect(self):
        list1=['1', '2', '3']
        list2=['3', '4', '5']
        self.t("intersect ['1', '2', '3'], ['3', '4', '5']")
        if self.tm.intersect(list1, list2) == ['3']:
            self.o()
            return True
        return self.f()
        
    def test_get_broadcast_spaces(self):
        # topologie vide
        self.__test_load_db__("TopologyManagerDB/vide.db")

        # get None device
        self.t("get None device")
        broad = self.tm.__get_broadcast_spaces__(None)
        if broad != []:
            return self.f()
        self.o()
        
        # get non-existing device
        self.t("get non-existing device")
        broad = self.tm.__get_broadcast_spaces__(['-1'])
        if broad != []:
            return self.f()
        self.o()
        
        # topologie non vide
        self.__test_load_db__("TopologyManagerDB/topo.db")
        self.tm.add_broadcast_space(['1','2','3'])
        
        # get None device
        self.t("get None device")
        broad = self.tm.__get_broadcast_spaces__(None)
        if broad != []:
            return self.f()
        self.o()
        
        # get non-existing device
        self.t("get non-existing device")
        broad = self.tm.__get_broadcast_spaces__(['-1'])
        if broad != []:
            return self.f()
        self.o()
        
        # get one existing device
        self.t("get one existing device")
        broad = self.tm.__get_broadcast_spaces__(['1'])
        if broad != ['b0']:
            return self.f()
        self.o()
        
        # get one existing device
        self.t("get several existing devices")
        broad = self.tm.__get_broadcast_spaces__(['1', '2'])
        if broad != ['b0']:
            return self.f()
        self.o()
        
        self.tm.add_broadcast_space(['4','5','6'])
        # get None device
        self.t("get None device")
        broad = self.tm.__get_broadcast_spaces__(None)
        if broad != []:
            return self.f()
        self.o()
        
        # get non-existing device
        self.t("get non-existing device")
        broad = self.tm.__get_broadcast_spaces__(['-1'])
        if broad != []:
            return self.f()
        self.o()
        
        # get one existing device
        self.t("get one existing device")
        broad = self.tm.__get_broadcast_spaces__(['1'])
        if broad != ['b0']:
            return self.f()
        self.o()
        
        # get one existing device
        self.t("get several existing devices")
        broad = self.tm.__get_broadcast_spaces__(['1', '2'])
        if broad != ['b0']:
            return self.f()
        self.o()
        
        # get one existing device
        self.t("get several existing devices")
        broad = self.tm.__get_broadcast_spaces__(['1', '4'])
        if broad != ['b0', 'b1']:
            return self.f()
        self.o()
        
        # get one existing device
        self.t("get several existing devices")
        broad = self.tm.__get_broadcast_spaces__(['5', '4'])
        if broad != ['b1']:
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

    """Load the topology from database"""
    def __test_load_db__(self, topo):
        self.tm.portmatrix = {}
        self.tm.next_broad_id = 0
        self.tm.broad_list = list()
        self.tm.broadcastmatrix = {}
        self.tm.__load_db__(topo)
        self.tm.update_broadcast_space(0)
        
if __name__ == "__main__":
    tm = TestTopologyManager()
    nbTest = 0.0
    nbFail = 0.0

    # tests update node
    print "\n##Test update node##"
    nbTest+=1
    if not tm.test_update_node():
        print "Test update node\t[FAIL]"
        nbFail+=1
    else: print "Test update node\t[OK]"
    
    # tests update link
    print "\n##Test update link##"
    nbTest+=1
    if not tm.test_update_link():
        print "Test update link\t[FAIL]"
        nbFail+=1
    else: print "Test update link\t[OK]"
    
    # tests get port
    nbTest+=1
    print "\n##Test get port##"
    if not tm.test_get_port():
        print "Test get port\t[FAIL]"
        nbFail+=1
    else: print "Test get port\t[OK]"
    
    # tests add broadcast space
    nbTest+=1
    print "\n##Test add broadcast space##"
    if not tm.test_add_broadcast_space():
        print "Test add broadcast space\t[FAIL]"
        nbFail+=1
    else: print "Test add broadcast space\t[OK]"
    
    # tests update broadcast space
    nbTest+=1
    print "\n##Test update broadcast space##"
    if not tm.test_update_broadcast_space():
        print "Test update broadcast space\t[FAIL]"
        nbFail+=1
    else: print "Test update broadcast space\t[OK]"
    
    # tests get broadcast spaces
    nbTest+=1
    print "\n##Test get broadcast space##"
    if not tm.test_get_broadcast_spaces():
        print "Test get broadcast spaces\t[FAIL]"
        nbFail+=1
    else: print "Test get broadcast spaces\t[OK]"
    
    # tests intersect
    nbTest+=1
    print "\n##Test intersect##"
    if not tm.test_intersect():
        print "Test intersect\t[FAIL]"
        nbFail+=1
    else: print "Test intersect\t[OK]"
    
    # tests getpath
    nbTest+=1
    print "\n##Test get_paths##"
    if not tm.test_get_paths():
        print "Test get_paths\t[FAIL]"
        nbFail+=1
    else: print "Test get_paths\t[OK]"
    
    print "\nResults: %d%% success !" % ((nbTest - nbFail)/ nbTest *100.0)

