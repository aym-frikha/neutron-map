__author__ = 'aymen'
from neutron.plugins.map import models
from neutron.plugins.map.cli_driver import ios_parser_translator
from neutron.plugins.map.cli_driver import ssh_driver
from neutron.openstack.common import log

LOG = log.getLogger(__name__)


class CliDriver():
    def __init__(self, resources):
        self.name = 'cli_driver'
        self.translator = ios_parser_translator.IOSTranslator(resources)
        self.telnet = ssh_driver
        pass

    def configure_equipment(self, node, configuration):
        if type(node) == models.PhysicalNode:
            self.translator.translate_metacli_to_cli(configuration)
            LOG.error(_('la configuration cli_driver de %s est  %s'), node.name,
                      self.translator.configuration)
            ssh_driver.put_configuration(node.name, node.address, node.login,
                                         node.password,
                                         self.translator.configuration)

            pass
        return True
        pass