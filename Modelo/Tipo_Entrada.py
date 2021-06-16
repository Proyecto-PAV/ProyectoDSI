from BaseDeDatos.CapaConexion import *


class TipoEntrada():

    nombre = ""
    tipoEntrada = 0

    def __init__(self, nombre, tipoEntrada):
        self.nombre = nombre,
        self.tipoEntrada = tipoEntrada

    def getNombre(self):
        pass

    def getTipoEntrada(self, numero):
        nombre = ObtenerNombreEntrada(numero)
        return nombre

    def mostrarNombre(self):
        return "Nombre: "+ self.nombre

    
