from BaseDeDatos.CapaConexion import *
class Entrada():

    fechaVenta = ""
    horaVenta = ""
    monto = 0
    numero = 0
    
    def __init__(self, fechaVenta, horaVenta, monto, numero):
        self.fechaVenta = fechaVenta
        self.horaVenta = horaVenta
        self.monto = monto
        self.numero = numero

    def conocerGuiaAsignado(self):
        pass
    def conocerSede(self):
        pass
    def conocerTarifa(self):
        pass
    def getNro(self, nombre_sede):
        UltimoNumeroEntrada = ObtenerUltimoNumero(nombre_sede)
        return UltimoNumeroEntrada
    def new(self):
        pass
