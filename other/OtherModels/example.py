import xml.etree.ElementTree as ET
from io import StringIO

def to_xml(obj):
    root = ET.Element(obj.__class__.__name__)
    for k, v in vars(obj).items():
        child = ET.Element(k)
        child.text = str(v)
        root.append(child)
    return ET.tostring(root, encoding='unicode')

# Ejemplo de uso
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 30)
xml_str = to_xml(p)
print(xml_str)