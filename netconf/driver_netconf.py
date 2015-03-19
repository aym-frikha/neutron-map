from time import sleep
import sys
from xml.etree import ElementTree as ET
import os

from ncclient import manager
import ncclient.transport.errors as sshErr
import cli_generator





# # IF IN NEUTRON
#import logging
from neutron.openstack.common import log as logging
from neutron.plugins.map import map_utils, iosparser

LOG = logging.getLogger(__name__)
# # Else
#from ..fake_environment import _
#from ..fake_environment import log

from oslo.config import cfg



#logging.basicConfig(filename='/home/stack/netconf.log',level=logging.DEBUG)
#logger = logging.getLogger('ncclient.transport.session')

# Timeout used in second. Should be long on fully emulated solutions
timeout = 60

# Accept sshv2 keys, whatever they are
def unknown_host_cb(host, key):
    return True

class NetconfDriver(object):
    def __init__(self):
        self.devices_file = cfg.CONF.netconf.devices
        self.syntaxe = cfg.CONF.netconf.syntaxe
        self.cli_gen = cli_generator.cliGenerator()
        self.ios_parser = iosparser.IOSParser()
    
    def handle(self, device_name):
        devices_fd = open(self.devices_file)
        for device_line in devices_fd.read().split('\n'):
            self.device_data = device_line.split(',')
            if device_name == self.device_data[0]:
                return True
        return False
    
    def retrieve_conf(self, device_name):
        if not self.handle(device_name):
            return False
        name, ip, port, login, password = self.device_data[:5]
        try:
            with manager.connect_ssh(ip, port=port, username=login,
                                     password=password,
                                     unknown_host_cb=unknown_host_cb,
                                     look_for_keys=False) as m:
                config = m.get_config(source='running').data_xml
                xml = ET.fromstring(config)
                cli_config_db = xml[0]
                self.ios_parser.parse_cli_configuration(cli_config_db.text,
                                                        device_name)
                device = self.ios_parser.device

                return device
        except sshErr.SSHError as e:
            raise map_utils.DriverFails(str(e))
            
    def send_command(self, device_name, command_list):
        if not self.handle(device_name):
            return False
        name, ip, port, login, password, syntaxe = self.device_data[:6]
        if syntaxe + '.stx' not in os.listdir(self.syntaxe):
            LOG.error(_("Error, this syntax is unknown"))
            return False
        if not os.path.isfile(self.syntaxe + '/' + syntaxe + '.stx'):
            LOG.error(_("Error, syntaxe file, %s%s.stx is not a file ..."),
                      self.syntaxe, syntaxe)
            return False
        syntaxe_fd = open(self.syntaxe + '/' + syntaxe + '.stx')
        syntax_dict = eval(syntaxe_fd.readline())
        try:
            with manager.connect_ssh(ip, port=port, username=login,
                                     password=password,
                                     unknown_host_cb=unknown_host_cb,
                                     look_for_keys=False) as m:
                #template = """<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0"><aaa xmlns="http://tail-f.com/ns/aaa/1.1"><authentication> <users> <user xc:operation="delete"><name>%s</name></user></users></authentication></aaa></config>"""
                #ip_change = """<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
                #<cpi:xml-config-data xmlns:cpi="http://www.cisco.com/cpi_10/schema"><Hostname>R1</Hostname><Interface><InterfaceName>fastEthernet0/1</InterfaceName><IP><Address><IPAddress>192.168.1.1</IPAddress><Mask>255.255.255.0</Mask></Address></IP></Interface></cpi:xml-config-data></config>"""
                #hostname = """<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0"><cpi:cli_driver-config-data-block>username nectonfCreated</cpi:cli_driver-config-data-block></config>"""
                #hostname2 = """<config><cli_driver-config-data><cmd>username clement</cmd></cli_driver-config-data></config>"""
                cmd_list = ''
                for command in command_list:
                    cmd_list += syntax_dict['command'] % command
                conf_patch = syntax_dict['wrapper'] % cmd_list
                with m.locked(target='running'):
                    m.edit_config(target='running', config=conf_patch)

                return True
        except sshErr.SSHError as e:
            raise map_utils.DriverFails(str(e))

    def configure_device(self, device_name, device_object):
        if not self.handle(device_name):
            return False
        commands = self.cli_gen.command_for_device(device_name, device_object)
        return self.send_command(device_name, commands)





if __name__ == '__main__':

    sys.path.append('..')
    from ..neutron.plugins.map.fake_environment import _
    from ..neutron.plugins.map.fake_environment import log
    LOG = log()

    cfg.CONF(args=['--config-file', 'dneutron/example_conf.ini'], project='neutron', version='1')
    driver = NetconfDriver()
    if not driver.retrieve_conf('R1'):
        print "Wrong device_name"
    #if not driver.send_command('R1',['hostname R42', 'username autoadded']):
    #    print "Error while sending commands"
    # Gives some time to ssh to close... Yes. It's dirty. Buts It's how
    # ncclient closes ssh connections.
    sleep(1)

    #driver.configure_device('R1')
    #sleep(1)
