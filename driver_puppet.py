import sys
import db
import pyxb.utils.domutils
from DB_Structures import *

class Driver(object):
    def __init__(self):
        self.manifest_directory = 'manifests/'
        self.delete_me = True

    def apply_conf(self, device_id):
        # TODO: Is this device managed by this plugin?

        #Let's retrieve this device configuration
        if device_id == 'R2' and self.delete_me:
            self.delete_me = False
            raise Exception
        conf_path = db.get_device_conf(device_id)
        conf_file = open(conf_path)
        conf = conf_file.read()
        conf_file.close()
        device = Device.CreateFromDocument(conf)

        # We then parse this configuration tree into a python dict
        config_tree = device.ConfigTree
        ressources = {}
        for ressource_node in config_tree.Node:
            if not ressources.has_key(ressource_node.name):
                ressources[ressource_node.name] = {}
            parameters = {}
            #TODO Many children possible? What does it means?
            if (hasattr(ressource_node, 'Children')
                and ressource_node.Children != None):
                for parameter_node in ressource_node.Children.Node:
                    #for parameter_node in parameter_list.Node:
                    try:
                        if parameter_node.Value != None:
                            sub_service_value = parameter_node.Value
                        else:
                            sub_service_value = 'enable'
                    except AttributeError:
                        sub_service_value = 'enable'
                    parameters[parameter_node.name] = sub_service_value
                ressources[ressource_node.name][ressource_node.Value] = parameters

        # Manifest generation from the python dict
        manifest = 'node "' + device_id + '" {'
        for key in ressources.keys():
            # Manual looking for interface. TODO: This may be more flexible
            if key in ('interface', 'vlan'):
                for (int_name, parameters) in ressources[key].items():
                    manifest += ('\n\t' + key + ' {')
                    manifest += '\n\t\t' + '"' + int_name + '" :'
                    virgule = ''
                    for (parameter, value) in parameters.items() :
                        manifest += ('\n\t\t\t' + parameter + ' => ' + value +
                                     virgule)
                        if virgule != ',':
                            virgule += ','
                    manifest += '\n\t}'
        manifest += '\n}'

        # Open node file, clear it and write manifest
        file_path = self.manifest_directory + 'node_%s.pp' % device_id
        file = open(file_path, 'w+')
        file.write(manifest)
        file.close()


if __name__ == '__main__':
    d1 = Driver()
    d1.apply_conf('SW1')
