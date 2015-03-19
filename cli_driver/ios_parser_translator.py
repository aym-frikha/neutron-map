__author__ = 'aymen'

from enum import Enum

# # IF IN NEUTRON
from neutron.openstack.common import log as logging
from neutron.plugins.map import resources

LOG = logging.getLogger(__name__)

from oslo.config import cfg
import os.path


class IOSCommandSyntax():
    def __init__(self):
        self.negated = True
        self.version = None
        self.syntax = None


class IOSCommandType(Enum):
    MODE = 'mode'
    SUBMODE = 'submode'
    COMMAND = 'command'


class IOSCommand():
    def __init__(self):
        self.name = None
        self.type = IOSCommandType
        self.mode = None
        self.parent = None

        self.syntax_list = []
        self.children = []
        self.default_syntax = IOSCommandSyntax()
        self.syntax_list.append(self.default_syntax)


class IOSTranslator(object):
    def __init__(self, resources_manager):
        # iosReference
        self.ressources = resources_manager
        self.iosReference = resources_manager.get_conf_references('IOS')


    def translate_metacli_to_cli(self, device):
        self.configuration = ""
        for node in device.ConfigTree.Node:
            self.translate_metacli_line(node, 0)


    def translate_metacli_line(self, node, level):

        command = None  # IOS Command
        for cmd in self.iosReference.CommandList.Command:
            if node.name == cmd.name:
                command = cmd
                break
        if command == None:
            if node.name.startswith('no '):
                # nameParts = node.name.split(" ")
                for cmd in self.iosReference.CommandList.Command:
                    if node.name[3:] == cmd.name:
                        command = cmd
                        break
        if command == None:
            if not node.known:
                outline = ""
                for i in range(0, level + 1):
                    outline += "  "
                    self.configuration += '\n' + outline + node.name
            else:
                LOG.error(_('No command matches node name %s'), node.name)
            return
        indent = 0
        if command.type == 'mode' or command.mode == 'global':
            level = 0
            indent = 0
        elif command.type == 'submode':
            level = 1
            indent = 1
        else:
            indent = level + 1  # Simple command, so indent according to the current level

        cli_line = ""

        for i in range(0, indent):
            cli_line += "  "

        ret_line = self.translate_command(node, command)

        if ret_line != None:
            cli_line += ret_line
            self.configuration += '\n' + cli_line
        else:
            LOG.error(_("Cannot translate node %(name)s, name does not match "
                        "syntax for command %(command)s "), {'name': node.name,
                                                             'command': command.name})
            return
        if node.Children:
            for child in node.Children.Node:
                self.translate_metacli_line(child, level)


    def translate_command(self, node, command):
        retline = ""
        buffer = ""
        is_keyword = True
        is_dynamic = False
        is_optional = False
        option_found = False
        is_choice = False
        choice_found = False

        parameters_found = False
        name_parts = node.name.split(' ')
        value_parts = []
        node_value = ''
        if node.Value != None:
            node_value = node.Value

        if node.Parameters:
            for param in node.Parameters.Node:
                # if not node.parameter:
                # continue
                param_value = None
                if param.Value == None:
                    param_value = ""
                else:
                    param_value = param.Value

                if param.shadow:
                    node_value += (" " + param_value)
                else:
                    node_value += (" " + param.name + " " + param_value)

        value_parts = node_value.split(' ')
        comIdx = 0
        nameIdx = 0
        valIdx = 0
        cmd_syntax = command.Syntax[0].value()
        command_syntax = None
        if name_parts[0] == 'no' and command.negated:
            command_syntax = 'no ' + cmd_syntax
        else:
            command_syntax = cmd_syntax
        while comIdx <= len(command_syntax):
            curChar = '\0'
            if comIdx < len(command_syntax):
                curChar = command_syntax[comIdx]
            if curChar == ' ' or curChar == '|' or comIdx == len(
                    command_syntax):
                if (not (is_optional and option_found) and not (
                            is_choice and choice_found) and len(buffer) != 0):
                    if is_keyword:
                        if nameIdx < len(name_parts):
                            if buffer == name_parts[nameIdx]:
                                if len(retline) != 0:
                                    retline += " "
                                retline += name_parts[nameIdx]
                                nameIdx += 1
                                if is_choice:
                                    choice_found = True
                                if is_optional:
                                    option_found = True
                            else:
                                LOG.error(_(
                                    'Expected Keyword %(buffer)s but found %(name)s'),
                                          {'buffer': buffer,
                                           'name': name_parts[nameIdx]})
                        elif not is_optional:
                            LOG.error(_(
                                'No more keywords available in node name %(name)s'),
                                      {'name': node.name})
                    else:
                        if node_value != "":
                            if valIdx < len(value_parts):
                                if is_dynamic or buffer == value_parts[valIdx]:
                                    if len(retline) != 0:
                                        retline += " "
                                    retline += value_parts[valIdx]
                                    valIdx += 1
                                    if is_choice:
                                        choice_found = True
                                    if is_optional:
                                        option_found = True
                                elif not is_choice and not is_optional:
                                    LOG.error(_(
                                        'Expected keyword %(buffer)s but found %(name)s'),
                                              {'name': value_parts[valIdx],
                                               'buffer': buffer})
                            elif not is_optional:
                                LOG.error(_(
                                    'No more keywords available in node value %(name)s'),
                                          {'name': node_value})
                is_dynamic = False
                buffer = ""
            elif curChar == '$':
                is_keyword = False
                is_dynamic = True
                buffer = ""
            elif curChar == '{':
                is_choice = True
                choice_found = False
                is_dynamic = False
                buffer = ""
            elif curChar == '}':
                if not choice_found:
                    LOG.error(_("Missing choice element for node %s"),
                              node.name)
                    return None
                is_choice = False
                choice_found = False
                is_keyword = True
                is_dynamic = False
                buffer = ""
            elif curChar == '[':
                is_optional = True
                option_found = False
                is_dynamic = False
                buffer = ""
            else:
                if len(buffer) == 0 and nameIdx == len(name_parts):
                    is_keyword = False
                buffer += str(curChar)
            # TODO: many HACKS
            if nameIdx == len(name_parts):
                for val in range(valIdx, len(value_parts)):
                    if len(retline) != 0:
                        retline += " "
                    retline += value_parts[val]
                break
            comIdx += 1

        return retline