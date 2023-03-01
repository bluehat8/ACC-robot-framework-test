import xml.etree.ElementTree as ET
from io import StringIO
import Person

import XmlStorage
from typing import Type, List
from xml.etree.ElementTree import Element

#instancia=Person()

def to_xml(obj):
    root = ET.Element(obj.__class__.__name__)
    for k, v in vars(obj).items():
        child = ET.Element(k)
        child.text = str(v)
        root.append(child)
    return ET.tostring(root, encoding='unicode')

p1 = Person.Person("John", 30)
p2 = Person.Person("Jane", 25)

person_list = [p1,p2]

xml_str=XmlStorage.list_to_xml(person_list)
print(xml_str)


element_names = p1.get_element_names()

# print(element_names)

person_list_from_xml = XmlStorage.from_xml_4(xml_str, Person.Person,element_names)

# print(person_list_from_xml[0])
for person in person_list_from_xml:
    print(person.name, person.age)
    

#print(XmlStorage.get_init_attributes(Person))
# person_list_from_xml2 = XmlStorage.from_xml_generic2(xml_str, Person)

# print(person_list_from_xml2)



# xml_str = XmlStorage.to_xml(person_list)

# xml_doc = ET.fromstring(xml_str)
# person_list = XmlStorage.from_xml3(xml_str)

# print(person_list)