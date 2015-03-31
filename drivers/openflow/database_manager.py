import MySQLdb
from . import config
from .openflow_controller import Device, Link, Port

import logging
LOG = logging.getLogger(config.DATABASE_LOGGER_NAME)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=config.DATABASE_ABS_LOG_FILE,
                    filemode='w')


class DatabaseManager(object):
    connection = None
    def __init__(self):
        self.host = config.MYSQL_HOST
        self.user = config.MYSQL_USER
        self.passwd = config.MYSQL_PASSWD
        self.db = config.MYSQL_DB
    
    def connect(self):
        try:
            self.connection = MySQLdb.connect (host = self.host, user = self.user, passwd = self.passwd, db = self.db)
        except Exception as e:
            LOG.error(_("Unable to Connect to Openflow Database"), e)

    def get_connection(self):
        if not self.connection :
            self.connect()
        return self.connection
    
    def add_device(self, device):
        if not device:
            return False
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO devices(device_id, device_name, ofproto_version, ip_address) VALUES(%s, %s, %i, %s)", (device.dpid, device.name, device.ofproto_version, device.ip_address))
            cursor.execute("INSERT INTO devices_updates(device_id, device_name, ofproto_version, ip_address) VALUES(%s, %s, %i, %s)", (device.dpid, device.name, device.ofproto_version, device.ip_address))
        except Exception as e:
            LOG.error(_("An error occurred while inserting a new device with id : %(id)s. Exception : %(exception)s"), {'id': device.dpid, 'exception': e})
            cursor.close()
            return False
        cursor.close()
        return True
    
    def update_device(self, device):
        if not device:
            return False
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE devices SET device_name = %s, ofproto_version = %i, ip_address = %s WHERE device_id = %s", (device.name, device.ofproto_version, device.ip_address, device.dpid))
            cursor.execute("INSERT INTO devices_updates(device_id, device_name, ofproto_version, ip_address) VALUES(%s, %s, %i, %s)", (device.dpid, device.name, device.ofproto_version, device.ip_address))
        except Exception as e:
            LOG.error(_("An error occurred while updating device with id : %(id)s. Exception : %(exception)s"), {'id': device.dpid, 'exception': e})
            cursor.close()
            return False
        cursor.close()
        return True
    
    def delete_device(self, device):
        if not device:
            return False
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM devices WHERE device_id = %s", (device.dpid))
            cursor.execute("INSERT INTO devices_updates(device_id, device_name, ofproto_version, ip_address, state) VALUES(%s, %s, %i, %s, %i)", (device.dpid, device.name, device.ofproto_version, device.ip_address, 0))
        except Exception as e:
            LOG.error(_("An error occurred while deleting device with id : %(id)s. Exception : %(exception)s"), {'id': device.dpid, 'exception': e})
            cursor.close()
            return False
        cursor.close()
        return True 
    
    def get_device(self, device_name):
        if not device_name:
            return None
        connection = self.get_connection()
        cursor = connection.cursor()
        device = None
        try:
            cursor.execute("SELECT * FROM devices WHERE device_name = %s", (device_name))
            if cursor.rowcount > 0 :
                row = cursor.fetchone()
                device = Device(row[1], row[2], row[3], row[4], self.get_links(device_name))
        except Exception as e:
            LOG.error(_("An error occurred while selecting Device %(device)s. Exception : %(exception)s"), {'device': device_name, 'exception': e})
        cursor.close()
        return device
    
    def get_device_by_id(self, device_id):
        if not device_id:
            return None
        connection = self.get_connection()
        cursor = connection.cursor()
        device = None
        try:
            cursor.execute("SELECT * FROM devices WHERE device_id = %s", (device_id))
            if cursor.rowcount > 0 :
                row = cursor.fetchone()
                device = Device(row[1], row[2], row[3], row[4], self.get_links(row[2]))
        except Exception as e:
            LOG.error(_("An error occurred while selecting Device %(device)s. Exception : %(exception)s"), {'device': device_id, 'exception': e})
        cursor.close()
        return device
    
    def add_device_to_configure(self, device_name):
        if not device_name:
            return False
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT IGNORE INTO deploy_config(device_name) VALUES(%s)", (device_name))
        except Exception as e:
            LOG.error(_("An error occurred while inserting Device %(device)s to be configured. Exception : %(exception)s"), {'device': device_name, 'exception': e})
            cursor.close()
            return False
        cursor.close()
        return True
    
    def get_devices_to_configure(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        devices = []
        try:
            cursor.execute("SELECT * FROM deploy_config")
            rows = cursor.fetchall()
            cursor.execute("TRUNCATE TABLE deploy_config")
            for row in rows:
                devices.append(row[0])
        except Exception as e:
            LOG.error(_("An error occurred while retrieving all devices to be configured. Exception : %(exception)s"), {'exception': e})
        cursor.close()
        return devices
    
    def add_link(self, link):
        if not link:
            return False
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO links(src_device_name, dst_device_name, port) VALUES(%s, %s, %i)", (link.src, link.dst, link.port_src))
            cursor.execute("INSERT INTO links(src_device_name, dst_device_name, port) VALUES(%s, %s, %i)", (link.dst, link.src, link.port_dst))
            cursor.execute("INSERT INTO links_updates(src_device_name, dst_device_name, port_src, port_dst) VALUES(%s, %s, %i, %i)", (link.src, link.dst, link.port_src, link.port_dst))
        except Exception as e:
            LOG.error(_("An error occurred while inserting a new Link between Device %(deviceA)s and Device %(deviceB)s on ports %(port_src)i and %(port_dst)i. Exception : %(exception)s"), {'deviceA': link.src, 'deviceB': link.dst, 'port_src': link.port_src, 'port_dst': link.port_dst, 'exception': e})
            cursor.close()
            return False
        cursor.close()
        return True
    
    def update_link(self, link):
        if not link:
            return False
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE link SET port = %i WHERE src_device_name = %s AND dst_device_name = %s", (link.port_src, link.src, link.dst))
            cursor.execute("UPDATE link SET port = %i WHERE src_device_name = %s AND dst_device_name = %s", (link.port_dst, link.dst, link.src))
            cursor.execute("INSERT INTO links_updates(src_device_name, dst_device_name, port_src, port_dst) VALUES(%s, %s, %i, %i)", (link.src, link.dst, link.port_src, link.port_dst))
        except Exception as e:
            LOG.error(_("An error occurred while updating Link between Device %(deviceA)s and Device %(deviceB)s on ports %(port_src)i and %(port_dst)i. Exception : %(exception)s"), {'deviceA': link.src, 'deviceB': link.dst, 'port_src': link.port_src, 'port_dst': link.port_dst, 'exception': e})
            cursor.close()
            return False
        cursor.close()
        return True
    
    def delete_link(self, link):
        if not link:
            return False
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM links WHERE src_device_name = %s AND dst_device_name = %s", (link.src, link.dst))
            cursor.execute("DELETE FROM links WHERE src_device_name = %s AND dst_device_name = %s", (link.dst, link.src))
            cursor.execute("INSERT INTO links_updates(src_device_name, dst_device_name, port_src, port_dst, state) VALUES(%s, %s, %i, %i, %i)", (link.src, link.dst, link.port_src, link.port_dst, 0))
        except Exception as e:
            LOG.error(_("An error occurred while deleting Link between Device %(deviceA)s and Device %(deviceB)s on ports %(port_src)i and %(port_dst)i. Exception : %(exception)s"), {'deviceA': link.src, 'deviceB': link.dst, 'port_src': link.port_src, 'port_dst': link.port_dst, 'exception': e})
            cursor.close()
            return False
        cursor.close()
        return True
    
    def get_link(self, src_device_name, dst_device_name):
        if not src_device_name or not dst_device_name:
            return None
        connection = self.get_connection()
        cursor = connection.cursor()
        link = None
        try:
            cursor.execute("SELECT * FROM links WHERE src_device_name = %s AND dst_device_name = %s", (src_device_name, dst_device_name))
            if cursor.rowcount > 0 :
                row = cursor.fetchone()
                link = Link(row[0], row[1], row[2])
        except Exception as e:
            LOG.error(_("An error occurred while selecting Link between %(device1)s and %(device2)s. Exception : %(exception)s"), {'device1': src_device_name, 'device2': dst_device_name, 'exception': e})
        cursor.close()
        return link
    
    def get_links(self, device_name):
        if not device_name:
            return None
        connection = self.get_connection()
        cursor = connection.cursor()
        links = []
        try:
            cursor.execute("SELECT * FROM links WHERE src_device_name = %s", (device_name))
            rows = cursor.fetchall()
            for row in rows:
                link = Link(row[0], row[1], row[2])
                links.append(link)
        except Exception as e:
            LOG.error(_("An error occurred while selecting Links for %(device)s. Exception : %(exception)s"), {'device': device_name, 'exception': e})
        cursor.close()
        return links
    
    def add_port(self, port):
        if not port:
            return False
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO ports(port_no, name, network_id, hw_address, mac_address, device_id) VALUES(%i, %s, %s, %s, %s, %s)", (port.port_no, port.name, port.network_id, port.hw_addr, port.mac_address, port.dpid))
            cursor.execute("INSERT INTO ports_updates(port_no, name, network_id, hw_address, mac_address, device_id) VALUES(%i, %s, %s, %s, %s, %s)", (port.port_no, port.name, port.network_id, port.hw_addr, port.mac_address, port.dpid))
        except Exception as e:
            LOG.error(_("An error occurred while inserting a new port with id : %(id)s. Exception : %(exception)s"), {'id': port.port_no, 'exception': e})
            cursor.close()
            return False
        cursor.close()
        return True
    
    def update_port(self, port):
        if not port:
            return False
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE ports SET name = %s, network_id = %s, hw_address = %s, mac_address = %s, device_id = %s WHERE port_no = %i", (port.name, port.network_id, port.hw_addr, port.mac_address, port.dpid, port.port_no))
            cursor.execute("INSERT INTO ports_updates(port_no, name, network_id, hw_address, mac_address, device_id) VALUES(%i, %s, %s, %s, %s, %s)", (port.port_no, port.name, port.network_id, port.hw_addr, port.mac_address, port.dpid))
        except Exception as e:
            LOG.error(_("An error occurred while updating port with id : %(id)s. Exception : %(exception)s"), {'id': port.port_no, 'exception': e})
            cursor.close()
            return False
        cursor.close()
        return True
    
    def delete_port(self, port):
        if not port:
            return False
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM ports WHERE port_no = %i", (port.port_no))
            cursor.execute("INSERT INTO ports_updates(port_no, name, network_id, hw_address, mac_address, device_id, state) VALUES(%i, %s, %s, %s, %s, %s, %i)", (port.port_no, port.name, port.network_id, port.hw_addr, port.mac_address, port.dpid, 0))
        except Exception as e:
            LOG.error(_("An error occurred while deleting port with id : %(id)s. Exception : %(exception)s"), {'id': port.port_no, 'exception': e})
            cursor.close()
            return False
        cursor.close()
        return True 
    
    def get_port(self, port_no):
        if not port_no:
            return None
        connection = self.get_connection()
        cursor = connection.cursor()
        port = None
        try:
            cursor.execute("SELECT * FROM ports WHERE port_no = %i", (port_no))
            if cursor.rowcount > 0 :
                row = cursor.fetchone()
                port = Port(row[6], row[1], row[2], row[4], row[3], row[5])
        except Exception as e:
            LOG.error(_("An error occurred while selecting Port %(port)s. Exception : %(exception)s"), {'port': port_no, 'exception': e})
        cursor.close()
        return port
    
    def close(self):
        try:
            if self.connection:
                self.connection.close()
        except Exception as e:
            LOG.error(_("Unable to Close MySQL Connection"), e)
            
