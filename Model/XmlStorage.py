import xml.etree.ElementTree as ET
from io import StringIO
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
from typing import Type, List


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
    
    
    
# def get_actor_data(xml_doc, output=False):
#     return xml_doc.from_xml(ActorData, output)


def get_actor_data(xml_doc, output=False):
    return from_xml(xml_doc, "ActorData", "Output/", output)