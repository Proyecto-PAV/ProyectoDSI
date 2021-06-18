from PyQt5.QtCore import pyqtRemoveInputHook
from BaseDeDatos.CapaConexion import *

class TipoEntrada():

    nombre = ""
    tipoEntrada = 0

    def __init__(self, nombre, tipoEntrada):
        self.nombre = nombre
        self.tipoEntrada = tipoEntrada

    def getNombre(self):
        pass

    def getTipoEntrada(numero):
        tiposEntrasdasBd = obtenerTiposEntradas()
        for tipo in tiposEntrasdasBd:
            tipoEntrada = TipoEntrada(tipo[1], tipo[0])
            if tipoEntrada.tipoEntrada == numero:
                nombre = tipoEntrada.nombre
                return nombre

    def mostrarNombre(self):
        return "Nombre: "+ self.nombre

    
