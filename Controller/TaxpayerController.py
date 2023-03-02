import sys
sys.path.append('./Model')
import contribuNatural
import XmlStorage

xml_to_str= XmlStorage.xml_to_str("ArchivosXML/contribuNatural.xml")
instancia= contribuNatural.ContribuNatural('')
element_names = instancia.get_element_names()

def get_data(xml_str, element_names):
    return XmlStorage.from_xml_5(xml_str=xml_str, class_type=contribuNatural.ContribuNatural,
                                 attributes=element_names, include_output=False)

def get_attribute(data, position):
    lst=get_data(xml_to_str, element_names)
    obj=lst[int(position)]
    return getattr(obj,data)


print("======",get_attribute('primerNom',0))