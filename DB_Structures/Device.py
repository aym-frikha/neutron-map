# ./Device.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2015-01-28 12:14:34.048516 by PyXB version 1.2.4 using Python 2.7.6.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:211e683c-a711-11e4-a47d-525400f4d787')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 57, 36)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.Internal = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Internal', tag='Internal')
STD_ANON.External = STD_ANON._CF_enumeration.addEnumeration(unicode_value='External', tag='External')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 106, 12)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.n11 = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='11', tag='n11')
STD_ANON_.n01 = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='01', tag='n01')
STD_ANON_.n0N = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='0N', tag='n0N')
STD_ANON_.n1N = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='1N', tag='n1N')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 4, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Description'), 'Description', '__AbsentNamespace0_CTD_ANON_Description', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 6, 16), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element Properties uses Python identifier Properties
    __Properties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Properties'), 'Properties', '__AbsentNamespace0_CTD_ANON_Properties', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 7, 16), )

    
    Properties = property(__Properties.value, __Properties.set, None, None)

    
    # Element Services uses Python identifier Services
    __Services = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Services'), 'Services', '__AbsentNamespace0_CTD_ANON_Services', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 17, 16), )

    
    Services = property(__Services.value, __Services.set, None, None)

    
    # Element ConfigTree uses Python identifier ConfigTree
    __ConfigTree = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ConfigTree'), 'ConfigTree', '__AbsentNamespace0_CTD_ANON_ConfigTree', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 28, 16), )

    
    ConfigTree = property(__ConfigTree.value, __ConfigTree.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_name', pyxb.binding.datatypes.anySimpleType)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 36, 12)
    __name._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 36, 12)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __Description.name() : __Description,
        __Properties.name() : __Properties,
        __Services.name() : __Services,
        __ConfigTree.name() : __ConfigTree
    })
    _AttributeMap.update({
        __name.name() : __name
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 8, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element IOSVersion uses Python identifier IOSVersion
    __IOSVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'IOSVersion'), 'IOSVersion', '__AbsentNamespace0_CTD_ANON__IOSVersion', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 10, 28), )

    
    IOSVersion = property(__IOSVersion.value, __IOSVersion.set, None, None)

    
    # Element EquipmentType uses Python identifier EquipmentType
    __EquipmentType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EquipmentType'), 'EquipmentType', '__AbsentNamespace0_CTD_ANON__EquipmentType', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 12, 28), )

    
    EquipmentType = property(__EquipmentType.value, __EquipmentType.set, None, None)

    _ElementMap.update({
        __IOSVersion.name() : __IOSVersion,
        __EquipmentType.name() : __EquipmentType
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 18, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Service uses Python identifier Service
    __Service = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Service'), 'Service', '__AbsentNamespace0_CTD_ANON_2_Service', True, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 20, 28), )

    
    Service = property(__Service.value, __Service.set, None, None)

    _ElementMap.update({
        __Service.name() : __Service
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 21, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'href'), 'href', '__AbsentNamespace0_CTD_ANON_3_href', pyxb.binding.datatypes.string, unicode_default='null')
    __href._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 22, 36)
    __href._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 22, 36)
    
    href = property(__href.value, __href.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __href.name() : __href
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 29, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Node uses Python identifier Node
    __Node = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Node'), 'Node', '__AbsentNamespace0_CTD_ANON_4_Node', True, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 31, 28), )

    
    Node = property(__Node.value, __Node.set, None, None)

    _ElementMap.update({
        __Node.name() : __Node
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 42, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'href'), 'href', '__AbsentNamespace0_CTD_ANON_5_href', pyxb.binding.datatypes.string)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 43, 20)
    __href._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 43, 20)
    
    href = property(__href.value, __href.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __href.name() : __href
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 48, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Modification uses Python identifier Modification
    __Modification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Modification'), 'Modification', '__AbsentNamespace0_CTD_ANON_6_Modification', True, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 50, 24), )

    
    Modification = property(__Modification.value, __Modification.set, None, None)

    _ElementMap.update({
        __Modification.name() : __Modification
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 70, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element RefNode uses Python identifier RefNode
    __RefNode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RefNode'), 'RefNode', '__AbsentNamespace0_CTD_ANON_7_RefNode', True, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 72, 24), )

    
    RefNode = property(__RefNode.value, __RefNode.set, None, None)

    _ElementMap.update({
        __RefNode.name() : __RefNode
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 73, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'href'), 'href', '__AbsentNamespace0_CTD_ANON_8_href', pyxb.binding.datatypes.string)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 74, 32)
    __href._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 74, 32)
    
    href = property(__href.value, __href.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __href.name() : __href
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 81, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Node uses Python identifier Node
    __Node = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Node'), 'Node', '__AbsentNamespace0_CTD_ANON_9_Node', True, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 83, 24), )

    
    Node = property(__Node.value, __Node.set, None, None)

    _ElementMap.update({
        __Node.name() : __Node
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 88, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Node uses Python identifier Node
    __Node = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Node'), 'Node', '__AbsentNamespace0_CTD_ANON_10_Node', True, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 90, 24), )

    
    Node = property(__Node.value, __Node.set, None, None)

    _ElementMap.update({
        __Node.name() : __Node
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 95, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'href'), 'href', '__AbsentNamespace0_CTD_ANON_11_href', pyxb.binding.datatypes.string)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 96, 20)
    __href._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 96, 20)
    
    href = property(__href.value, __href.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __href.name() : __href
    })



# Complex type DevNode with content type ELEMENT_ONLY
class DevNode (pyxb.binding.basis.complexTypeDefinition):
    """Complex type DevNode with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DevNode')
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 39, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element BaseParent uses Python identifier BaseParent
    __BaseParent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BaseParent'), 'BaseParent', '__AbsentNamespace0_DevNode_BaseParent', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 41, 12), )

    
    BaseParent = property(__BaseParent.value, __BaseParent.set, None, None)

    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Value'), 'Value', '__AbsentNamespace0_DevNode_Value', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 46, 12), )

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Element Modifications uses Python identifier Modifications
    __Modifications = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Modifications'), 'Modifications', '__AbsentNamespace0_DevNode_Modifications', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 47, 12), )

    
    Modifications = property(__Modifications.value, __Modifications.set, None, None)

    
    # Element ReferenceList uses Python identifier ReferenceList
    __ReferenceList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ReferenceList'), 'ReferenceList', '__AbsentNamespace0_DevNode_ReferenceList', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 69, 12), )

    
    ReferenceList = property(__ReferenceList.value, __ReferenceList.set, None, None)

    
    # Element Parameters uses Python identifier Parameters
    __Parameters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Parameters'), 'Parameters', '__AbsentNamespace0_DevNode_Parameters', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 80, 12), )

    
    Parameters = property(__Parameters.value, __Parameters.set, None, None)

    
    # Element Children uses Python identifier Children
    __Children = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Children'), 'Children', '__AbsentNamespace0_DevNode_Children', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 87, 12), )

    
    Children = property(__Children.value, __Children.set, None, None)

    
    # Element CimRef uses Python identifier CimRef
    __CimRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CimRef'), 'CimRef', '__AbsentNamespace0_DevNode_CimRef', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 94, 12), )

    
    CimRef = property(__CimRef.value, __CimRef.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_DevNode_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 100, 8)
    __name._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 100, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute CimRef uses Python identifier CimRef_
    __CimRef_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'CimRef'), 'CimRef_', '__AbsentNamespace0_DevNode_CimRef_', pyxb.binding.datatypes.string, unicode_default='null')
    __CimRef_._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 101, 8)
    __CimRef_._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 101, 8)
    
    CimRef_ = property(__CimRef_.value, __CimRef_.set, None, None)

    
    # Attribute known uses Python identifier known
    __known = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'known'), 'known', '__AbsentNamespace0_DevNode_known', pyxb.binding.datatypes.boolean, unicode_default='true')
    __known._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 102, 8)
    __known._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 102, 8)
    
    known = property(__known.value, __known.set, None, None)

    
    # Attribute parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'parameter'), 'parameter', '__AbsentNamespace0_DevNode_parameter', pyxb.binding.datatypes.boolean, unicode_default='false')
    __parameter._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 103, 8)
    __parameter._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 103, 8)
    
    parameter = property(__parameter.value, __parameter.set, None, None)

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uid'), 'uid', '__AbsentNamespace0_DevNode_uid', pyxb.binding.datatypes.long, unicode_default='0')
    __uid._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 104, 8)
    __uid._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 104, 8)
    
    uid = property(__uid.value, __uid.set, None, None)

    
    # Attribute cardinality uses Python identifier cardinality
    __cardinality = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cardinality'), 'cardinality', '__AbsentNamespace0_DevNode_cardinality', STD_ANON_)
    __cardinality._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 105, 8)
    __cardinality._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 105, 8)
    
    cardinality = property(__cardinality.value, __cardinality.set, None, None)

    
    # Attribute shadow uses Python identifier shadow
    __shadow = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shadow'), 'shadow', '__AbsentNamespace0_DevNode_shadow', pyxb.binding.datatypes.boolean, unicode_default='false')
    __shadow._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 115, 8)
    __shadow._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 115, 8)
    
    shadow = property(__shadow.value, __shadow.set, None, None)

    _ElementMap.update({
        __BaseParent.name() : __BaseParent,
        __Value.name() : __Value,
        __Modifications.name() : __Modifications,
        __ReferenceList.name() : __ReferenceList,
        __Parameters.name() : __Parameters,
        __Children.name() : __Children,
        __CimRef.name() : __CimRef
    })
    _AttributeMap.update({
        __name.name() : __name,
        __CimRef_.name() : __CimRef_,
        __known.name() : __known,
        __parameter.name() : __parameter,
        __uid.name() : __uid,
        __cardinality.name() : __cardinality,
        __shadow.name() : __shadow
    })
Namespace.addCategoryObject('typeBinding', 'DevNode', DevNode)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 51, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element TimeStamp uses Python identifier TimeStamp
    __TimeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TimeStamp'), 'TimeStamp', '__AbsentNamespace0_CTD_ANON_12_TimeStamp', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 53, 36), )

    
    TimeStamp = property(__TimeStamp.value, __TimeStamp.set, None, None)

    
    # Element OldValue uses Python identifier OldValue
    __OldValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'OldValue'), 'OldValue', '__AbsentNamespace0_CTD_ANON_12_OldValue', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 54, 36), )

    
    OldValue = property(__OldValue.value, __OldValue.set, None, None)

    
    # Attribute source uses Python identifier source
    __source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'source'), 'source', '__AbsentNamespace0_CTD_ANON_12_source', STD_ANON)
    __source._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 56, 32)
    __source._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 56, 32)
    
    source = property(__source.value, __source.set, None, None)

    _ElementMap.update({
        __TimeStamp.name() : __TimeStamp,
        __OldValue.name() : __OldValue
    })
    _AttributeMap.update({
        __source.name() : __source
    })



Device = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Device'), CTD_ANON, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 3, 4))
Namespace.addCategoryObject('elementBinding', Device.name().localName(), Device)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Description'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 6, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Properties'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 7, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Services'), CTD_ANON_2, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 17, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ConfigTree'), CTD_ANON_4, scope=CTD_ANON, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 28, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'Description')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 6, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'Properties')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 7, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'Services')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 17, 16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'ConfigTree')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 28, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'IOSVersion'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 10, 28), unicode_default='null'))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EquipmentType'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 12, 28), unicode_default='null'))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'IOSVersion')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 10, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'EquipmentType')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 12, 28))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Service'), CTD_ANON_3, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 20, 28)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 20, 28))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'Service')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 20, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Node'), DevNode, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 31, 28)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'Node')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 31, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_3()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Modification'), CTD_ANON_12, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 50, 24)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 50, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, 'Modification')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 50, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_4()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RefNode'), CTD_ANON_8, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 72, 24)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 72, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'RefNode')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 72, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_5()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Node'), DevNode, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 83, 24)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'Node')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 83, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_6()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Node'), DevNode, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 90, 24)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'Node')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 90, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_7()




DevNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BaseParent'), CTD_ANON_5, nillable=pyxb.binding.datatypes.boolean(1), scope=DevNode, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 41, 12)))

DevNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Value'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), scope=DevNode, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 46, 12)))

DevNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Modifications'), CTD_ANON_6, nillable=pyxb.binding.datatypes.boolean(1), scope=DevNode, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 47, 12)))

DevNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ReferenceList'), CTD_ANON_7, scope=DevNode, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 69, 12)))

DevNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Parameters'), CTD_ANON_9, scope=DevNode, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 80, 12)))

DevNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Children'), CTD_ANON_10, scope=DevNode, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 87, 12)))

DevNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CimRef'), CTD_ANON_11, scope=DevNode, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 94, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 41, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 46, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 47, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 69, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 80, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 87, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 94, 12))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DevNode._UseForTag(pyxb.namespace.ExpandedName(None, 'BaseParent')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 41, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DevNode._UseForTag(pyxb.namespace.ExpandedName(None, 'Value')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 46, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DevNode._UseForTag(pyxb.namespace.ExpandedName(None, 'Modifications')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 47, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DevNode._UseForTag(pyxb.namespace.ExpandedName(None, 'ReferenceList')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 69, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(DevNode._UseForTag(pyxb.namespace.ExpandedName(None, 'Parameters')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 80, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(DevNode._UseForTag(pyxb.namespace.ExpandedName(None, 'Children')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 87, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(DevNode._UseForTag(pyxb.namespace.ExpandedName(None, 'CimRef')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 94, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DevNode._Automaton = _BuildAutomaton_8()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TimeStamp'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 53, 36)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'OldValue'), pyxb.binding.datatypes.string, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 54, 36)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'TimeStamp')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 53, 36))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'OldValue')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/Device.xsd', 54, 36))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_9()

