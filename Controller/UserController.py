import sys
sys.path.append('./Model')
import Users
import XmlStorage

xml_to_str= XmlStorage.xml_to_str("ArchivosXML/prueba.xml")
instancia= Users.User('1','1s')
element_names = instancia.get_element_names()

def get_user_data(xml_str, element_names):
    return XmlStorage.from_xml_5(xml_str=xml_str, class_type=Users.User, attributes=element_names, include_output=False)

def get_user_attribute(data, position):
    lst=get_user_data(xml_to_str, element_names)
    obj=lst[position]
    return getattr(obj,data)
    