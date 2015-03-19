from neutron.openstack.common import importutils
from neutron.plugins.map import nodemanager as nodeManager, isolationprovider, \
    map_utils, dynamic_db, resources
from neutron.plugins.ml2 import driver_api as api
from oslo.config import cfg

from neutron.openstack.common import log as logging
LOG = logging.getLogger(__name__)

class DriverManager(object):

    def __init__(self, resources):
        self.model = resources
        self.isolation_provider = isolationprovider.IsolationProvider()
        self.node_config = nodeManager.NodeManager()
        self.load_drivers()

    def load_drivers(self):
        self.driver = []
        for driver_class in cfg.CONF.dneutron.drivers:
            driver = importutils.import_object(driver_class)
            self.driver.append(driver)

    def apply(self, context, mapping_dict, network_id):
        deployed_instances = {}
        LOG.info(_("Strategy is:\n%s"), mapping_dict)
        for isolation, mappings in mapping_dict.items():
            isolation_id = isolation.split('-')[-1]
            isolation_method = '-'.join(isolation.split('-')[:-1])
            for mapping in mappings:
                device, port, params = mapping
                segment = {api.NETWORK_TYPE: isolation_method,
                           api.PHYSICAL_NETWORK: port,
                           api.SEGMENTATION_ID: isolation_id}
                dynamic_db.add_network_segment(context.session, network_id, segment)
                if not self.isolation_provider.transactionnal(isolation_method):
                    try:
                        instances = self.isolation_provider.create_service_instance(
                                service_name=isolation_method,
                                devices_ports={device : port},
                                parameters=([isolation_id] + params))
                        instance = instances[device]
                        if not instance:
                            continue
                        else:
                            LOG.debug(_("Created %s"), instance)
                        self.node_config.deploy_service(device, instance)
                        self.e = None
                        deployed = self.deploy_config(device)
                        if not deployed:
                            raise map_utils.NoDriverException(_("No driver can "
                                             + "communicate with device ") + _(device))
                        if deployed_instances.has_key(isolation):
                            deployed_instances[isolation].append(mapping)
                        else:
                            deployed_instances[isolation] = []
                            deployed_instances[isolation].append(mapping)
                    except map_utils.NoDeviceReprException:
                        LOG.error(_("Device %s where not configured:" 
                                    + " no device representation could"
                                    + " be found"), device)
                        continue
                    except map_utils.ServiceError as e:
                        continue
                        LOG.error(_("Service %s could not be applied"
                                    + " on device %s"),
                                  isolation_method, device)
                        LOG.error(_(e))
                else:
                    # TODO: To be defined precisely: How values are returned.
                    pass
                    # instances_lst = self.service_provider.create_service_instance(
                    #         service_name=isolation_method,
                    #         devices_ports={device : port},
                    #         parameters=([isolation_id] + params))
                    # instances = instances_lst[device]
                    # for instance in instances:
                    #     self.node_config.deploy_service(device, instance)
                    #     self.e = None
                    #     try:
                    #         deployed = self.deploy_config(device)
                    #         if not deployed:
                    #         self.e = utils.NoDriverException(_("No driver can "
                    #         "communicate with device " + _(device))
                    #     except Exception as e:
                    #         self.e = e
                    #     finally:
                    #         if self.e != None:
                    #             raise self.e
                    #     if deployed_instances.has_key(isolation):
                    #         deployed_instances[isolation].append(mapping)
                    #     else:
                    #         deployed_instances[isolation] = []
                    #         deployed_instances[isolation].append(mapping)
                #TODO: if is virtual_host

 
    # Return true if applyed, false if no driver support this device, Exception
    # if deloyment fails.
    def deploy_config(self, device_name):
        device_object = self.model.get_device_by_name(device_name)
        for driver in self.driver:
            try:
                if driver.configure_device(device_name, device_object):
                    return True
            except AttributeError as e:
                LOG.error(_("Driver %s does not contains a %s method"), 
                    driver.__class__.__name__, 'configure_device')
                continue
        else:
            return False

    def retrieve_config(self, device_name):
        for driver in self.driver:
            retrieved = driver.retrieve_conf(device_name)
            if retrieved:
                self.model.create_device(retrieved, device_name)
                

        else:
            raise map_utils.NoDriverException(_("No driver can communicate with "
                                            + "device ") + _(device_name))

