from BaseDeDatos import CapaConexion

class PantallaCantidadActualPrinci():
    
    cantidadActual = 0
    capacidadTotal = 0

    
    def __init__(self, cantidad, capacidad):

        self.cantidadActual = cantidad
        self.capacidadTotal = capacidad

    
    def actualizarCantidadActualPrincipal(self, cantidad):
        #! CORROBORAR
        nueva_cant = self.cantidadActual + cantidad
        self.cantidadActual = nueva_cant