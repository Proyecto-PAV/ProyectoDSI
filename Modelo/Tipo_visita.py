from BaseDeDatos.CapaConexion import *

class TipoVisita():

     #atributos de la clase TipoVisita
    nombre = ""
    tipoVisita = 0

    def __init__(self, nombre, tipoVisita):
        #constructor del objeto TipoVisita
        self.nombre = nombre
        self.tipoVisita = tipoVisita

    def getNombre(self):
        pass

    def getTipoVisita(self):
        return self.nombre

    def mostrarNombre(self):
        return "Nombre: "+ self.nombre
