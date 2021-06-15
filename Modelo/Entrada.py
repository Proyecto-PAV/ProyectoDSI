from Modelo.Empleado import Empleado
from Modelo import Sede
from Modelo import guia 
from Modelo import Tarifa 
from Modelo import guia 

class Entrada():
    numero = 0
    fechaVenta = ""
    horaVenta = ""
    monto = 0
    idTipoEntrada = 0
    idTipoVisita = 0
    nombre_sede = ""
    guia = True
    def __init__(self, numero,fechaVenta, horaVenta, monto, idTipoEntrada, idTipoVisita,sede, guia, ):
        self.numero = numero
        self.fechaVenta = fechaVenta
        self.horaVenta = horaVenta
        self.monto = monto
        self.sede = sede
        self.guia = guia
        self.idTipoEntrada = idTipoEntrada
        self.idTipoVisita = idTipoVisita

    def conocerGuiaAsignado(self):
        return self.guia
    def conocerSede(self):
        return self.sedes
    def conocerTarifa(self):
        return self.tarifa
    def getNro(self):
        return self.numero
    def new(self, fechaVenta, horaVenta, monto, numero, sedes, guia, tarifa):
        return Entrada(self, numero, fechaVenta, horaVenta, monto, sedes, guia, tarifa)