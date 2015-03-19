__author__ = 'aymen'
from oslo.config import cfg
from neutron.plugins.map import models
from neutron.openstack.common import importutils
from neutron.plugins.map.cli_driver import ios_parser_translator
from neutron.openstack.common import log
from neutron.plugins.map import map_utils
LOG = log.getLogger(__name__)



class DriverManager():

    def __init__(self, resources):
        self.resources = resources
        self.initialize()
        pass

    def initialize(self):
        self.ordered_driver = []
        for driver_class in cfg.CONF.map.drivers:
            LOG.error(_("Les drivers sont %s"), driver_class)
            driver = importutils.import_object(driver_class, self.resources )
            self.ordered_driver.append(driver)


    def configure_equipments(self, nodes):
        LOG.error(_("Les drivers sont %s"), self.ordered_driver)
        for node, configuration in nodes.iteritems():
            node_configured = False
            for driver in self.ordered_driver:
                LOG.info(_("Driver %(driver)s is used to configure %(name)s"),
                {"driver": driver.name,
                 "name": node.name})
                if driver.configure_equipment(node, configuration):
                    break
            else:
                raise map_utils.NoDriverException(_("No driver can "
                                             + "communicate with device ") + _(node.name))



        pass