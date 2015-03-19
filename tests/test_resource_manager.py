__author__ = 'aymen'

import unittest

from neutron.plugins.map.resources import ResourceManager
from oslo.config import cfg

# from fake_environment import _
# from fake_environment import log
#
# LOG = log()

class TestResourceManager(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        cfg.CONF(args=['--config-file', '../install/map_conf.ini'], project='neutron', version='1')
        self.name_test = 'toto'
        self.manager = ResourceManager()

    def test_get_all_devices_config(self):
        nbr_devices = len(self.manager.network_files)
        list_devices = self.manager.get_all_device_config()
        self.assertEqual(nbr_devices, len(list_devices))

    def test_get_device_config(self):
        dev = self.manager.get_device_config(self.manager.network_files[0].split('.')[0])
        self.assertIsNotNone(dev)

    def test_set_device_conf(self):
        dev = self.manager.get_device_config(self.manager.network_files[0].split('.')[0])
        dev.name = self.name_test
        self.manager.set_device_config(dev)
        self.assertTrue(self.manager.device_known(self.name_test))

    def test_get_all_gen_services(self):
        if (len(self.manager.service_files) != 0):
            nbr_services = len(self.manager.service_files)
            list_services = self.manager.get_all_gen_services()
            self.assertEqual(nbr_services, len(list_services))

    def test_get_gen_service(self):
        if (len(self.manager.service_files) != 0):
            service = self.manager.get_gen_service(self.manager.service_files[0].split('.')[0])
            self.assertIsNotNone(service)

    def test_set_gen_service(self):
        service = self.manager.get_gen_service(self.manager.service_files[0].split('.')[0])
        service.name = self.name_test
        self.manager.set_gen_service(service)
        self.assertTrue(self.manager.gen_service_known(self.name_test))


    def test_get_all_inst_services(self):
        nbr_inst_services = len(self.manager.instance_service_files)
        list_inst_services = self.manager.get_all_inst_services()
        nbr_total_extracted = 0
        for inst_services in list_inst_services.values():
            nbr_total_extracted = nbr_total_extracted + len(inst_services)
        self.assertEqual(nbr_inst_services, nbr_total_extracted)

    def test_get_all_inst_services_with_type(self):
        service_type = self.manager.get_inst_service(self.
            manager.instance_service_files[0].split('.')[0]).InstanceOf.href
        list_inst_services = self.manager.get_all_inst_services(service_type)
        if service_type is not None:
            self.assertIsNotNone(list_inst_services)
        else:
            self.assertIsNone(list_inst_services)

    def test_set_inst_service(self):
        inst_service = self.manager.get_inst_service(self.manager.instance_service_files[0].split('.')[0])
        inst_service.name = self.name_test
        self.manager.set_inst_service(inst_service)
        self.assertTrue(self.manager.inst_service_known(self.name_test))

    def test_get_rule(self):
        if len(self.manager.rule_files) != 0:
            rule = self.manager.get_rule(self.manager.rule_files[0].split('.')[0])
            self.assertIsNotNone(rule)

    def test_get_all_rules(self):
        nbr_rules = len(self.manager.rule_files)
        list_rules = self.manager.get_all_rules()
        self.assertEqual(nbr_rules, len(list_rules))

    def test_set_rule(self):
        rule = self.manager.get_rule(self.manager.rule_files[0].split('.')[0])
        rule.name = self.name_test
        self.manager.set_rule(rule)
        self.assertTrue(self.manager.rule_known(self.name_test))

    def test_get_conf_references(self):
        if len(self.manager.os_ref_files) != 0:
            os_ref = self.manager.get_conf_references(self.manager.os_ref_files[0].split('.')[0])
            self.assertIsNotNone(os_ref)

    def test_get_all_conf_references(self):
        nbr_os_ref = len(self.manager.os_ref_files)
        list_os_ref = self.manager.get_all_conf_references()
        self.assertEqual(nbr_os_ref, len(list_os_ref))

    def test_set_conf_references(self):
        os_ref = self.manager.get_conf_references(self.manager.os_ref_files[0].split('.')[0])
        os_ref.name = self.name_test
        self.manager.set_conf_references(os_ref)
        self.assertTrue(self.manager.conf_reference_known(self.name_test))


    @classmethod
    def tearDownClass(self):
        manager = ResourceManager()
        if 'toto.xml' in manager.network_files:
            manager.delete_device_config('toto')
        if 'toto.xml' in manager.service_files:
            manager.delete_gen_service('toto')
        if 'toto.xml' in manager.instance_service_files:
            manager.delete_inst_service('toto')
        if 'toto.xml' in manager.rule_files:
            manager.delete_rule('toto')
        if 'toto.xml' in manager.os_ref_files:
            manager.delete_conf_reference('toto')









