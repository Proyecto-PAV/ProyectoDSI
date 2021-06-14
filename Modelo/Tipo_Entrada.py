from BaseDeDatos import CapaConexion


class TipoEntrada():

    nombre = ""
    tipoEntrada = 0

    def __init__(self, nombre, tipoEntrada):
        self.nombre = nombre,
        self.tipoEntrada = tipoEntrada

    def getNombre(self, numero):

        nombre = CapaConexion.ObtenerNombreEntrada(numero)
        return nombre

    def getTipoEntrada(self, numero):
        nombre = self.getNombre(numero)
        return nombre

    def mostrarNombre(self):
        return "Nombre: "+ self.nombre

    
