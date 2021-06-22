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

    def getTipoVisita(numero):
        tiposVisitasBd = obtenerNombreVisita()
        for tipo in tiposVisitasBd:
            tipoVisita = TipoVisita(tipo[1], tipo[0])
            if tipoVisita.tipoVisita == numero:
                nombre = tipoVisita.nombre
                return tipo

    def mostrarNombre(self):
        return "Nombre: "+ self.nombre
