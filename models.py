__author__ = 'aymen'

import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.dialects.mysql import INTEGER as Integer
from neutron.db import model_base
from neutron.db import models_v2
from neutron.openstack.common import uuidutils
from neutron.plugins.map import constants as cst

STATUS = sa.Enum(cst.ACTIVE, cst.INACTIVE, name='status_types')


class TargetNetwork(model_base.BASEV2, models_v2.HasId):
    """Represent the global network. It includes virtual, physical
    networks and Generic services
    """
    __tablename__ = 'target_network'


class PhysicalNetwork(model_base.BASEV2, models_v2.HasId):
    """Represent the physical network. It represents all physical machines
     and links on the network. This element includes zero or more physical nodes.
    """
    __tablename__ = 'physical_network'

    name = sa.Column(sa.String(36), nullable=False)
    target_network = sa.Column(sa.String(36),
                               sa.ForeignKey('target_network.id',
                                             ondelete="SET NULL"))


class VirtualNetwork(model_base.BASEV2):
    """Represents a v2 neutron network."""

    __tablename__ = 'virtual_network'

    id = sa.Column(sa.String(36), sa.ForeignKey('networks.id',
                                                ondelete="CASCADE"),
                   nullable=False, primary_key=True)
    target_network = sa.Column(sa.String(36),
                               sa.ForeignKey('target_network.id',
                                             ondelete="SET NULL"))

    # network = orm.relationship(
    # models_v2.Network,
    #     backref=orm.backref("virtual_network",
    #                         lazy='joined', uselist=False,
    #                         cascade='delete'))


class GenericService(model_base.BASEV2, models_v2.HasId):
    """Is a Meta-CLI representation of network services. The administrator
     must analyse network services and identify their parameters.

     """
    __tablename__ = 'generic_service'

    name = sa.Column(sa.String(36), nullable=False)
    description = sa.Column(sa.String(255), nullable=True)
    target_network = sa.Column(sa.String(36),
                               sa.ForeignKey('target_network.id',
                                             ondelete="SET NULL"))
    config = sa.Column(sa.String(255), nullable=True)


class PhysicalLink(model_base.BASEV2, models_v2.HasId):
    """ Represents a network cable that connects two network interfaces. It can
        represent an ethernet cable or an internal link between a blade server
        and an internal switch.

    """
    __tablename__ = 'physical_link'

    name = sa.Column(sa.String(36), nullable=False)
    description = sa.Column(sa.String(255), nullable=True)
    cost = sa.Column(Integer(5), nullable=False)
    status = sa.Column(STATUS, default=cst.ACTIVE, nullable=False)
    physical_network = sa.Column(sa.String(36),
                                 sa.ForeignKey('physical_network.id',
                                               ondelete="SET NULL"))

    def __init__(self, name=None,
                 description=None, cost=None, status=None,
                 physical_network=None):
        # TODO, Without the initialisation of id parameter,
        # TODO, I have always 'None' value
        self.id = uuidutils.generate_uuid()
        self.description = description
        self.cost = cost
        self.name = name
        self.status = status
        self.physical_network = physical_network


class PhysicalInterface(model_base.BASEV2, models_v2.HasId):
    """It can be associated to a physical link and must belongs to a
    physical node. """
    __tablename__ = 'physical_interface'

    PhysicalInterfaceType = sa.Enum(cst.ETHERNET, cst.FAST_ETHERNET, cst.GIG_ETHERNET,
                                    name='physical_interface_type')
    name = sa.Column(sa.String(36), nullable=False)
    description = sa.Column(sa.String(255), nullable=True)
    type = sa.Column(PhysicalInterfaceType, nullable=True)
    status = sa.Column(STATUS, default=cst.ACTIVE, nullable=False)
    physical_link_id = sa.Column(sa.String(36),
                                 sa.ForeignKey('physical_link.id',
                                               ondelete="CASCADE"),
                                 nullable=True)
    virtual_link_id = sa.Column(sa.String(36),
                                sa.ForeignKey('virtual_link.id',
                                              ondelete="CASCADE"),
                                nullable=True)
    physical_node = sa.Column(sa.String(36),
                              sa.ForeignKey('physical_node.id',
                                            ondelete="SET NULL"))
    physical_interface_group = sa.Column(sa.String(36),
                                         sa.ForeignKey(
                                             'physical_interface_group.id',
                                             ondelete="SET NULL"),
                                         nullable=True)

    def __init__(self, name=None,
                 description=None, type=None,
                 status=None, physical_link_id=None, virtual_link_id=None,
                 physical_node=None, physical_interface_group=None):
        # TODO, Without the initialisation of id parameter,
        # TODO, I have always 'None' value
        self.id = uuidutils.generate_uuid()
        self.description = description
        self.type = type
        self.name = name
        self.physical_link_id = physical_link_id
        self.virtual_link_id = virtual_link_id
        self.physical_node = physical_node
        self.physical_interface_group = physical_interface_group
        self.status = status


class PhysicalInterfaceGroup(model_base.BASEV2, models_v2.HasId):
    """Is a set of interfaces on the same physical node. It can be a line card
       or a VDC.

    """
    __tablename__ = 'physical_interface_group'

    PhysicalInterfaceGroupType = sa.Enum(cst.LINE_CARD, cst.VDC,
                                         name='physical_interface_group_type')
    description = sa.Column(sa.String(255), nullable=True)
    type = sa.Column(PhysicalInterfaceGroupType,
                     default=cst.LINE_CARD, nullable=True)
    physical_node = sa.Column(sa.String(36),
                              sa.ForeignKey('physical_node.id',
                                            ondelete="SET NULL"))


class PhysicalNode(model_base.BASEV2, models_v2.HasId):
    """It can be a physical network equipment, storage or treatment. This node
    is associated with a physical network and may be associated with a group
    of physical nodes.

    """
    __tablename__ = 'physical_node'
    PhysicalNodeType = sa.Enum(cst.SWITCH, cst.STORAGE, cst.SERVER, cst.FIREWALL,
                               cst.ROUTER, cst.IDS, cst.IPS, name='physical_node_type')

    physical_network = sa.Column(sa.String(36),
                                 sa.ForeignKey('physical_network.id',
                                               ondelete="SET NULL"))
    name = sa.Column(sa.String(36), nullable=False)
    password = sa.Column(sa.String(36), nullable=False)
    login = sa.Column(sa.String(36), nullable=False)
    description = sa.Column(sa.String(255), nullable=True)
    type = sa.Column(PhysicalNodeType, nullable=False)
    equipment_model = sa.Column(sa.String(255), nullable=True)
    system_version = sa.Column(sa.String(255), nullable=True)
    address = sa.Column(sa.String(64), nullable=False)
    config = sa.Column(sa.String(255), nullable=True)
    status = sa.Column(STATUS, default=cst.ACTIVE, nullable=False)

    physical_node_group = sa.Column(sa.String(36),
                                    sa.ForeignKey('physical_node_group.id'),
                                    nullable=True)

    def __init__(self, id=None, name=None, password=None, login=None, description=None, type=None,
                 equipment_model=None, system_version=None, address=None,
                 config=None, status=None, physical_network=None,
                 physical_node_group=None):
        self.id = id
        self.description = description
        self.type = type
        self.name = name
        self.password = password
        self.login = login
        self.equipment_model = equipment_model
        self.system_version = system_version
        self.address = address
        self.config = config
        self.physical_network = physical_network
        self.status = status
        self.physical_node_group = physical_node_group


class PhysicalNodeGroup(model_base.BASEV2, models_v2.HasId):
    """Is a set of physical nodes. It can represent a chassis of a blade server,
       which contains several servers and multiple network devices.

    """
    __tablename__ = 'physical_node_group'

    PhysicalNodeGroupType = sa.Enum(cst.CHASSIS, name='physical_node_group_type')
    description = sa.Column(sa.String(255), nullable=True)
    type = sa.Column(PhysicalNodeGroupType, default=cst.CHASSIS, nullable=False)
    physical_network = sa.Column(sa.String(36),
                                 sa.ForeignKey('physical_network.id',
                                               ondelete="SET NULL"))
    # physical_nodes = orm.relationship(PhysicalNode,
    # backref=orm.backref("physical_node_group",
    # lazy="joined"))


class InstanceService(model_base.BASEV2, models_v2.HasId):
    """Is an instance of a generic service. It has specific attributes related
    on specific devices like interface names and ip addresses.
    """
    __tablename__ = 'instance_service'

    name = sa.Column(sa.String(36), nullable=False)
    description = sa.Column(sa.String(255), nullable=True)
    config = sa.Column(sa.String(255), nullable=True)
    physical_network = sa.Column(sa.String(36),
                                 sa.ForeignKey('physical_network.id',
                                               ondelete="SET NULL"))
    virtual_network = sa.Column(sa.String(36),
                                sa.ForeignKey('virtual_network.id',
                                              ondelete="SET NULL"))
    physical_node = sa.Column(sa.String(36), sa.ForeignKey("physical_node.id",
                                                           ondelete="SET NULL"))
    virtual_node = sa.Column(sa.String(36), sa.ForeignKey("virtual_node.id",
                                                          ondelete="SET NULL"))
    generic_service = sa.Column(sa.String(36),
                                sa.ForeignKey('generic_service.id',
                                              ondelete="SET NULL"))


class VirtualLink(model_base.BASEV2, models_v2.HasId):
    """Is used to connect two virtual interfaces. It may represent a link
       between a virtual machine and a virtual switch or between a Virtual
       Interface and a Physical Interface.

    """
    __tablename__ = 'virtual_link'

    name = sa.Column(sa.String(36), nullable=True)
    description = sa.Column(sa.String(255), nullable=True)
    status = sa.Column(STATUS, default=cst.ACTIVE, nullable=False)
    cost = sa.Column(sa.Integer, nullable=False)
    virtual_network = sa.Column(sa.String(36),
                                sa.ForeignKey('virtual_network.id',
                                              ondelete="SET NULL"))

    def __init__(self, name=None, description=None, status=None, cost=None,
                 virtual_network=None):
        self.name = name
        self.description = description
        self.status = status
        self.cost = cost
        self.virtual_network = virtual_network


class VirtualInterface(model_base.BASEV2, models_v2.HasId):
    """It is connected to another Virtual Interface or to a Physical Interface
       through a Virtual Link.
    """
    __tablename__ = 'virtual_interface'
    VirtualInterfaceType = sa.Enum(cst.VIRTIO, cst.E1000, cst.NE2KPCI, cst.PCNET,
                                   cst.RTL8139, cst.TUN, cst.TAP,
                                   name='virtual_interface_type')
    name = sa.Column(sa.String(36), nullable=True)
    description = sa.Column(sa.String(255), nullable=True)
    type = sa.Column(VirtualInterfaceType, nullable=True)
    status = sa.Column(STATUS, default=cst.ACTIVE, nullable=False)
    link_id = sa.Column(sa.String(36),
                        sa.ForeignKey('virtual_link.id',
                                      ondelete="CASCADE"), nullable=True)
    virtual_node = sa.Column(sa.String(36),
                             sa.ForeignKey('virtual_node.id',
                                           ondelete="SET NULL"))

    def __init__(self, id=None, name=None, description=None, type=None,
                 status=None,
                 link_id=None, virtual_node=None):
        self.id = id
        self.name = name
        self.description = description
        self.type = type
        self.status = status
        self.link_id = link_id
        self.virtual_node = virtual_node


class VirtualNode(model_base.BASEV2, models_v2.HasId):
    """Is a virtual device in the virtual network. It can be a virtual switch
      (OVS), a virtual bridge or a virtual machine.
    """
    __tablename__ = 'virtual_node'
    VirtualNodeType = sa.Enum(cst.VM, cst.VSWITCH, cst.VROUTER, cst.BRIDGE,
                              name='virtual_node_type')
    name = sa.Column(sa.String(36), nullable=True)
    description = sa.Column(sa.String(255), nullable=True)
    type = sa.Column(VirtualNodeType, nullable=False)
    config = sa.Column(sa.String(255), nullable=True)
    status = sa.Column(STATUS, default=cst.ACTIVE, nullable=False)
    virtual_node_group = sa.Column(sa.String(36),
                                   sa.ForeignKey('virtual_node_group.id'),
                                   nullable=True)
    virtual_network = sa.Column(sa.String(36),
                                sa.ForeignKey('virtual_network.id'),
                                nullable=False)

    def __init__(self, id=None, virtual_node_group=None, name=None,
                 description=None,
                 type=None, config=None, status=None, virtual_network=None):
        self.id = id
        self.name = name
        self.description = description
        self.type = type
        self.config = config
        self.status = status
        self.virtual_node_group = virtual_node_group
        self.virtual_network = virtual_network


class VirtualNodeGroup(model_base.BASEV2, models_v2.HasId):
    """Is a group of virtual nodes that belongs to the same physical node.
       The association between the Virtual Node Group and Physical Node is
       necessary for the mapping between virtual and physical networks.
    """
    __tablename__ = 'virtual_node_group'
    VirtualNodeGroupType = sa.Enum(cst.VSWITCH_GROUP, cst.VROUTER_GROUP, cst.BRIDGE_GROUP,
                                   name='virtual_node_group_type')
    description = sa.Column(sa.String(255), nullable=True)
    type = sa.Column(VirtualNodeGroupType, nullable=False)
    physical_node_attached = sa.Column(sa.String(36),
                                       sa.ForeignKey('physical_node.id'),
                                       nullable=False)

    virtual_network = sa.Column(sa.String(36),
                                sa.ForeignKey('virtual_network.id'),
                                nullable=False)

    def __init__(self, id=None, description=None,
                 type=None, physical_node_attached=None, virtual_network=None):
        self.id = id
        self.description = description
        self.type = type
        self.physical_node_attached = physical_node_attached
        self.virtual_network = virtual_network

        # virtual_nodes = orm.relationship(VirtualNode,
        # backref=orm.backref("virtual_node_group",
        #                                                      lazy="joined"))