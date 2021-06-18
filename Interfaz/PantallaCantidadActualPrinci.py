from BaseDeDatos import CapaConexion

class PantallaCantidadActualPrinci():
    
    cantidadActual = 0
    capacidadTotal = 0

    
    def __init__(self, cantidad, capacidad):

        self.cantidadActual = cantidad
        self.capacidadTotal = capacidad

    
    def actualizarCantidadActualPrincipal(self, cantidad):
        #! CORROBORAR
        print('Cantidad Vieja:' ,self.cantidadActual)
        nueva_cant = self.cantidadActual + cantidad
        self.cantidadActual = nueva_cant
        print('Cantidad nueva:', nueva_cant)