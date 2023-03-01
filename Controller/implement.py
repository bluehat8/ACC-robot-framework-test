import xml.etree.ElementTree as ET
from io import StringIO
import sys
sys.path.append('./Model')
import Person

import XmlStorage
from typing import Type, List
from xml.etree.ElementTree import Element


p1 = Person.Person("John", 30)
p2 = Person.Person("Jane", 25)

person_list = [p1,p2]

xml_str=XmlStorage.list_to_xml(person_list)
#print(xml_str)

XmlStorage.create_xml(xml_str, "ArchivosXML/Persona2.xml")

element_names = p1.get_element_names()


def get_person_data(xml_str, element_names):
    return XmlStorage.from_xml_5(xml_str=xml_str, class_type=Person.Person,
                                 attributes=element_names, include_output=False)

print("====================================================")
for person in get_person_data(xml_str, element_names):
    print(person.name, person.age)
    
