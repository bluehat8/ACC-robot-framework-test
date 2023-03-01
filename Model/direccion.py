import XmlStorage
import xml.etree.ElementTree as ET
import inspect


class direccion:
    def __init__(self, tipoDireccion, calleIzquierda, calleDerecha, edificioCasa, apartamento, piso, distrito, barrio, direccion):
        self.tipoDireccion = tipoDireccion
        self.calleIzquierda = calleIzquierda
        self.calleDerecha = calleDerecha
        self.edificioCasa = edificioCasa 
        self.apartamento = apartamento
        self.piso = piso
        self.distrito = distrito
        self.barrio = barrio
        self.direccion = direccion
             
    # def __str__(self):
    #     return f"tipoDireccion: {self.tipoDireccion}, calleIzquierda: {self.calleIzquierda},"+"""
    # calleDerecha: {self.calleDerecha}, edificioCasa: {self.edificioCasa}, apartamento: {self.apartamento}, piso: {self.piso}, distrito: {self.distrito}, barrio: {self.barrio}, direccion: {self.direccion}"""
    
    def get_element_names(self):
        elements = list(self.__dict__.keys())

    # Filtrar los nombres no deseados
    
        elements = [e for e in elements if not e.startswith("__") and not callable(getattr(self, e))]
        return elements