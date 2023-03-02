import xml.etree.ElementTree as ET
import inspect


class TelefonoCorreo:
    def __init__(self, tipoTelefono, numTelefono=0, correo=0):

        self.tipoTelefono = tipoTelefono
        self.numTelefono = numTelefono
        self.correo = correo

      
    def get_element_names(self):
        elements = list(self.__dict__.keys())

    # Filtrar los nombres no deseados
    
        elements = [e for e in elements if not e.startswith("__") and not callable(getattr(self, e))]
        return elements