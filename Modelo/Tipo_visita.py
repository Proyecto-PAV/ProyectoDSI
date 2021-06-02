

class TipoVisita():

    nombre = ""
    tipoVisita = 0

    def __init__(self, nombre, tipoVisita):
        self.nombre = nombre
        self.tipoVisita = tipoVisita

    def getNombre(self):
        return self.nombre

    def getTipoVisita(self):
        return self.tipoEntrada

    def mostrarNombre(self):
        return "Nombre: "+ self.nombre
