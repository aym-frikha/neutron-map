from oslo.config import cfg
from neutron.plugins.map import nodemanager, isolationprovider


def main():
    

    cfg.CONF(args=['--config-file', 'example_conf.ini'], project='neutron', version='1')
    plugin = nodemanager.NodeManager()
    #device1 = plugin.get_device_by_file("Device - Nexus-1000v(2).xml")
    isolation = isolationprovider.IsolationProvider()
    #validator1 = validator.Validator(isolation.get_all_instances_names())
    #validator1.validate_all()
    #service = isolation.get_service('Vlan Access')
    #device = plugin.applicable_service_by_device('VlanProfile','Nexus-1000v(2)')
    devices =['R2','SW1', 'SW2']
    services = ['Vlan', 'VPLS', 'Trunk']
    #print plugin.list_services_by_devices(services, devices)
    devices_ports={"R1": "FastEthernet0-0",
        "R2": "Fastethernet0-1"}
    print plugin.discover_all_services("R1")
    #isolation.create_service_instance("VPLS", "59", devices_ports)
    #isolation.create_service_instance("trunk-allow", "60", devices_ports)
    #isolation.create_service_instance("trunk-allow", "70", devices_ports)
    #plugin.remove_service("R4" ,"R4-trunk-allow-59" )
    #plugin.remove_service("R2" ,"R2-VPLS-59" )
    #plugin.remove_service("R2" ,"R2-trunk-allow-59" )
    #plugin.remove_service("R1" ,"R1-trunk-allow-59" )
    #plugin.remove_service("R3" ,"R3-trunk-allow-59" )
    #plugin.deploy_service("R3" ,"R3-trunk-allow-70" )
    #isolation.create_empty_service_instance("VPLS", "VPLS30")
    #isolation.create_empty_service_instance("Trunking", "Trunk")
    #plugin.deploy_service("R2" ,"R2-Trunk" )
    #plugin.deploy_service("R+1" ,"Trunk" )
    #plugin.remove_service("R3" ,"R3-trunk-allow-70" )
    #plugin.deploy_service("R1" ,"VPLS30" )
    #plugin.remove_service("R1" ,"VPLS30")
    #plugin.remove_service("R1" ,"Vlan30")
    #isolation.list_services_by_domain("L2")

    #isolation.create_service_instance("Vlan", "59", devices_ports)
    #isolation.create_empty_service_instance("VPLS", "VPLS30")
    #isolation.create_empty_service_instance("Trunking", "Trunk")
    # Instance service name:
    # device-service-instance
    # ex: R2-VPLS-32
    #plugin.deploy_service("R2" ,"R2-Trunk" )
    #plugin.deploy_service("R1" ,"Trunk" )
    #plugin.remove_service("R1" ,"Trunk" )
    #plugin.deploy_service("R1" ,"VPLS30" )
    #plugin.remove_service("R1" ,"VPLS30")
    #plugin.remove_service("R1" ,"Vlan30")
    

    #plugin.deploy_service("R1" ,"Trunk"  )
    #plugin.remove_service("R1" ,"Trunk" )
if __name__ == "__main__":
    main()
