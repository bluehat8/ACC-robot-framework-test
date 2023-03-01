from xml.dom import minidom
import xml.etree.cElementTree as ET

def leerXml(ruta, elemento):
    doc=minidom.parse(ruta)
    return (doc.getElementsByTagName(elemento)[0]).firstChild.data

def ingresarDatosDeSalidaXML(ruta, findall, atributo, valor):
# Crea un arbol y consigue su raíz.
    arbol = ET.parse(ruta)
    raiz = arbol.getroot()
    
# Una vez hecho esto, puedes empezar a iterar mediante raiz.iter() o raiz.findall(). Ej.
    for hijo in raiz.findall(findall):
        hijo.find(atributo).text =valor

    arbol.write(ruta,encoding="UTF-8",xml_declaration=True)
    
