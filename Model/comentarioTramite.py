import XmlStorage
import xml.etree.ElementTree as ET
import inspect


class ComentarioTramite:
    def __init__(self, comentario):
        self.comentario = comentario
                
        
    def get_element_names(self):
        elements = list(self.__dict__.keys())

    # Filtrar los nombres no deseados
    
        elements = [e for e in elements if not e.startswith("__") and not callable(getattr(self, e))]
        return elements