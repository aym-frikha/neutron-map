# ./OSreference.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-12-11 17:22:02.391620 by PyXB version 1.2.4 using Python 3.2.3.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:215f7f96-8184-11e4-9551-0025110f1de8')

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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 4, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Description'), 'Description', '__AbsentNamespace0_CTD_ANON_Description', False, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 6, 16), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element OSVersions uses Python identifier OSVersions
    __OSVersions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'OSVersions'), 'OSVersions', '__AbsentNamespace0_CTD_ANON_OSVersions', False, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 7, 16), )

    
    OSVersions = property(__OSVersions.value, __OSVersions.set, None, None)

    
    # Element CommandList uses Python identifier CommandList
    __CommandList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CommandList'), 'CommandList', '__AbsentNamespace0_CTD_ANON_CommandList', False, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 20, 16), )

    
    CommandList = property(__CommandList.value, __CommandList.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 46, 12)
    __name._UseLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 46, 12)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __Description.name() : __Description,
        __OSVersions.name() : __OSVersions,
        __CommandList.name() : __CommandList
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
    _XSDLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 8, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element OSversion uses Python identifier OSversion
    __OSversion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'OSversion'), 'OSversion', '__AbsentNamespace0_CTD_ANON__OSversion', True, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 10, 28), )

    
    OSversion = property(__OSversion.value, __OSversion.set, None, None)

    
    # Attribute mode uses Python identifier mode
    __mode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mode'), 'mode', '__AbsentNamespace0_CTD_ANON__mode', pyxb.binding.datatypes.string)
    __mode._DeclarationLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 16, 24)
    __mode._UseLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 16, 24)
    
    mode = property(__mode.value, __mode.set, None, None)

    _ElementMap.update({
        __OSversion.name() : __OSversion
    })
    _AttributeMap.update({
        __mode.name() : __mode
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 11, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_2_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 12, 36)
    __name._UseLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 12, 36)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 21, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Command uses Python identifier Command
    __Command = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Command'), 'Command', '__AbsentNamespace0_CTD_ANON_3_Command', True, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 23, 28), )

    
    Command = property(__Command.value, __Command.set, None, None)

    _ElementMap.update({
        __Command.name() : __Command
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
    _XSDLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 24, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Syntax uses Python identifier Syntax
    __Syntax = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Syntax'), 'Syntax', '__AbsentNamespace0_CTD_ANON_4_Syntax', True, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 26, 40), )

    
    Syntax = property(__Syntax.value, __Syntax.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_4_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 36, 36)
    __name._UseLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 36, 36)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_4_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 37, 36)
    __type._UseLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 37, 36)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute mode uses Python identifier mode
    __mode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mode'), 'mode', '__AbsentNamespace0_CTD_ANON_4_mode', pyxb.binding.datatypes.string)
    __mode._DeclarationLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 38, 36)
    __mode._UseLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 38, 36)
    
    mode = property(__mode.value, __mode.set, None, None)

    
    # Attribute negated uses Python identifier negated
    __negated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'negated'), 'negated', '__AbsentNamespace0_CTD_ANON_4_negated', pyxb.binding.datatypes.string)
    __negated._DeclarationLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 39, 36)
    __negated._UseLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 39, 36)
    
    negated = property(__negated.value, __negated.set, None, None)

    _ElementMap.update({
        __Syntax.name() : __Syntax
    })
    _AttributeMap.update({
        __name.name() : __name,
        __type.name() : __type,
        __mode.name() : __mode,
        __negated.name() : __negated
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 27, 44)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_CTD_ANON_5_version', pyxb.binding.datatypes.string)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 30, 50)
    __version._UseLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 30, 50)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __version.name() : __version
    })



OSReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OSReference'), CTD_ANON, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 3, 4))
Namespace.addCategoryObject('elementBinding', OSReference.name().localName(), OSReference)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Description'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 6, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'OSVersions'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 7, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CommandList'), CTD_ANON_3, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 20, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'Description')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 6, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'OSVersions')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 7, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'CommandList')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 20, 16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'OSversion'), CTD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 10, 28)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'OSversion')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 10, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Command'), CTD_ANON_4, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 23, 28)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'Command')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 23, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_2()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Syntax'), CTD_ANON_5, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 26, 40)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'Syntax')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/OSreference.xsd', 26, 40))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_3()

