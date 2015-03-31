from neutron.plugins.map.plugins.ryu.ryu.base import app_manager
from neutron.plugins.map.plugins.ryu.ryu.controller.handler import set_ev_cls
from neutron.plugins.map.plugins.ryu.ryu.controller import network
from neutron.plugins.map.plugins.ryu.ryu.topology import event
from neutron.plugins.map.plugins.ryu.ryu.ofproto import ofproto_v1_0, ofproto_v1_2, nx_match
from neutron.plugins.map.plugins.ryu.ryu.ofproto.ether import ETH_TYPE_LLDP
from neutron.plugins.map.plugins.ryu.ryu.lib import addrconv
from neutron.plugins.map.plugins.ryu.ryu.lib.packet import lldp
from .database_manager import DatabaseManager
from . import config
import time
from threading import Thread

import logging
LOG = logging.getLogger(config.OPENFLOW_CONTROLLER_LOGGER_NAME)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=config.OPENFLOW_CONTROLLER_ABS_LOG_FILE,
                    filemode='w')



class MAPController(app_manager.RyuApp):
    
    PREFIX_DEVICE_NAME = "OPENFLOW_SWITCH"

    def __init__(self, *args, **kwargs):
        super(MAPController, self).__init__(*args, **kwargs)
        self.counter = 0
        self.switches = {} # datapath_id => switch_name
        self.dps = {} # Switch_Name => Datapath (Switch)
        self.db_manager = DatabaseManager()
        self.timer = config.OPENFLOW_CONFIG_INTERVAL
        self.launch()   

    @set_ev_cls(event.EventSwitchEnter)
    def add_device(self, ev):
        switch = ev.switch
        self.counter += 1
        switch_name = self.PREFIX_DEVICE_NAME + str(self.counter)
        self.switches[switch.dp.id] = switch_name
        self.dps[switch_name] = switch.dp
        self.db_manager.add_device(Device(switch.dp.id, switch_name, switch.dp.ofproto.OFP_VERSION))
        ports = switch.ports.values()
        for port in ports:
            self.add_single_port(port)
        

    @set_ev_cls(event.EventSwitchLeave)
    def remove_device(self, ev):
        switch = ev.switch
        switch_name = self.switches[switch.dp.id]
        del self.switches[switch.dp.id]
        del self.dps[switch_name]
        self.db_manager.delete_device(Device(switch.dp.id, switch_name, switch.dp.ofproto.OFP_VERSION))
    
    @set_ev_cls(event.EventLinkAdd)  
    def add_link(self, ev):
        link = ev.link
        src_switch_name = self.switches[link.src.dpid]
        dst_switch_name = self.switches[link.dst.dpid]
        # Add Forward and Reverse Link
        self.db_manager.add_link(Link(src_switch_name, dst_switch_name, link.src.port_no, link.dst.port_no))
        
    @set_ev_cls(event.EventLinkDelete)  
    def remove_link(self, ev):
        link = ev.link
        src_switch_name = self.switches[link.src.dpid]
        dst_switch_name = self.switches[link.dst.dpid]
        # Delete Forward and Reverse Link
        self.db_manager.delete_link(Link(src_switch_name, dst_switch_name, link.src.port_no, link.dst.port_no))
        
    @set_ev_cls(event.EventPortAdd)  
    def add_port(self, ev):
        port = ev.port
        self.db_manager.add_port(Port(port.dpid, port.port_no, port.name, port.hw_addr))
        
    def add_single_port(self, port):
        self.db_manager.add_port(Port(port.dpid, port.port_no, port.name, port.hw_addr))
    
    @set_ev_cls(event.EventPortModify)  
    def modify_port(self, ev):
        port = ev.port
        self.db_manager.update_port(Port(port.dpid, port.port_no, port.name, port.hw_addr))
        
    @set_ev_cls(event.EventPortDelete)  
    def remove_port(self, ev):
        port = ev.port
        self.db_manager.delete_port(Port(port.dpid, port.port_no, port.name, port.hw_addr))
        
    @set_ev_cls(network.EventNetworkPort)
    def update_port_network_id(self, ev):
        add_del = ev.add_del
        if not add_del:
            return
        port = self.db_manager.get_port(Port(ev.dpid, ev.port_no))
        if add_del == True:
            port.network_id = ev.network_id
        else:
            port.network_id = None
        self.db_manager.update_port(port)
        
    @set_ev_cls(network.EventMacAddress)
    def update_port_mac_address(self, ev):
        add_del = ev.add_del
        if not add_del:
            return
        port = self.db_manager.get_port(Port(ev.dpid, ev.port_no))
        if add_del == True:
            port.mac_address = ev.mac_address
        else:
            port.mac_address = None
        port.network_id = ev.network_id
        self.db_manager.update_port(port)
    
    # TODO: Assure that deploy_config really does what we intend for it to do. Correct implementation if necessary
    def deploy_config(self):
        LOG.info('Configuration Deployer Running...')
        while self.run_deployer :
            time.sleep(self.timer)
            devices = self.db_manager.get_devices_to_configure()
            for device_name in devices:
                dp = self.dps[device_name]
                if dp is not None:
                    ofproto = dp.ofproto
                    ofproto_parser = dp.ofproto_parser

                    # TODO:XXX need other versions
                    if ofproto.OFP_VERSION == ofproto_v1_0.OFP_VERSION:
                        rule = nx_match.ClsRule()
                        rule.set_dl_dst(addrconv.mac.text_to_bin(
                                    lldp.LLDP_MAC_NEAREST_BRIDGE))
                        rule.set_dl_type(ETH_TYPE_LLDP)
                        actions = [ofproto_parser.OFPActionOutput(
                                    ofproto.OFPP_CONTROLLER, self.LLDP_PACKET_LEN)]
                        dp.send_flow_mod(
                        rule=rule, cookie=0, command=ofproto.OFPFC_ADD,
                        idle_timeout=0, hard_timeout=0, actions=actions,
                        priority=0xFFFF)
                    elif ofproto.OFP_VERSION >= ofproto_v1_2.OFP_VERSION:
                        match = ofproto_parser.OFPMatch(
                        eth_type=ETH_TYPE_LLDP,
                        eth_dst=lldp.LLDP_MAC_NEAREST_BRIDGE)
                        # OFPCML_NO_BUFFER is set so that the LLDP is not
                        # buffered on switch
                        parser = ofproto_parser
                        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER,
                                                      ofproto.OFPCML_NO_BUFFER
                                                      )]
                        inst = [parser.OFPInstructionActions(
                            ofproto.OFPIT_APPLY_ACTIONS, actions)]
                        mod = parser.OFPFlowMod(datapath=dp, match=match,
                                            idle_timeout=0, hard_timeout=0,
                                            instructions=inst,
                                            priority=0xFFFF)
                        dp.send_msg(mod)
                    else:
                        LOG.error('Cannot install flow. Unsupported Version. %x',
                              dp.ofproto.OFP_VERSION)
        LOG.info('Configuration Deployer Stopped')
        return
    
    def start(self):
        self.run_deployer = True
    
    def stop(self):
        self.run_deployer = False
    
    def launch(self):
        try:
            self.start()
            self.config_deployer = Thread(target = self.deploy_config)
            self.config_deployer.start() 
        except Exception as e:
                LOG.error(_("Failed to start Configuration Deployer"), e)
                return False
        return True
    
    def cleanUp(self):
        self.stop()
        
        
class Device(object):
    def __init__(self, dpid, name, ofproto_version = 0x05, ip_address = None, links = []):
        super(Device, self).__init__()
        self.dpid = dpid
        self.name = name
        self.ofproto_version = ofproto_version
        self.ip_address = ip_address
        self.links = links
        
class Link(object):
    def __init__(self, src, dst, port_src, port_dst = None):
        super(Link, self).__init__()
        self.src = src
        self.dst = dst
        self.port_src = port_src
        self.port_dst = port_dst
        
class Port(object):
    def __init__(self, dpid, port_no, name = None, hw_addr = None, network_id = None, mac_address = None):
        super(Port, self).__init__()
        self.dpid = dpid
        self.port_no = port_no
        self.name = name
        self.hw_addr = hw_addr
        self.network_id = network_id
        self.mac_address = mac_address