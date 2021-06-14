
class TipoEntrada():

    nombre = ""
    tipoEntrada = 0

    def __init__(self, nombre, tipoEntrada):
        self.nombre = nombre,
        self.tipoEntrada = tipoEntrada

    def getNombre(self):
        return self.nombre

    def getTipoEntrada(self):
        return self.tipoEntrada

    def mostrarNombre(self):
        return "Nombre: "+ self.nombre

    
