from BaseDeDatos import CapaConexion

class TipoVisita():

    nombre = ""
    tipoVisita = 0

    def __init__(self, nombre, tipoVisita):
        self.nombre = nombre
        self.tipoVisita = tipoVisita

    def getNombre(self, numero):
        nombre = CapaConexion.ObtenerNombreVisita(numero)
        return nombre

    def getTipoVisita(self, numero):
        nombre = self.getNombre(numero)
        return nombre

    def mostrarNombre(self):
        return "Nombre: "+ self.nombre
