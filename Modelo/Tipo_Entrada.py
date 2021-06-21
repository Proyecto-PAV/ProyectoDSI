from PyQt5.QtCore import pyqtRemoveInputHook
from BaseDeDatos.CapaConexion import *

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

    def getTipoEntrada(numero):
        #buscamos todas las entradas en la BD y creamos el obtejo
        tiposEntrasdasBd = obtenerTiposEntradas()
        for tipo in tiposEntrasdasBd:
            TE = TipoEntrada(tipo[1], tipo[0])
            #Si el tipo entrada creado coincide con el pasado por el parametro lo retorna
            if  TE.tipoEntrada == numero:
                return TE

    def mostrarNombre(self):
        return "Nombre: "+ self.nombre

    
