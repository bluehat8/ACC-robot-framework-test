import sys
import xml.etree.ElementTree as ET
from io import StringIO
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
from typing import TypeVar, Type, List
import Person
import inspect



T = TypeVar('T')


def to_xml(obj):
    root = ET.Element(obj.__class__.__name__)
    for k, v in vars(obj).items():
        child = ET.Element(k)
        child.text = str(v)
        root.append(child)
    return ET.tostring(root, encoding='unicode')



def from_xml(xml_doc: Element, include_output: bool = False) -> List:
    xml_node = xml_doc.find(f"./body{'Output/' if include_output else ''}ArrayOf{Type.__name__}")
    if xml_node is not None:
        obj = ET.fromstring(xml_node.text)
        return [Type.from_xml(x) for x in obj.findall(Type.__name__)]
    else:
        return []
    


    

def list_to_xml(obj_list):
    root = ET.Element('ArrayOf{}'.format(obj_list[0].__class__.__name__))
    for obj in obj_list:
        obj_xml = ET.Element(obj.__class__.__name__)
        for k, v in vars(obj).items():
            child = ET.Element(k)
            child.text = str(v)
            obj_xml.append(child)
        root.append(obj_xml)
    return ET.tostring(root, encoding='unicode')   



# def from_xml_3(xml_str: str, obj_list, attributes):
#     root = ET.fromstring(xml_str)
#     person_list = []
#     for person in root.findall(obj_list.__name__):
#         name = person.find('name').text
#         age = int(person.find('age').text)
#         person_list.append(Person.Person(name, age))
#     return person_list
    

# def get_actor_data(xml_doc, output=False):
#     return from_xml(xml_doc, "ActorData", "Output/", output)



def from_xml_4(xml_str: str, class_type:Type, attributes):
    root = ET.fromstring(xml_str)
    object_list = []
    for obj in root.findall(class_type.__name__):
        values = []
        for attribute in attributes:
            value = obj.find(attribute).text
            values.append(value)
        object_instance = class_type(*values)
        object_list.append(object_instance)
    return object_list
    
