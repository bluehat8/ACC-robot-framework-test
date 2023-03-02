import XmlStorage
import xml.etree.ElementTree as ET
import inspect


class ContribGeneralidades:
    def __init__(self, nacionalidad, profesion=0, numeroNis=0, estadoCivil=0, cuentaEnacal=0):
        self.nacionalidad = nacionalidad
        self.profesion = profesion
        self.numeroNis = numeroNis
        self.estadoCivil = estadoCivil
        self.cuentaEnacal = cuentaEnacal
        
   
    def get_element_names(self):
        elements = list(self.__dict__.keys())

    # Filtrar los nombres no deseados
    
        elements = [e for e in elements if not e.startswith("__") and not callable(getattr(self, e))]
        return elements