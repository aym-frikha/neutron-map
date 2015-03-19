__author__ = 'aymen'

import paramiko
import sys
# username = ('user')
# password = ('1234')
# hostname = ('test-server.com')
ports = 22
remoteD = ('/home/thinkmate/GNS3/Projects/Scenario3/configs/')

def check(sftp, path):
    parts = path.split('/')
    for n in range(2, len(parts) + 1):
        path = '/'.join(parts[:n])
        print 'Path:', path,
        sys.stdout.flush()
        try:
            s = sftp.stat(path)
            print 'mode =', oct(s.st_mode)
        except IOError as e:
            print e


def put_configuration(equipment_name, ip_address, login, password, configuration):
    # with open('/tmp/' + equipment_name + ".cfg", "w+") as text_file:
    #     text_file.write( configuration)
    # paramiko.util.log_to_file('/tmp/paramiko.log')
    # transport = paramiko.Transport(((ip_address), ports))
    # transport.connect(username = (login), password = (password))
    # sftp = paramiko.SFTPClient.from_transport(transport)
    # check(sftp, remoteD)
    # check(sftp, '/tmp/' + equipment_name + ".cfg")
    # try:
    #     sftp.put('/tmp/' + equipment_name + ".cfg", remoteD + equipment_name + ".cfg")
    # except IOError as e:
    #     print e
    # sftp.close()
    # transport.close()
    pass