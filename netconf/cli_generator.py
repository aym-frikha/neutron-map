# Dependancy: pyparsing
import sys
from pyparsing import *
from xml.etree import ElementTree as ET

from oslo.config import cfg
from neutron.plugins.map import resources


WORD = 'word'
LINE = 'line'
OPTION = 'opt'
SHADOW = 'shadow'
KEYWORD = 'keyword'
CHOICE = 'oneOf'
OR = 'or'
EXPRESSION = 'expr'
VARIABLE = 'var'

class cliGenerator(object):

    def __init__(self):
        self.node_manager = resources.DbManager()
        self.ios_ref = self.node_manager.get_IOSReference()


    def command_from_tree(self, config_tree):
        commands = []
        for node in config_tree.Node:
            commands += self.generate_commands(node)
        return commands

    def generate_commands(self, node):
        commands = []
        # Implicit function to print 'None' element as empty strings
        xstr = lambda s: s or ""
        #for node in config_tree.Node:
        node_name = node.name
        negate = False
        for command in self.ios_ref.CommandList.Command:
            if node_name == command.name or (
                     node_name[:3] == "no " and node_name[3:] == command.name):
                if node_name[:3] == "no " and node_name[3:] == command.name:
                    negate = True
                    node_name == node.name[3:]
                name_parts = node_name.split(' ')
                node_data = [xstr(node.Value)]
                if node.Children:
                    for param in node.Parameters:
                        if not param.shadow:
                            node_data.append(param.Name)
                        node_data.append(xstr(node.Value))
                cmd_syntax = command.Syntax[0].value()
                if negate:
                    cmd_syntax = "no " + cmd_syntax
                line = self.parse_command(cmd_syntax)
                cmd_line = []
                def treat_element(should):
                    if (should.tag == WORD
                            or should.tag == KEYWORD
                            or should.tag == LINE) :
                        if len(name_parts) > 0:
                                found = name_parts.pop(0)
                        else:
                            LOG.info(_("Error in While generating conf"))
                            return False
                        if found != should.text:
                            # False since 'switchport' was added to the IOS
                            # return False
                            cmd_line.append(should.text)
                            name_parts.insert(0, found)
                        else:
                            cmd_line.append(found)
                    elif should.tag == VARIABLE:
                        if len(node_data) > 0:
                            cmd_line.append(node_data.pop(0))
                            return True
                        else:
                            return False
                    elif should.tag == OR:
                        for expr in should:
                            if expr.tag != EXPR:
                                return False
                            else:
                                for word in expr:
                                    if not treat_element(word):
                                        break
                                else:
                                    break
                        else:
                            return False
                for line_element in line:
                    treat_element(line_element)
                commands.append(' '.join(cmd_line))
                if node.Children:
                    for children in node.Children.Node:
                        sub_commands = self.generate_commands(children)
                        if sub_commands == False:
                            return False
                        elif sub_commands:
                            commands += sub_commands
                    commands.append('exit')
                return commands
                    #commands += child_command

                        
                    
            elif not node.known:
                commands.append(node.name)
                return commands

    def parse_command(self, command):
        expr = Forward()
        nestedParens = nestedExpr('(', ')', content=expr).setResultsName('par')
        nestedBrackets = nestedExpr('[', ']',
                                           content=expr).setResultsName(OPTION)
        nestedCurlies = nestedExpr('{', '}',
                                           content=expr).setResultsName(CHOICE)
        nonBracePrintables = ''.join(
                              c for c in printables if c not in '(){}[] |,$#%')
        variable = Combine(Literal('$') + Word(nonBracePrintables)
                        ).setResultsName(VARIABLE)
        # This case is a serious problem in validMaker. I don't know what it is
        ghost = Combine(Literal('#').suppress()
                      + Word(nonBracePrintables)).setResultsName(SHADOW)
        keyword = Combine(Literal('%').suppress()
                        + Word(nonBracePrintables)).setResultsName(KEYWORD)

        enclosed = (nestedParens | nestedBrackets | nestedCurlies)
        word = (Word(nonBracePrintables).setResultsName(WORD) | enclosed |
                                                    variable | ghost | keyword)
        expr << (Group(word).setResultsName(EXPRESSION)
                 | Group(Group(OneOrMore(word)).setResultsName(EXPRESSION)
                     + OneOrMore(Literal('|').suppress()
                            + Group(OneOrMore(word)).setResultsName(EXPRESSION)
                     )).setResultsName(OR))
        rule = OneOrMore(word).setResultsName(LINE)

        result = rule.parseString(command)
        return ET.fromstring(result.asXML())

    def command_for_device(self, device_name, device_object):
        return self.command_from_tree(device_object.ConfigTree)




if __name__ == '__main__':

    sys.path.append('..')
    from neutron.plugins.map.fake_environment import _
    from neutron.plugins.map.fake_environment import log
    LOG = log()
    cfg.CONF(args=['--config-file', 'example_conf.ini'], project='neutron',
                                                                   version='1')
    cli_gen = cliGenerator()
    node_manager = resources.DbManager()
    R1 = node_manager.get_device_by_name('R1')
    print cli_gen.command_from_tree(R1.ConfigTree)
