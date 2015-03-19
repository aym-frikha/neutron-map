__author__ = 'aymen'

import unittest

from neutron.plugins.map import nodemanager
from ressources import ResourceManager
from oslo.config import cfg

# from fake_environment import _
# from fake_environment import log
#
# LOG = log()

class TestResourceManager(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        cfg.CONF(args=['--config-file', '../install/map_conf.ini'], project='neutron', version='1')
        self.resources = ResourceManager()
        self.node_manager = NodeManager()

    def test_deploy_service(self):
        if len(self.resources.instance_service_files) != 0 and len(self.resources.network_files) != 0:
            instance_service_name = self.resources.instance_service_files[0].split('.')[0]
            device_name = self.resources.network_files[0].split('.')[0]
            inst_service = self.resources.get_inst_service(instance_service_name)
            device = self.resources.get_device_config(device_name)
            print("deploy service ", instance_service_name, " on device ", device_name)
            device = nodemanager.deploy_service(device, inst_service)
            service_deployed = nodemanager.discover_service(device, inst_service)
            self.assertTrue(service_deployed)
            # print(device.toDOM().toprettyxml())

    def test_service_non_present_on_device(self):
        if len(self.resources.instance_service_files) != 0 and len(self.resources.network_files) != 0:
            instance_service_name = self.resources.instance_service_files[0].split('.')[0]
            device_name = self.resources.network_files[0].split('.')[0]
            inst_service = self.resources.get_inst_service(instance_service_name)
            device = self.resources.get_device_config(device_name)
            # print("deploy service ", instance_service_name, " on device ", device_name)
            # device = self.node_manager.deploy_service(device, inst_service)
            service_deployed = nodemanager.discover_service(device, inst_service)
            self.assertFalse(service_deployed)
            # print(device.toDOM().toprettyxml())

    def test_remove_service_from_device(self):
        if len(self.resources.instance_service_files) != 0 and len(self.resources.network_files) != 0:
            instance_service_name = self.resources.instance_service_files[0].split('.')[0]
            device_name = self.resources.network_files[0].split('.')[0]
            inst_service = self.resources.get_inst_service(instance_service_name)
            device = self.resources.get_device_config(device_name)
            print("deploy service ", instance_service_name, " on device ", device_name)
            device = nodemanager.deploy_service(device, inst_service)
            #print(device.toDOM().toprettyxml())
            service_deployed = nodemanager.discover_service(device, inst_service)
            self.assertTrue(service_deployed)
            device = nodemanager.remove_service(device, instance_service_name)
            #print(device.toDOM().toprettyxml())
            service_deployed = nodemanager.discover_service(device, inst_service)
            self.assertFalse(service_deployed)

    def test_deploy_two_services(self):
        if len(self.resources.instance_service_files) > 1 and len(self.resources.network_files) != 0:
            instance_service_name1 = self.resources.instance_service_files[0].split('.')[0]
            instance_service_name2 = self.resources.instance_service_files[1].split('.')[0]
            device_name = self.resources.network_files[0].split('.')[0]
            inst_service1 = self.resources.get_inst_service(instance_service_name1)
            inst_service2 = self.resources.get_inst_service(instance_service_name2)
            device = self.resources.get_device_config(device_name)
            print("deploy service ", instance_service_name1, " on device ", device_name)
            device = nodemanager.deploy_service(device, inst_service1)
            print("deploy service ", instance_service_name2, " on device ", device_name)
            device = nodemanager.deploy_service(device, inst_service2)
            print("verify deployment of service ", instance_service_name1, " on device ", device_name)
            service_deployed = nodemanager.discover_service(device, inst_service1)
            self.assertTrue(service_deployed)
            print("verify deployment of service ", instance_service_name2, " on device ", device_name)
            service_deployed = nodemanager.discover_service(device, inst_service2)
            self.assertTrue(service_deployed)

    def test_remove_one_service_from_two(self):
        if len(self.resources.instance_service_files) > 1 and len(self.resources.network_files) != 0:
            instance_service_name1 = self.resources.instance_service_files[0].split('.')[0]
            instance_service_name2 = self.resources.instance_service_files[1].split('.')[0]
            device_name = self.resources.network_files[0].split('.')[0]
            inst_service1 = self.resources.get_inst_service(instance_service_name1)
            inst_service2 = self.resources.get_inst_service(instance_service_name2)
            device = self.resources.get_device_config(device_name)

            print("deploy service ", instance_service_name1, " on device ", device_name)
            device = nodemanager.deploy_service(device, inst_service1)

            print("deploy service ", instance_service_name2, " on device ", device_name)
            device = nodemanager.deploy_service(device, inst_service2)

            print("verify deployment of service ", instance_service_name1, " on device ", device_name)
            service_deployed = nodemanager.discover_service(device, inst_service1)
            self.assertTrue(service_deployed)

            print("verify deployment of service ", instance_service_name2, " on device ", device_name)
            service_deployed = nodemanager.discover_service(device, inst_service2)
            self.assertTrue(service_deployed)

            print("remove service ", instance_service_name2, " from device ", device_name)
            device = nodemanager.remove_service(device, instance_service_name2)

            print("verify deployment of service ", instance_service_name1, " on device ", device_name)
            service_deployed = nodemanager.discover_service(device, inst_service1)
            self.assertTrue(service_deployed)
            print("verify removal of service ", instance_service_name2, " on device ", device_name)
            service_deployed = nodemanager.discover_service(device, inst_service2)
            self.assertFalse(service_deployed)


