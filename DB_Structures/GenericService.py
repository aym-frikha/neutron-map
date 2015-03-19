# ./GenericService.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2015-01-28 09:55:30.763851 by PyXB version 1.2.4 using Python 2.7.6.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:b424cfae-a6fd-11e4-affa-525400f4d787')

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
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 49, 12)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.n11 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='11', tag='n11')
STD_ANON.n01 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='01', tag='n01')
STD_ANON.n0N = STD_ANON._CF_enumeration.addEnumeration(unicode_value='0N', tag='n0N')
STD_ANON.n1N = STD_ANON._CF_enumeration.addEnumeration(unicode_value='1N', tag='n1N')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 4, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Description'), 'Description', '__AbsentNamespace0_CTD_ANON_Description', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 6, 16), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element Transactional uses Python identifier Transactional
    __Transactional = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Transactional'), 'Transactional', '__AbsentNamespace0_CTD_ANON_Transactional', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 7, 16), )

    
    Transactional = property(__Transactional.value, __Transactional.set, None, None)

    
    # Element Priority uses Python identifier Priority
    __Priority = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Priority'), 'Priority', '__AbsentNamespace0_CTD_ANON_Priority', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 8, 16), )

    
    Priority = property(__Priority.value, __Priority.set, None, None)

    
    # Element Domain uses Python identifier Domain
    __Domain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Domain'), 'Domain', '__AbsentNamespace0_CTD_ANON_Domain', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 9, 16), )

    
    Domain = property(__Domain.value, __Domain.set, None, None)

    
    # Element ServiceTree uses Python identifier ServiceTree
    __ServiceTree = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ServiceTree'), 'ServiceTree', '__AbsentNamespace0_CTD_ANON_ServiceTree', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 10, 16), )

    
    ServiceTree = property(__ServiceTree.value, __ServiceTree.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 18, 12)
    __name._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 18, 12)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __Description.name() : __Description,
        __Transactional.name() : __Transactional,
        __Priority.name() : __Priority,
        __Domain.name() : __Domain,
        __ServiceTree.name() : __ServiceTree
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
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 11, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Node uses Python identifier Node
    __Node = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Node'), 'Node', '__AbsentNamespace0_CTD_ANON__Node', True, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 13, 28), )

    
    Node = property(__Node.value, __Node.set, None, None)

    _ElementMap.update({
        __Node.name() : __Node
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 24, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'href'), 'href', '__AbsentNamespace0_CTD_ANON_2_href', pyxb.binding.datatypes.string)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 25, 20)
    __href._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 25, 20)
    
    href = property(__href.value, __href.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __href.name() : __href
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 29, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Node uses Python identifier Node
    __Node = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Node'), 'Node', '__AbsentNamespace0_CTD_ANON_3_Node', True, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 31, 24), )

    
    Node = property(__Node.value, __Node.set, None, None)

    _ElementMap.update({
        __Node.name() : __Node
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 36, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Node uses Python identifier Node
    __Node = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Node'), 'Node', '__AbsentNamespace0_CTD_ANON_4_Node', True, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 38, 24), )

    
    Node = property(__Node.value, __Node.set, None, None)

    _ElementMap.update({
        __Node.name() : __Node
    })
    _AttributeMap.update({
        
    })



# Complex type GenNode with content type ELEMENT_ONLY
class GenNode (pyxb.binding.basis.complexTypeDefinition):
    """Complex type GenNode with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GenNode')
    _XSDLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 21, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element BaseParent uses Python identifier BaseParent
    __BaseParent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BaseParent'), 'BaseParent', '__AbsentNamespace0_GenNode_BaseParent', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 23, 12), )

    
    BaseParent = property(__BaseParent.value, __BaseParent.set, None, None)

    
    # Element Parameters uses Python identifier Parameters
    __Parameters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Parameters'), 'Parameters', '__AbsentNamespace0_GenNode_Parameters', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 28, 12), )

    
    Parameters = property(__Parameters.value, __Parameters.set, None, None)

    
    # Element Children uses Python identifier Children
    __Children = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Children'), 'Children', '__AbsentNamespace0_GenNode_Children', False, pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 35, 12), )

    
    Children = property(__Children.value, __Children.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_GenNode_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 43, 8)
    __name._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 43, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute CimRef uses Python identifier CimRef
    __CimRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'CimRef'), 'CimRef', '__AbsentNamespace0_GenNode_CimRef', pyxb.binding.datatypes.string, unicode_default='null')
    __CimRef._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 44, 8)
    __CimRef._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 44, 8)
    
    CimRef = property(__CimRef.value, __CimRef.set, None, None)

    
    # Attribute known uses Python identifier known
    __known = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'known'), 'known', '__AbsentNamespace0_GenNode_known', pyxb.binding.datatypes.boolean, unicode_default='true')
    __known._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 45, 8)
    __known._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 45, 8)
    
    known = property(__known.value, __known.set, None, None)

    
    # Attribute parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'parameter'), 'parameter', '__AbsentNamespace0_GenNode_parameter', pyxb.binding.datatypes.boolean, unicode_default='false')
    __parameter._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 46, 8)
    __parameter._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 46, 8)
    
    parameter = property(__parameter.value, __parameter.set, None, None)

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uid'), 'uid', '__AbsentNamespace0_GenNode_uid', pyxb.binding.datatypes.long, unicode_default='0')
    __uid._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 47, 8)
    __uid._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 47, 8)
    
    uid = property(__uid.value, __uid.set, None, None)

    
    # Attribute cardinality uses Python identifier cardinality
    __cardinality = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cardinality'), 'cardinality', '__AbsentNamespace0_GenNode_cardinality', STD_ANON)
    __cardinality._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 48, 8)
    __cardinality._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 48, 8)
    
    cardinality = property(__cardinality.value, __cardinality.set, None, None)

    
    # Attribute shadow uses Python identifier shadow
    __shadow = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shadow'), 'shadow', '__AbsentNamespace0_GenNode_shadow', pyxb.binding.datatypes.boolean, unicode_default='false')
    __shadow._DeclarationLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 58, 8)
    __shadow._UseLocation = pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 58, 8)
    
    shadow = property(__shadow.value, __shadow.set, None, None)

    _ElementMap.update({
        __BaseParent.name() : __BaseParent,
        __Parameters.name() : __Parameters,
        __Children.name() : __Children
    })
    _AttributeMap.update({
        __name.name() : __name,
        __CimRef.name() : __CimRef,
        __known.name() : __known,
        __parameter.name() : __parameter,
        __uid.name() : __uid,
        __cardinality.name() : __cardinality,
        __shadow.name() : __shadow
    })
Namespace.addCategoryObject('typeBinding', 'GenNode', GenNode)


GenericService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GenericService'), CTD_ANON, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 3, 4))
Namespace.addCategoryObject('elementBinding', GenericService.name().localName(), GenericService)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Description'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 6, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Transactional'), pyxb.binding.datatypes.boolean, scope=CTD_ANON, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 7, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Priority'), pyxb.binding.datatypes.integer, scope=CTD_ANON, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 8, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Domain'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 9, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ServiceTree'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 10, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'Description')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 6, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'Transactional')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 7, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'Priority')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 8, 16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'Domain')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 9, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'ServiceTree')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 10, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Node'), GenNode, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 13, 28)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'Node')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 13, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Node'), GenNode, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 31, 24)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'Node')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 31, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_2()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Node'), GenNode, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 38, 24)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'Node')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 38, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_3()




GenNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BaseParent'), CTD_ANON_2, nillable=pyxb.binding.datatypes.boolean(1), scope=GenNode, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 23, 12)))

GenNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Parameters'), CTD_ANON_3, scope=GenNode, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 28, 12)))

GenNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Children'), CTD_ANON_4, scope=GenNode, location=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 35, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 23, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 28, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 35, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GenNode._UseForTag(pyxb.namespace.ExpandedName(None, 'BaseParent')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 23, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GenNode._UseForTag(pyxb.namespace.ExpandedName(None, 'Parameters')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 28, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(GenNode._UseForTag(pyxb.namespace.ExpandedName(None, 'Children')), pyxb.utils.utility.Location('/opt/stack/neutron/neutron/plugins/map/ValidMakerDB/Schema/GenericService.xsd', 35, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GenNode._Automaton = _BuildAutomaton_4()

