from BaseDeDatos.CapaConexion import *

class TipoVisita():

    nombre = ""
    tipoVisita = 0

    def __init__(self, nombre, tipoVisita):
        self.nombre = nombre
        self.tipoVisita = tipoVisita

    def getNombre(self):
        pass

    def getTipoVisita(numero):
        tiposVisitasBd = obtenerTiposVisitas()
        for tipo in tiposVisitasBd:
            tipoVisita = TipoVisita(tipo[1], tipo[0])
            if tipoVisita.tipoVisita == numero:
                nombre = tipoVisita.nombre
                return nombre

    def mostrarNombre(self):
        return "Nombre: "+ self.nombre
