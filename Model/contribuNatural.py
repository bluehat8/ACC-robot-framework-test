import XmlStorage
import xml.etree.ElementTree as ET
import inspect


class contribGeneralidades:
    def __init__(self, tipoPersona, primerNom, segundoNom, documentoID, diaNaci, mesNaci, añoNaci, comentario, primerApe, segundoApe, identificacion, genero):
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