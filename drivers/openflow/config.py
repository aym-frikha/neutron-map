# Used by openflow_controller.py
OPENFLOW_DRIVER_FOLDER = '/opt/stack/data/neutron/plugins/map/drivers/openflow/openflow_driver_folder/'
OPENFLOW_DRIVER_LOGGER_NAME = 'openflow_driver'
OPENFLOW_DRIVER_LOG_FILE = 'openflow_driver.log'
OPENFLOW_DRIVER_ABS_LOG_FILE = OPENFLOW_DRIVER_FOLDER + OPENFLOW_DRIVER_LOG_FILE

# Used by openflow_controller.py
OPENFLOW_CONTROLLER_FOLDER = '/opt/stack/data/neutron/plugins/map/drivers/openflow/openflow_controller_folder/'
OPENFLOW_CONTROLLER_LOGGER_NAME = 'openflow_controller'
OPENFLOW_CONTROLLER_LOG_FILE = 'openflow_controller.log'
OPENFLOW_CONTROLLER_ABS_LOG_FILE = OPENFLOW_CONTROLLER_FOLDER + OPENFLOW_CONTROLLER_LOG_FILE
OPENFLOW_CONFIG_INTERVAL = 3 #seconds

# Used by database_manager.py
MYSQL_USER = ''
MYSQL_PASSWD = ''
MYSQL_HOST = ''
MYSQL_DB = 'openflow'
DATABASE_FOLDER = '/opt/stack/data/neutron/plugins/map/drivers/openflow/database_manager_folder/'
DATABASE_LOGGER_NAME = 'database_manager'
DATABASE_LOG_FILE = 'database.log'
DATABASE_ABS_LOG_FILE = DATABASE_FOLDER + DATABASE_LOG_FILE


# Used by objectsmanager.py
OBJ_MNGR_LOGGER_NAME = 'objects_manager'
OBJ_MNGR_FOLDER = '/opt/stack/data/neutron/plugins/map/drivers/openflow/objectsmanager_folder/'
OBJ_MNGR_LOG_FILE = 'object_manager.log'
OBJ_MNGR_ABS_LOG_FILE = OBJ_MNGR_FOLDER + OBJ_MNGR_LOG_FILE
OBJ_MNGR_TABLES_LIST = {'devices', 'links', 'ports'}
OBJ_MNGR_TABLES_UPDATE_PATTERN = "_updates"
OBJ_MNGR_UPDATE_TIMER = 3 #seconds
OBJ_MNGR_AUTOSTART = True
TOPO_MNGR_FOLDER = '/opt/stack/data/neutron/plugins/map/'
TOPO_MNGR_LOG_FILE = 'plugins/topologymanager_folder/topology_manager.log'
TOPO_MNGR_DB_FILE = 'Scenario1.db'
TOPO_MNGR_ABS_LOG_FILE = TOPO_MNGR_FOLDER + TOPO_MNGR_LOG_FILE
TOPO_MNGR_ABS_DB_FILE = TOPO_MNGR_FOLDER + TOPO_MNGR_DB_FILE
