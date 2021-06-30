from PyQt5.QtCore import pyqtRemoveInputHook
from BaseDeDatos.CapaConexion import *
#! revisar estos import

class TipoEntrada():

    #atributos de la clase TipoEntrada
    nombre = ""
    tipoEntrada = 0

    def __init__(self, nombre, tipoEntrada):
         #constructor del objeto TipoSesion
        self.nombre = nombre
        self.tipoEntrada = tipoEntrada

    def getNombre(self):
        pass

    def getTipoEntrada(self):
        #retornamos el tipo de entrada
        return self.nombre

    def mostrarNombre(self):
        return "Nombre: "+ self.nombre

    
