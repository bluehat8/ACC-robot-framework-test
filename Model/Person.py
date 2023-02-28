import XmlStorage
import xml.etree.ElementTree as ET


# Ejemplo de uso
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    @classmethod
    def from_xml(cls, xml_element):
        name = xml_element.find("name").text
        age = int(xml_element.find("age").text)
        return cls(name, age)

    def to_xml(self):
        root = ET.Element("Person")
        name_el = ET.SubElement(root, "name")
        name_el.text = self.name
        age_el = ET.SubElement(root, "age")
        age_el.text = str(self.age)
        return ET.tostring(root, encoding="unicode")


p = Person("John", 30)
xml_str = XmlStorage.to_xml(p)
print(xml_str)


with open("ArchivosXML/prueba.xml") as f:
    xml_str = f.read()

# Creamos una instancia de ElementTree y obtenemos la raíz del árbol
xml_doc = ET.fromstring(xml_str)
print(xml_doc)

lstPerson=XmlStorage.from_xml(xml_doc,False)

print(lstPerson)


