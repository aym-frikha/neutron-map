#!/usr/bin/env python
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# @author: Aymen Frikha, netvirt
# Ressources.py
# 23.07.2013

# # IF IN NEUTRON
from neutron.openstack.common import log as logging
LOG = logging.getLogger(__name__)
# Else
# from neutron.plugins.map.fake_environment import _
# from neutron.plugins.map.fake_environment import log
#
# LOG = log()
import re
import os

from neutron.plugins.map.DB_Structures import GenericService, Rule, Device, \
    ServiceInstance, OSreference
from config import cfg
from neutron.plugins.map.map_utils import NoDeviceReprException, \
    NoOSRefReprException, NoRuleReprException, NoServiceInstanceReprException, \
    NoServiceReprException, TopologyLoadingException

class ResourceManager(object):
    def __init__(self):
        self.network_path = cfg.CONF.map.network_path
        self.service_path = cfg.CONF.map.service_path
        self.instance_service_path = cfg.CONF.map.network_service_path
        self.rules_path = cfg.CONF.map.service_rules_path
        self.os_ref_path = cfg.CONF.map.os_references
        self.scenario_file = cfg.CONF.map.scenar_file
        self._update_files()

    def _update_files(self):
        self.network_files = [file for file in os.listdir(self.network_path) if
                              not file.endswith('~')]
        self.service_files = [file for file in os.listdir(self.service_path) if
                              not file.endswith('~')]
        self.instance_service_files = [file for file in
                                       os.listdir(self.instance_service_path) if
                                       not file.endswith('~')]
        self.rule_files = [file for file in os.listdir(self.rules_path) if
                           not file.endswith('~')]
        self.os_ref_files = [file for file in os.listdir(self.os_ref_path) if
                             not file.endswith('~')]

    '''  Manage device configurations:
     ' get_all_device_config(): List[device_config]
     ' get_device_config(device_name): device_config
     ' set_device_config(device_config): None
     ' delete_device_config(device_name): None
    '''

    def get_device_config(self, device_name):
        try:
            xml = open(os.path.join(self.network_path, device_name + '.xml')).read()
            device = Device.CreateFromDocument(xml)
            return device
        except IOError as e:
            print(e)
            LOG.error(_("Problem during the loading of '%s'"),
                      device_name + '.xml')
            raise NoDeviceReprException(device_name)

    def get_all_device_config(self):
        """

        :param self:
        :return: devices: List[device_config]
        """
        self._update_files()
        devices = []
        for device_name_xml in self.network_files:
            devices.append(
                self.get_device_config(device_name_xml.split('.')[0]))
        return devices

    def device_known(self, device_name):
        self._update_files()
        return device_name + '.xml' in self.network_files

    def set_device_config(self, device):
        cli_file = self.network_path + device.name + '.xml'
        try:
            file_writer = open(cli_file, 'w')  # new StreamWriter
            if file_writer is None:
                LOG.error("Cannot open file %s for writing!", cli_file)
                return
            print(device.toDOM().toprettyxml())
            file_writer.write(device.toDOM().toprettyxml())
            file_writer.close()
        except IOError as ioe:
            LOG.error(("Unable to write device %s configuration in file %s"),
                      device.name, cli_file)
            LOG.error(("%r"), ioe)

    def delete_device_config(self, device_name):
        self._update_files()
        try:
            os.remove(self.network_path + device_name + '.xml')
        except OSError as ose:
            LOG.error("Unable to remove device %s configuration",
                      device_name)
            LOG.error("%r", ose)

    '''  Manage generic services:\n'
     '     get_all_gen_services(): List[gen_service]\n'
     '     get_gen_service(gen_service_name): gen_service\n'
     '     set_gen_service(gen_service): None\n '
     '     delete_gen_service(gen_service_name)
    '''

    def get_gen_service(self, gen_service_name):
        try:
            xml = open(os.path.join(self.service_path, gen_service_name + '.xml')).read()
            service = GenericService.CreateFromDocument(xml)
            return service
        except IOError as e:
            print(e)
            LOG.error(_("Problem during the loading of '%s'"),
                      gen_service_name + '.xml')
            raise NoServiceReprException(gen_service_name)

    def get_all_gen_services(self):
        self._update_files()
        services = []
        for service in self.service_files:
            generic_service = self.get_gen_service(service.split('.')[0])
            services.append(generic_service.name)
        return services

    def set_gen_service(self, gen_service):
        cli_file = self.service_path + gen_service.name + '.xml'
        try:
            file_writer = open(cli_file, 'w')  # new StreamWriter
            if file_writer is None:
                LOG.error("Cannot open file %s for writing!", cli_file)
                return
            file_writer.write(gen_service.toDOM().toprettyxml())
            file_writer.close()
        except IOError as ioe:
            LOG.error("Unable to write service %s configuration in file %s",
                      gen_service.name, cli_file)
            LOG.error("%r", ioe)

    def delete_gen_service(self, gen_service_name):
        self._update_files()
        try:
            os.remove(self.service_path + gen_service_name + '.xml')
        except OSError as ose:
            LOG.error("Unable to remove service %s configuration",
                      gen_service_name)
            LOG.error("%r", ose)

    def gen_service_known(self, service_name):
        self._update_files()
        return service_name + '.xml' in self.service_files

    '''  Manage instance services:\n'
     '     get_all_inst_services(Type): List[inst_service]\n'
     '     get_all_inst_services(): Dict{Type:List[inst_service]}\n'
     '     get_inst_service(inst_service_name): inst_service\n '
     '     set_inst_service(inst_service): None
     '     delete_inst_service(inst_service_name)
    '''

    def get_inst_service(self, inst_service_name):
        try:
            xml = open(
                self.instance_service_path + inst_service_name + '.xml').read()
            inst_service = ServiceInstance.CreateFromDocument(xml)
            return inst_service
        except IOError as e:
            print(e)
            LOG.error(_("Problem during the loading of '%s'"),
                      inst_service_name + '.xml')
            raise NoServiceInstanceReprException(inst_service_name)

    def get_all_inst_services(self, instance_of=None):
        self._update_files()
        inst_services = {}
        for inst_service_name in self.instance_service_files:
            instance_service = self.get_inst_service(
                inst_service_name.split('.')[0])
            service_ref = instance_service.InstanceOf.href
            if service_ref in inst_services:
                inst_services[service_ref].append(instance_service)
            else:
                inst_services[service_ref] = []
                inst_services[service_ref].append(instance_service)
        if instance_of is not None:
            return inst_services[instance_of]
        return inst_services

    def set_inst_service(self, inst_service):
        cli_file = self.instance_service_path + inst_service.name + '.xml'
        try:
            file_writer = open(cli_file, 'w')  # new StreamWriter
            if file_writer is None:
                LOG.error("Cannot open file %s for writing!", cli_file)
                return
            file_writer.write(inst_service.toDOM().toprettyxml())
            file_writer.close()
        except IOError as ioe:
            LOG.error(
                "Unable to write instance service %s configuration in file %s",
                inst_service.name, cli_file)
            LOG.error("%r", ioe)

    def delete_inst_service(self, inst_service_name):
        self._update_files()
        try:
            os.remove(self.instance_service_path + inst_service_name + '.xml')
        except OSError as ose:
            LOG.error("Unable to remove instance service %s configuration",
                      inst_service_name)
            LOG.error("%r", ose)

    def inst_service_known(self, inst_service_name):
        self._update_files()
        return inst_service_name + '.xml' in self.instance_service_files

    '''  Manage services rules:\n'
     '     get_all_rules(Type): List[rules]
     '     get_all_rules(): Dict{Type: List[rules]}
     '     get_rule(rule_name): rule
     '     set_rule(rule): None
     '     delete_rule(rule_name): None
    '''

    def get_rule(self, rule_name):
        try:
            xml = open(os.path.join(self.rules_path, rule_name + '.xml')).read()
            inst_service = Rule.CreateFromDocument(xml)
            return inst_service
        except IOError as e:
            print(e)
            LOG.error(_("Problem during the loading of '%s'"),
                      rule_name + '.xml')
            raise NoRuleReprException(rule_name)

    def get_all_rules(self, service_type=None):
        # TODO implement extraction with service_type
        self._update_files()
        rules = []
        for rule_name in self.rule_files:
            rules.append(self.get_rule(rule_name.split('.')[0]))
        return rules

    def set_rule(self, rule):
        cli_file = self.rules_path + rule.name + '.xml'
        try:
            file_writer = open(cli_file, 'w')  # new StreamWriter
            if file_writer is None:
                LOG.error("Cannot open file %s for writing!", cli_file)
                return
            file_writer.write(rule.toDOM().toprettyxml())
            file_writer.close()
        except IOError as ioe:
            LOG.error("Unable to write rule %s configuration in file %s",
                      rule.name, cli_file)
            LOG.error("%r", ioe)

    def rule_known(self, rule_name):
        self._update_files()
        return rule_name + '.xml' in self.rule_files

    def delete_rule(self, rule_name):
        self._update_files()
        try:
            os.remove(self.rules_path + rule_name + '.xml')
        except OSError as ose:
            LOG.error("Unable to remove rule %s configuration",
                      rule_name)
            LOG.error("%r", ose)

    '''  Manage OS references:\n'
     '     get_conf_references(type): conf_references
     '     get_all_conf_references(): Dict{Type: conf_references}
     '     set_conf_references(conf_references): None
    '''

    def get_conf_references(self, type):
        try:
            xml = open(os.path.join(self.os_ref_path, type + '.xml')).read()
            os_ref = OSreference.CreateFromDocument(xml)
            return os_ref
        except IOError as e:
            print(e)
            LOG.error(_("Problem during the loading of '%s'"), type + '.xml')
            raise NoOSRefReprException(type)

    def get_all_conf_references(self):
        self._update_files()
        os_references = {}
        for ref_name in self.os_ref_files:
            os_references[ref_name] = self.get_conf_references(
                ref_name.split('.')[0])
        return os_references

    def set_conf_references(self, os_ref):
        cli_file = self.os_ref_path + os_ref.name + '.xml'
        try:
            file_writer = open(cli_file, 'w')  # new StreamWriter
            if file_writer is None:
                LOG.error("Cannot open file %s for writing!", cli_file)
                return
            file_writer.write(os_ref.toDOM().toprettyxml())
            file_writer.close()
        except IOError as ioe:
            LOG.error("Unable to write references %s configuration in file %s",
                      os_ref.name, cli_file)
            LOG.error("%r", ioe)

    def conf_reference_known(self, type):
        self._update_files()
        return type + '.xml' in self.os_ref_files

    def delete_conf_reference(self, type):
        self._update_files()
        try:
            os.remove(self.os_ref_path + type + '.xml')
        except OSError as ose:
            LOG.error(
                "Unable to remove configuration reference %s configuration",
                type)
            LOG.error("%r", ose)

    '''  Extract physical infrastructure:
     ' get_infrastructure_matrix(): List[List[String]]
    '''

    def get_infrastructure_matrix(self):
        LOG.info(_('loading: %s'), self.scenario_file)
        matrix = []
        try:
            topo_db = open(self.scenario_file)
        except:
            LOG.error(_("Problem during the loading from database %r"),
                      self.scenario_file)
            raise TopologyLoadingException(self.scenario_file)
        for line in topo_db:
            matrix.append(line.replace(' ', '').replace('\n', '').split(';'))
        LOG.info(_('Infrastructure matrix has been successfully loaded : %s'),
                 matrix)
        topo_db.close()
        return matrix

