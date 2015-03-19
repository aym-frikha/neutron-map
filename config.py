# Copyright (c) 2013 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo.config import cfg


map_opts = [
    cfg.ListOpt('l2_services',
                default=['trunk-allow'],
                help=_("List of L2 services"
                       "Ordered list of L2 services.")),
    cfg.ListOpt('l3_services',
                default=['eompls_int.xml', 'vxlan', 'vpls' ],
                help=_("Ordered list of L3 services.")),
    cfg.StrOpt('default_scenar', default='',
               help=_("Default scenar used by infrastructure manager")),
    cfg.StrOpt('scenar_file', default='',
               help=_("File containing port matrix of the physical topology")),
    cfg.StrOpt('network_service_path', default='',
               help=_("Path containing instance services files")),
    cfg.StrOpt('network_path', default='',
               help=_("Path containing device files")),
    cfg.StrOpt('service_path', default='',
               help=_("Path containing service files")),
    cfg.StrOpt('service_rules_path', default='',
               help=_("Path containing service rules files")),
    #cfg.StrOpt('rules', default='/opt/stack/neutron/neutron/plugins/map/rules/',
         #      help=_("Path pointing folder containing decision rules")),
    cfg.ListOpt('drivers', default=['neutron.plugins.map.cli_driver.cli.CliDriver'],
               help=_("List of drivers class to load. Drivers are used to "
                      "communicate with devices")),
    cfg.StrOpt('os_references', default='',
               help=_("File containing all OS references")),
   # cfg.BoolOpt('load_conf_at_boot', default='False',
      #         help=_("Force config load, even if known, at plugin boot")),
]

netconf_opts = [
    cfg.StrOpt('devices', default='devices.csv',
               help=_("File describing known devices for this router")),
    cfg.StrOpt('syntaxe', default='',
               help=_("Path containing netconf syntaxes for a given device")),
    ]



cfg.CONF.register_opts(map_opts, "map")
cfg.CONF.register_opts(netconf_opts, "netconf")
