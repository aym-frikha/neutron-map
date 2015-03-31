import sys 
import os
import threading
import time
from neutron.plugins.map.topologymanager import TopologyManager
from .database_manager import DatabaseManager
from . import config

sys.path.append(os.path.abspath("/opt/stack/dmap/neutron/plugins/map"))

import logging
LOG = logging.getLogger(config.OBJ_MNGR_LOGGER_NAME)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=config.OBJ_MNGR_ABS_LOG_FILE,
                    filemode='w')


class ObjectsManager(object):
	
	def __init__(self, *args, **kwargs):
		super(ObjectsManager, self).__init__(*args, **kwargs)
		self.table_pattern = config.OBJ_MNGR_TABLES_UPDATE_PATTERN
		self.tables_list = config.OBJ_MNGR_TABLES_LIST
		self.update_timer = config.OBJ_MNGR_UPDATE_TIMER
		self.autostart = config.OBJ_MNGR_AUTOSTART
		self.running = False
		self.thread = threading.Timer(self.update_timer, self.check_network_changes)
		
		self.db_manager = DatabaseManager()
		self.topo_manager = TopologyManager()
		self.topo_manager.__load_db__(config.TOPO_MNGR_ABS_DB_FILE)
		if self.autostart:
			self.start()
		
	def start(self):
		if self.running != True:
			self.running = True
			try:
				self.thread.start()
				LOG.info('ObjectManager has started thread')
			except Exception as e:
				LOG.error(_("ObjectsManager is unable to Start thread"), e)
				return False
		return True
	
	def stop(self):
		if self.running != False:
			self.running = False
			try:
				self.thread.cancel()
				LOG.info('objects_manager has stopped thread')
			except Exception as e:
				LOG.error(_("ObjectsManager is unable to Start thread"), e)
				return False
		return True
	
	def restart(self):
		if self.stop() == True:
			return self.start()
		return False
		
	def check_network_changes(self):
		print(time.ctime())
		if self.running != True:
			self.stop()
		else:
			if self.tables_list != None:
				for table in self.tables_list:
					self.check_updates(table)
			self.thread = threading.Timer(self.update_timer, self.check_network_changes)
			try:
				self.thread.start()
			except Exception as e:
				LOG.error(_("ObjectsManager is unable to continue thread"), e)	
	
	def check_updates(self, table):		
		connection = self.db_manager.get_connection()
		cursor = connection.cursor()
		try:
			cursor.execute('SELECT * FROM ' + table + self.table_pattern)
			if cursor.rowcount > 0:
				rows = cursor.fetchall()
				for row in rows:
					index = len(row) - 1
					if row[index] == 0:
						self.apply_delete(row, table)
					else:
						self.apply_update(row, table)
					self.delete_update_entry(table, row, cursor)
			connection.commit()
		except Exception as e:
			LOG.error(_("ObjectsManager is unable to access the database"), e)	
		cursor.close()
		return True
	
	def delete_update_entry(self, table, row, cursor):
		try:
			if table == 'links':
				cursor.execute('DELETE FROM '+ table + self.table_pattern + ' WHERE src_device_name =\'' + str(row[0]) + '\' AND dst_device_name=\''+ str(row[1])+'\'')
			if table == 'devices':
				cursor.execute('DELETE FROM '+ table + self.table_pattern + ' WHERE id=' + str(row[0]))
		except Exception as e:
			LOG.error(_("ObjectsManager is unable to clean the update tables"), e)			
	
	def apply_delete(self, row, table):
		if table == 'links':
			self.topo_manager.update_link(row[0], str(row[2]), row[1], str(row[3]), 'DOWN')
			print('______________delete link ' + row[0] +'-' + row[1] + ' applied________________________')				
		if table == 'devices':
			self.topo_manager.update_node(row[2], 'DEL')
			print('______________delete device ' + row[2] +' applied________________________')				
		LOG.info('ObjectsManager has deleted ' + self.get_log_entry(row) + ' from ' + table)
		self.topo_manager.print_topo(config.TOPO_MNGR_ABS_DB_FILE, True)
		
	def apply_update(self,row,table):			
		if table == 'links':
			self.topo_manager.update_link(row[0], str(row[2]), row[1], str(row[3]), 'UP')
			print('______________update link ' + row[0] +'-' + row[1] + ' applied________________________')				
		if table == 'devices':
			self.topo_manager.update_node(row[2], 'ADD')
			print('______________delete device ' + row[2] + ' applied________________________')				
		LOG.info('ObjectsManager has updated ' + self.get_log_entry(row) + ' from ' + table)
		self.topo_manager.print_topo(config.TOPO_MNGR_ABS_DB_FILE, True)
		
	def get_log_entry(self, row):
		entry = ''
		for index in range(0, len(row)):
			entry += str(row[index]) + ' '
		entry = entry.strip()
		return entry
		
		
if __name__ == "__main__":
	#print 'Execution of ObjectManager.py'
	objectif = ObjectsManager()
	#logging.info('Object manager starting')
	#print 'Object initialised'