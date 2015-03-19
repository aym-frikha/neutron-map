#!/usr/bin/env python
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# @author: Clement Parisot, netvirt
# domainkeeper.py
# 24.07.2013

# # IF IN NEUTRON
from neutron.openstack.common import log as logging
from neutron.plugins.map import resources

LOG = logging.getLogger(__name__)

from oslo.config import cfg
import os.path



class IOSParser(object):
    def __init__(self, resources_manager):
        # Declare device structure
        self.device = resources.Device.Device()
        self.device.Description = ""
        self.device.Properties = resources.Device.CTD_ANON_()
        self.device.Properties.IOSVersion = ""
        self.device.Properties.EquipmentType = ""
        self.device.Services = resources.Device.CTD_ANON_2()
        #self.device.IPAddress = '192.168.1.1' #not used
        self.device.ConfigTree = resources.Device.CTD_ANON_4()
        self.device.name = ''

        #current command to parse
        self.m_Command = None

        #Nodes used for the construction
        self.new_node = None
        self.new_node2 = resources.Device.DevNode()
        self.ret_node = resources.Device.DevNode()

        #iosReference
        self.ressources = resources_manager
        self.iosReference = resources_manager.get_IOSReference()

    def retrieve_config_file(self, filePath, name):
        LOG.info(_("Retrieve %s configuration."), self.device.name)
        LOG.info(_("Retrieving configuration at %s..."), filePath)
        if os.path.exists(filePath) and os.isfile(filePath):
            try:
                fileDescriptor = open(filePath, 'r')
                device_conf = fileDescriptor.read()
                self.parse_cli_configuration(device_conf, name)
            except IOError as ioe:
                LOG.error(_("couldn't retrieve configuration %s"), filepath)
                LOG.error(_("%r"), ioe)
                return
        else:
            LOG.error(_("Cannot open file %s for reading!"), filePath)
            return
        LOG.info(_("Successfully retrieved configuration"))

    def parse_cli_configuration(self, device_conf, device_id):
        self.device.name = device_id
        if device_conf == None or device_conf == "":
            return
        cli_line = ""
        counter = 0
        self.m_Mode = resources.Device.DevNode()
        self.m_SubMode = resources.Device.DevNode()
        #parse each line
        for cli_line in device_conf.split('\n'):
            counter += 1
            #if line exists
            if cli_line != None and len(cli_line) != 0:
                self.m_Command = None
                #parse line in a new node
                self.new_node = self.parse_cli_line(cli_line, counter)

                if self.new_node != None:
                    #if commande is global or mode
                    if self.m_Command != None and (
                                                self.m_Command.mode == 'global'
                                             or self.m_Command.type == 'mode'):
                        #add node to the device
                        self.add_node(self.new_node)
                        self.m_SubMode = None
                    elif self.m_SubMode != None:
                        #if command is submode
                        if (    self.m_Command != None
                            and self.m_Command.type == 'submode'):
                            #add command as the children of mode command
                            self.__add_node__(self.new_node, self.m_Mode)
                        #add to submode
                        else:
                            self.__add_node__(self.new_node, self.m_SubMode)
                    #add to the mode
                    elif(self.m_Mode != None):
                        self.__add_node__(self.new_node, self.m_Mode)
                    elif(self.m_Command == None): # Unparseable line
                        self.add_node(self.new_node)
                    #else Error

                    if(self.m_Command != None):
                        if(self.m_Command.type == 'mode'):
                            #copy new_node to mode node
                            self.m_Mode = self.clone_node(self.m_Mode,
                                                          self.new_node)
                        elif(self.m_Command.type == 'submode'):
                            #copy new node to sub mode
                            self.m_SubMode = self.clone_node(self.m_SubMode,
                                                             self.new_node)
                else:
                    # TODO: set mode to a more appropriate value, 
                    # to add node as son of 'Config tree'.
                    self.m_Mode = None

    def parse_cli_line(self, cli_line, line_number):
        # Strip leading and trailing spaces and tabs
        cli_line = cli_line.strip()

        if(len(cli_line) == 0 or cli_line[0] == '!'): # Empty or comment line
            return None

        line_parts = cli_line.split()
        if(len(line_parts) == 0):
            LOG.error("Unparsable content, line %d'%d" ,line_number, cli_line)
            return self.add_unparsable_line(cli_line)

        self.ret_node = resources.Device.DevNode()
        for self.m_Command in self.iosReference.CommandList.Command:
            name_parts = self.m_Command.name.split(' ')
            cmdSyntax = self.m_Command.Syntax[0]
            check_part = None
            if line_parts[0] == "no" and self.m_Command.negated:
                check_part = line_parts[1]
            else:
                check_part = line_parts[0]
            if name_parts[0] != check_part: # Doesn't match this command
                continue

            found = False
            for name_part in name_parts:
                found = False
                for line_part in line_parts:
                    if name_part == line_part:
                        found = True
                        break

                if not found: # Doesn't match this command
                    break
            if found:
                self.ret_node = self.parse_command(self.m_Command, line_parts,
                                                  line_number)
                if self.ret_node == None or self.ret_node.name == "":
                    return self.add_unparsable_line(cli_line)
                else:
                    return self.ret_node

        LOG.error("No command matched for line %d %s", line_number, cli_line)
        return self.add_unparsable_line(cli_line)

    def add_unparsable_line(self, cli_line):
        the_node = resources.Device.DevNode()
        the_node.name = cli_line
        the_node.known = False
        return the_node

    def parse_command(self, command, line_parts, line_number):
        root_node = resources.Device.DevNode()
        root_node.name = ""
        cur_node = root_node

        pars_buffer = ""
        lineDone = False

        isKeyword = True

        isOptional = False
        optionFound = False

        isChoice = False
        choiceFound = False

        comIdx = 0
        lineIdx = 0

        cmdSyntax = self.m_Command.Syntax[0]
        if line_parts[0] == "no" and self.m_Command.negated:
            self.m_CommandName = "no " + self.m_Command.name
            self.m_CommandSyntax = "no " + cmdSyntax.value()
        else:
            self.m_CommandName = self.m_Command.name
            self.m_CommandSyntax = cmdSyntax.value()

        #TODO: eventually recode this part using pyparsing
        while comIdx <= len(self.m_CommandSyntax):
            if lineIdx >= len(line_parts) or line_parts[lineIdx][0] == '!':
                lineDone = True

            curChar = '\0'
            if comIdx < len(self.m_CommandSyntax):
                curChar = self.m_CommandSyntax[comIdx]

            if curChar == ' ' or curChar == '|' or comIdx == len(self.m_CommandSyntax):
                if len(pars_buffer) != 0 and not choiceFound:
                    if not isOptional and lineDone:
                        LOG.error("Missing Command elements on line %d", line_number)
                        return None
                    found = True
                    if lineIdx < len(line_parts):
                        if isKeyword:
                            if cur_node.shadow:
                                cur_node.name += pars_buffer
                                found = True
                                isKeyword = False
                            elif pars_buffer == line_parts[lineIdx]:
                                if len(cur_node.name) != 0:
                                    cur_node.name += " "
                                cur_node.name += line_parts[lineIdx]
                                lineIdx += 1
                                found = True
                        else:
                            if cur_node.Value == None:
                                cur_node.Value = str()
                            if cur_node.Value != None and len(cur_node.Value) != 0:
                                cur_node.Value += " "
                            cur_node.Value += line_parts[lineIdx]
                            lineIdx += 1
                            found = True
                    if found:
                        if isChoice:
                            choiceFound = True
                        if isOptional:
                            optionFound = True
                pars_buffer = ""
            elif curChar == '$':
                isKeyword = False
                pars_buffer = ""
            elif curChar == '{':
                if isChoice:
                    LOG.error("Nested choice element on line %d", line_number)
                    return None
                isChoice = True
                choiceFound = False
                pars_buffer = ""
            elif curChar == '}':
                if not choiceFound:
                    LOG.error("Missing choice element on line %d", line_number)
                    return None
                isChoice = False
                choiceFound = False
                isKeyword = True
                pars_buffer = ""
            elif curChar == '[':
                if isOptional:
                    LOG.error("Nested optional element on line %d", line_number)
                    return None
                isOptional = True
                optionFound = False
                pars_buffer = ""
            elif curChar == ']':
                isOptional = False
                optionFound = False
                isKeyword = True
                pars_buffer = ""
            elif curChar == '%' or curChar == '#':
                if cur_node != root_node and cur_node.name != "":
                    # Add previous node
                    self.__add_parameter__(root_node, cur_node)
                cur_node = resources.Device.DevNode()
                cur_node.name = ""
                isKeyword = True
                pars_buffer = ""

                if curChar == '#':
                    cur_node.shadow = True
            else:
                # Node complete
                if len(pars_buffer) == 0 and cur_node.name == self.m_CommandName:
                    isKeyword = False
                pars_buffer += str(curChar)
            comIdx+=1

        if cur_node != root_node and cur_node.name != "":
            self.__add_parameter__(root_node, cur_node)
        return root_node

    def __add_parameter__(self, node1, node2):
        node2.parameter = True
        self.add_child(node1, node2)

    def __add_node__(self, node, parent):
        if parent == None:
            self.add_node(node)
        else:
            node.fragment = False
            self.add_child(parent, node)
        return

    def add_node(self, node):
        node.fragment = True
        self.new_node2 = resources.Device.DevNode()
        if not self.device.ConfigTree == None:
            self.device.ConfigTree.append(self.clone_node(self.new_node2, node))
        else:
            self.device.ConfigTree = resources.Device.CTD_ANON_4()
            self.device.ConfigTree.append(self.clone_node(self.new_node2, node))

    def add_child(self, parent, node):
        node.Parent = parent
        self.new_node2 = resources.Device.DevNode()
        if not parent.Children == None:
            parent.Children.append(self.clone_node(self.new_node2, node))
        else:
            parent.Children = resources.Device.CTD_ANON_10()
            parent.Children.append(self.clone_node(self.new_node2, node))

    def translate_cli_configuration(self, cli_file):
        if cli_file == None or cli_file == "":
            return
        LOG.info("Writing %s...", cli_file)
        try:
            file_writer = open(cli_file, 'w') #new StreamWriter
            if file_writer == None:
                LOG.error("Cannot open file %s for writing!", cli_file)
                return
            file_writer.write(self.device.toDOM().toprettyxml())
            file_writer.close()
        except IOError as ioe:
            LOG.error(("Unable to write device %s configuration in file %s"),
                      self.device.name, cli_file)
            LOG.error(("%r"), ioe)

    def clone_node(self, device_node, service_node):
        return service_node
        device_node.name = service_node.name
        device_node._CimRef = service_node.CimRef
        device_node.known = service_node.known
        device_node.parameter =service_node.parameter
        device_node.uid= service_node.uid
        device_node.cardinality = service_node.cardinality
        device_node.shadow = service_node.shadow
        if service_node.BaseParent:
            device_node.BaseParent = resources.Device.CTD_ANON_5()
            device_node.BaseParent.href = service_node.BaseParent.href
        device_node.Value = service_node.Value
        if service_node.Children:
            device_node.Children = resources.Device.CTD_ANON_10()
            for node in service_node.Children.Node:
                    new_node = resources.Device.DevNode()
                    self.clone_node(new_node, node)
                    device_node.Children.append(new_node)
        return device_node

if __name__ == '__main__':
    cfg.CONF(args=['--config-file', 'install/map_conf.ini'],
             project='neutron', version='1')                                    
    ios = IOSParser()                                                           
    #ios.retrieve_config('./CLIDirectory/Pauillac.txt', 'Pauillac')             
    #ios.translate_cli_configuration(self, './CLIDirectory/Pauillac.xml')       
    file = open('conf_example/conf_cisco')                                      
    device_conf = file.read()                                         
    ios.parse_cli_configuration(device_conf, 'R1')                              
    device = ios.device
    print device.toDOM().toprettyxml()
