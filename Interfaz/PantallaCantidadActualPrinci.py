from BaseDeDatos import CapaConexion

class PantallaCantidadActualPrinci():
     #atributos de la clase PantallaCantidadActualPrinci
    cantidadActual = 0
    capacidadTotal = 0

    
    def __init__(self, cantidad, capacidad):
         #atributos de la clase PantallaCantidadActualPrinci
        self.cantidadActual = cantidad
        self.capacidadTotal = capacidad

    
    def actualizarCantidadActualPrincipal(self, cantidad):
        nueva_cant = self.cantidadActual + cantidad
        self.cantidadActual = nueva_cant