from Interfaz.PantallaCantidadActualPrinci import PantallaCantidadActualPrinci


class PantallaCantActualSala():
    
    #atributos de la clase PantallaCantActualSala
    cantidadActual = 0
    sala = ""
    capacidadSede = ""

    def __init__(self, sala, cantidad, capacidadSede):
        #constructor del objeto PantallaCantActualSala
        self.cantidadActual = cantidad
        self.nombreSala = sala
        self.capacidadSede = capacidadSede

    
    def actualizarCantidadActualSala(self, agregado):
        cant_nueva = self.cantidadActual + agregado
        self.cantidadActual = cant_nueva
