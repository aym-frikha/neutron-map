import re
import traceback
# # IF IN NEUTRON
from neutron.openstack.common import log as logging
LOG = logging.getLogger(__name__)



def format_port(port):
    return re.sub('/', '_', port)

def device_for_instance(instance):
    return instance.split('-')[0].lstrip(' ')

def port_for_instance(instance):
    return instance.split('-')[1]

def service_for_instance(instance):
    return '-'.join(instance.split('-')[2:]).split('.')[0]

class TopologyLoadingException(Exception):
    def __init__(self, file):
        top = traceback.extract_stack()[-1]
        message = _("Error in %s loading file %s") % (_(top), _(file))
        super(Exception, self).__init__(message)
        self.message = message

class NoDriverException(Exception):
    pass

class NoDeviceReprException(Exception):
    def __init__(self, device):
        message = _("Device %s has no known xml representation") % (
                    _(device))
        super(Exception, self).__init__(message)
        self.message = message

class NoRuleReprException(Exception):
    def __init__(self, rule):
        message = _("Rule %s has no known xml representation") % (
                    _(rule))
        super(Exception, self).__init__(message)
        self.message = message

class NoServiceInstanceReprException(Exception):
    def __init__(self, inst_service):
        message = _("Service Instance %s has no known xml representation") % (
                    _(inst_service))
        super(Exception, self).__init__(message)
        self.message = message

class NoServiceReprException(Exception):
    def __init__(self, service):
        message = _("Service  %s has no known xml representation") % (
                    _(service))
        super(Exception, self).__init__(message)
        self.message = message

class NoOSRefReprException(Exception):
    def __init__(self, os_ref):
        message = _("OS references  %s has no known xml representation") % (
                    _(os_ref))
        super(Exception, self).__init__(message)
        self.message = message

class ServiceError(Exception):
    pass

class DriverFails(Exception):
    pass
