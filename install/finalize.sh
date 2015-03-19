#!/bin/sh


#TODO: MUST BE RUNNED AS ROOOOOT!

STACK=/opt/stack
NEUTRON=$STACK/neutron/neutron/
ETC_NEUTRON=/etc/neutron
ETC_NOVA=/etc/nova
DEVSTACK=/home/stack/devstack

# Ask nova to take care of security groups
sed -e 's/security_group_api = quantum/security_group_api = nova/'\
    -i $ETC_NOVA/nova.conf

# Set MAP as neutron's plugin
sed -e 's/core_plugin = neutron.plugins.openvswitch.ovs_neutron_plugin.OVSNeutronPluginV2/core_plugin = neutron.plugins.map.dynamic_plugin.DynamicNeutronPlugin/'\
    -i $ETC_NEUTRON/neutron.conf

# Put MAP's configuration in /etc/
mkdir -p $ETC_NEUTRON/plugins/map/
cp example-config.ini $ETC_NEUTRON/plugins/map/map.ini

# Ask screen to use map's config when launched with 'rejoin stack'
sed -e "s|\(cd /opt/stack/neutron && python /usr/local/bin/neutron-server --config-file /etc/neutron/neutron.conf --config-file \).*\.ini|\1$ETC_NEUTRON/plugins/map/map.ini|"\
    -i $DEVSTACK/stack-screenrc

# Set up a data environement for MAP's data
mkdir -p $STACK/data/neutron/plugins/map/
mv network $STACK/data/neutron/plugins/map/
mv netconf $STACK/data/neutron/plugins/map/

# Install dependencies
sudo pip install pyxb
sudo git clone git://github.com/leopoul/ncclient
(cd ncclient && patch -p1 < ../dynamips_compat.patch && python setup.py install)

