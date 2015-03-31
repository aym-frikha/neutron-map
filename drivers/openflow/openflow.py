from .database_manager import DatabaseManager
from . import config

import logging
LOG = logging.getLogger(config.OPENFLOW_DRIVER_LOGGER_NAME)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=config.OPENFLOW_DRIVER_ABS_LOG_FILE,
                    filemode='w')



class OpenFlowDriver(object):
    def __init__(self):
        self.db_manager = DatabaseManager()
    
    def handle(self, device_name):
        # Consult openflow.devices table if a device with such name exists
        # If it does, store it's information / configuration in self.device_info and return True else False
        self.device = self.db_manager.get_device(device_name)
        if self.device :
            return True
        return False
    
    def retrieve_conf(self, device_name):
        if not self.handle(device_name):
            return False
        return self.device
                
            
    def configure_device(self, device_name, device_object):
        if not self.handle(device_name):
            return False
        # Insert into devices to update table (deploy_config)
        self.db_manager.add_device_to_configure(device_name)
        
        
        
