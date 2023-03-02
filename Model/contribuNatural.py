import XmlStorage
import xml.etree.ElementTree as ET
import inspect


class ContribuNatural:
    def __init__(self, tipoPersona, primerNom=0, segundoNom=0, documentoID=0, diaNaci=0, mesNaci=0, añoNaci=0, comentario=0, primerApe=0, segundoApe=0, identificacion=0, genero=0):
        self.tipoPersona = tipoPersona
        self.primerNom = primerNom
        self.segundoNom = segundoNom
        self.documentoID = documentoID
        self.diaNaci = diaNaci
        self.mesNaci = mesNaci
        self.añoNaci = añoNaci
        self.comentario = comentario
        self.primerApe = primerApe
        self.segundoApe = segundoApe
        self.identificacion = identificacion
        self.genero = genero
             
    def get_element_names(self):
        elements = list(self.__dict__.keys())

    # Filtrar los nombres no deseados
    
        elements = [e for e in elements if not e.startswith("__") and not callable(getattr(self, e))]
        return elements