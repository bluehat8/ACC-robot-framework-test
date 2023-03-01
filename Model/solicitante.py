import xml.etree.ElementTree as ET
import inspect


class Solicitante:
    def __init__(self, cedula, telefono, cargo, correo):

        self.cedula = cedula
        self.telefono = telefono
        self.cargo = cargo
        self.correo = correo

      
    def get_element_names(self):
        elements = list(self.__dict__.keys())

    # Filtrar los nombres no deseados
    
        elements = [e for e in elements if not e.startswith("__") and not callable(getattr(self, e))]
        return elements
    




    