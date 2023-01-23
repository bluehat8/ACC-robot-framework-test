from xml.dom import minidom
import xml.etree.cElementTree as ET


def leerXml(ruta, elemento):
    doc=minidom.parse(ruta)
    return (doc.getElementsByTagName(elemento)[0]).firstChild.data

def ingresarDatosDeSalidaXML(ruta, findall, atributo, valor):
# Crea un arbol y consigue su raíz.
    arbol = ET.parse('ArchivosXML/contribuNatural.xml')
    raiz = arbol.getroot()

# Una vez hecho esto, puedes empezar a iterar mediante raiz.iter() o raiz.findall(). Ej.
    cadena = valor # por ejemplo.

    for hijo in raiz.findall('output'):
        hijo.find('numerocontribuyente').text =valor

    arbol.write('ArchivosXML/contribuNatural.xml',encoding="UTF-8",xml_declaration=True)

ingresarDatosDeSalidaXML('ruta','findall','at','QA prueba2');