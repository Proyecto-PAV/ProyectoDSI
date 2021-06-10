from Modelo.Empleado import Empleado
from Modelo import Sede
from Modelo import guia 
from Modelo import Tarifa 
from Modelo import guia 

class Entrada():

    fechaVenta = ""
    horaVenta = ""
    monto = 0
    numero = 0
    sedes = []
    guia = True
    tarifa = []
    def __init__(self, fechaVenta, horaVenta, monto, numero, sedes, guia, tarifa):
        self.fechaVenta = fechaVenta
        self.horaVenta = horaVenta
        self.monto = monto
        self.numero = numero
        self.sede = sedes
        self.guia = guia
        self.tarifa = tarifa

    def conocerGuiaAsignado(self):
        return self.guia
    def conocerSede(self):
        return self.sedes
    def conocerTarifa(self):
        return self.tarifa
    def getNro(self):
        return self.numero
    def new(self, fechaVenta, horaVenta, monto, numero, sedes, guia, tarifa):
        return Entrada(self, fechaVenta, horaVenta, monto, numero, sedes, guia, tarifa)