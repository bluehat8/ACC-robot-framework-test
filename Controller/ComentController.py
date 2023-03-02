import sys
sys.path.append('./Model')
import comentarioTramite
import XmlStorage

xml_to_str= XmlStorage.xml_to_str("ArchivosXML/comentarioTramite.xml")
instancia= comentarioTramite.ComentarioTramite('')
element_names = instancia.get_element_names()

def get_data(xml_str, element_names):
    return XmlStorage.from_xml_5(xml_str=xml_str, class_type=comentarioTramite.ComentarioTramite,
                                 attributes=element_names, include_output=False)

def get_attribute(data, position):
    lst=get_data(xml_to_str, element_names)
    obj=lst[int(position)]
    return getattr(obj,data)


#print("======",get_attribute('comentario',0))
# print("====================================================")
# for users in get_user_data(xml_to_str, element_names):
#     print(users.username, users.password)
    