# ./Rule.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-12-10 10:36:32.666126 by PyXB version 1.2.4 using Python 3.2.3.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:514f60b6-8082-11e4-9551-0025110f1de8')

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
    _XSDLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 4, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Description'), 'Description', '__AbsentNamespace0_CTD_ANON_Description', False, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 6, 16), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element Conditions uses Python identifier Conditions
    __Conditions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Conditions'), 'Conditions', '__AbsentNamespace0_CTD_ANON_Conditions', False, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 7, 16), )

    
    Conditions = property(__Conditions.value, __Conditions.set, None, None)

    
    # Element Actions uses Python identifier Actions
    __Actions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Actions'), 'Actions', '__AbsentNamespace0_CTD_ANON_Actions', False, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 15, 16), )

    
    Actions = property(__Actions.value, __Actions.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 24, 12)
    __name._UseLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 24, 12)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __Description.name() : __Description,
        __Conditions.name() : __Conditions,
        __Actions.name() : __Actions
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
    _XSDLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 8, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Condition uses Python identifier Condition
    __Condition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Condition'), 'Condition', '__AbsentNamespace0_CTD_ANON__Condition', True, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 10, 28), )

    
    Condition = property(__Condition.value, __Condition.set, None, None)

    _ElementMap.update({
        __Condition.name() : __Condition
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
    _XSDLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 16, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Action uses Python identifier Action
    __Action = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Action'), 'Action', '__AbsentNamespace0_CTD_ANON_2_Action', True, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 18, 28), )

    
    Action = property(__Action.value, __Action.set, None, None)

    _ElementMap.update({
        __Action.name() : __Action
    })
    _AttributeMap.update({
        
    })



# Complex type LogOperation with content type ELEMENT_ONLY
class LogOperation (pyxb.binding.basis.complexTypeDefinition):
    """Complex type LogOperation with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogOperation')
    _XSDLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 27, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element LogicalOp uses Python identifier LogicalOp
    __LogicalOp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LogicalOp'), 'LogicalOp', '__AbsentNamespace0_LogOperation_LogicalOp', False, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 29, 12), )

    
    LogicalOp = property(__LogicalOp.value, __LogicalOp.set, None, None)

    
    # Element Negated uses Python identifier Negated
    __Negated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Negated'), 'Negated', '__AbsentNamespace0_LogOperation_Negated', False, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 30, 12), )

    
    Negated = property(__Negated.value, __Negated.set, None, None)

    
    # Element Operation uses Python identifier Operation
    __Operation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Operation'), 'Operation', '__AbsentNamespace0_LogOperation_Operation', False, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 31, 12), )

    
    Operation = property(__Operation.value, __Operation.set, None, None)

    
    # Element LeftTree uses Python identifier LeftTree
    __LeftTree = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LeftTree'), 'LeftTree', '__AbsentNamespace0_LogOperation_LeftTree', False, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 32, 12), )

    
    LeftTree = property(__LeftTree.value, __LeftTree.set, None, None)

    
    # Element LeftOperand uses Python identifier LeftOperand
    __LeftOperand = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LeftOperand'), 'LeftOperand', '__AbsentNamespace0_LogOperation_LeftOperand', False, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 33, 12), )

    
    LeftOperand = property(__LeftOperand.value, __LeftOperand.set, None, None)

    
    # Element RightTree uses Python identifier RightTree
    __RightTree = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RightTree'), 'RightTree', '__AbsentNamespace0_LogOperation_RightTree', False, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 34, 12), )

    
    RightTree = property(__RightTree.value, __RightTree.set, None, None)

    
    # Element RightOperand uses Python identifier RightOperand
    __RightOperand = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RightOperand'), 'RightOperand', '__AbsentNamespace0_LogOperation_RightOperand', False, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 35, 12), )

    
    RightOperand = property(__RightOperand.value, __RightOperand.set, None, None)

    _ElementMap.update({
        __LogicalOp.name() : __LogicalOp,
        __Negated.name() : __Negated,
        __Operation.name() : __Operation,
        __LeftTree.name() : __LeftTree,
        __LeftOperand.name() : __LeftOperand,
        __RightTree.name() : __RightTree,
        __RightOperand.name() : __RightOperand
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'LogOperation', LogOperation)


# Complex type RuleNode with content type ELEMENT_ONLY
class RuleNode (pyxb.binding.basis.complexTypeDefinition):
    """Complex type RuleNode with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RuleNode')
    _XSDLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 38, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ServiceRef uses Python identifier ServiceRef
    __ServiceRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ServiceRef'), 'ServiceRef', '__AbsentNamespace0_RuleNode_ServiceRef', False, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 40, 12), )

    
    ServiceRef = property(__ServiceRef.value, __ServiceRef.set, None, None)

    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__AbsentNamespace0_RuleNode_Name', False, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 41, 12), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element GUID uses Python identifier GUID
    __GUID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'GUID'), 'GUID', '__AbsentNamespace0_RuleNode_GUID', False, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 42, 12), )

    
    GUID = property(__GUID.value, __GUID.set, None, None)

    _ElementMap.update({
        __ServiceRef.name() : __ServiceRef,
        __Name.name() : __Name,
        __GUID.name() : __GUID
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RuleNode', RuleNode)


# Complex type Operand with content type ELEMENT_ONLY
class Operand (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Operand with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Operand')
    _XSDLocation = pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 45, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Node uses Python identifier Node
    __Node = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Node'), 'Node', '__AbsentNamespace0_Operand_Node', False, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 47, 12), )

    
    Node = property(__Node.value, __Node.set, None, None)

    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Value'), 'Value', '__AbsentNamespace0_Operand_Value', False, pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 48, 12), )

    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        __Node.name() : __Node,
        __Value.name() : __Value
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Operand', Operand)


Rule = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Rule'), CTD_ANON, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 3, 4))
Namespace.addCategoryObject('elementBinding', Rule.name().localName(), Rule)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Description'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 6, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Conditions'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 7, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Actions'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 15, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'Description')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 6, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'Conditions')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 7, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'Actions')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 15, 16))
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




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Condition'), LogOperation, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 10, 28)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 10, 28))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'Condition')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 10, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Action'), LogOperation, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 18, 28)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 18, 28))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'Action')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 18, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




LogOperation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LogicalOp'), pyxb.binding.datatypes.string, scope=LogOperation, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 29, 12), unicode_default='NONE'))

LogOperation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Negated'), pyxb.binding.datatypes.boolean, scope=LogOperation, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 30, 12)))

LogOperation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Operation'), pyxb.binding.datatypes.string, scope=LogOperation, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 31, 12)))

LogOperation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LeftTree'), pyxb.binding.datatypes.integer, scope=LogOperation, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 32, 12)))

LogOperation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LeftOperand'), Operand, scope=LogOperation, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 33, 12)))

LogOperation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RightTree'), pyxb.binding.datatypes.integer, scope=LogOperation, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 34, 12)))

LogOperation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RightOperand'), Operand, scope=LogOperation, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 35, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LogOperation._UseForTag(pyxb.namespace.ExpandedName(None, 'LogicalOp')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 29, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LogOperation._UseForTag(pyxb.namespace.ExpandedName(None, 'Negated')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 30, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LogOperation._UseForTag(pyxb.namespace.ExpandedName(None, 'Operation')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 31, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LogOperation._UseForTag(pyxb.namespace.ExpandedName(None, 'LeftTree')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 32, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LogOperation._UseForTag(pyxb.namespace.ExpandedName(None, 'LeftOperand')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 33, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LogOperation._UseForTag(pyxb.namespace.ExpandedName(None, 'RightTree')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 34, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LogOperation._UseForTag(pyxb.namespace.ExpandedName(None, 'RightOperand')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 35, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LogOperation._Automaton = _BuildAutomaton_3()




RuleNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ServiceRef'), pyxb.binding.datatypes.string, scope=RuleNode, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 40, 12)))

RuleNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Name'), pyxb.binding.datatypes.string, scope=RuleNode, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 41, 12)))

RuleNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'GUID'), pyxb.binding.datatypes.long, scope=RuleNode, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 42, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RuleNode._UseForTag(pyxb.namespace.ExpandedName(None, 'ServiceRef')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 40, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RuleNode._UseForTag(pyxb.namespace.ExpandedName(None, 'Name')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 41, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RuleNode._UseForTag(pyxb.namespace.ExpandedName(None, 'GUID')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 42, 12))
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
RuleNode._Automaton = _BuildAutomaton_4()




Operand._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Node'), RuleNode, scope=Operand, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 47, 12)))

Operand._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Value'), pyxb.binding.datatypes.string, scope=Operand, location=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 48, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 47, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 48, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Operand._UseForTag(pyxb.namespace.ExpandedName(None, 'Node')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 47, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Operand._UseForTag(pyxb.namespace.ExpandedName(None, 'Value')), pyxb.utils.utility.Location('/home/aymen/dneutron/ValidMakerDB/Schema/Rule.xsd', 48, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Operand._Automaton = _BuildAutomaton_5()

