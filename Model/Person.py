import XmlStorage
import xml.etree.ElementTree as ET
import inspect


# Ejemplo de uso
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    def get_element_names(self):
        elements = list(self.__dict__.keys())
    # Filtrar los nombres no deseados
        elements = [e for e in elements if not e.startswith("__") and not callable(getattr(self, e))]
        return elements
   
    



