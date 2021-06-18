from Interfaz.PantallaCantidadActualPrinci import PantallaCantidadActualPrinci
from BaseDeDatos import CapaConexion

class PantallaCantActualSala():
    
    cantidadActual=0
    sala=""
    capacidadSede=""

    def __init__(self, sala, cantidad, capacidadSede):
        self.cantidadActual = cantidad
        self.nombreSala = sala
        #! agregar este atributo al de clases
        self.capacidadSede = capacidadSede

    
    def actualizarCantidadActualSala(self, agregado):
        print('Cantidad Vieja Sede:' ,self.cantidadActual)
        self.nombreSala
        cant_nueva = self.cantidadActual + agregado
        self.cantidadActual = cant_nueva
        print('Cantidad nueva Sede:', self.cantidadActual)
