import xml.etree.ElementTree as ET
from io import StringIO
import xml.etree.ElementTree as ET
from typing import TypeVar, Type

T = TypeVar('T')


def to_xml(obj):
    root = ET.Element(obj.__class__.__name__)
    for k, v in vars(obj).items():
        child = ET.Element(k)
        child.text = str(v)
        root.append(child)
    return ET.tostring(root, encoding='unicode')

def xml_to_str(path):
    arbol=ET.parse(path)
    root = arbol.getroot()

    return ET.tostring(root, encoding='unicode', method='xml')


def list_to_xml(obj_list):
    root = ET.Element('ArrayOf{}'.format(obj_list[0].__class__.__name__))
    for obj in obj_list:
        obj_xml = ET.Element(obj.__class__.__name__)
        for k, v in vars(obj).items():
            child = ET.Element(k)
            child.text = str(v)
            obj_xml.append(child)
            child.tail="\n"
        root.append(obj_xml)
        obj_xml.tail="\n"
    return ET.tostring(root, encoding='unicode', xml_declaration=True)   


def from_xml_5(xml_str: str, class_type: Type, attributes, include_output: bool = False):
    root = ET.fromstring(xml_str)
    obj_list = []
    # Si se incluye la salida, se busca el elemento "Output" en el árbol XML
    # y se utiliza como el elemento raíz en lugar del elemento "ArrayOf<T>"
    if include_output:
        root = root.find("Output")

    # Buscar el elemento que contiene la lista de objetos
    elements = root.findall(f".//{class_type.__name__}")

    # Recorrer todos los elementos y crear instancias de la clase
    for elem in elements:
        values = [elem.find(attr).text for attr in attributes]
        obj = class_type(*values)
        obj_list.append(obj)

    return obj_list


def create_xml(xml_str, path):
    with open(path, 'w', encoding="utf-8") as f:
        f.write(xml_str)







# def from_xml(xml_doc: Element, include_output: bool = False) -> List:
#     xml_node = xml_doc.find(f"./body{'Output/' if include_output else ''}ArrayOf{Type.__name__}")
#     if xml_node is not None:
#         obj = ET.fromstring(xml_node.text)
#         return [Type.from_xml(x) for x in obj.findall(Type.__name__)]
#     else:
#         return []
    

# def get_actor_data(xml_doc, output=False):
#     return from_xml(xml_doc, "ActorData", "Output/", output)


# def from_xml_4(xml_str: str, class_type:Type, attributes):
#     root = ET.fromstring(xml_str)
#     object_list = []
#     for obj in root.findall(class_type.__name__):
#         values = []
#         for attribute in attributes:
#             value = obj.find(attribute).text
#             values.append(value)
#         object_instance = class_type(*values)
#         object_list.append(object_instance)
#     return object_list

