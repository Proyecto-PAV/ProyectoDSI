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
    def getNro(nombreSede):
        ultimoNro = 0
        entradas = obtenerEntradas()
        for row in entradas:
            o = Entrada(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            if (o.numero > ultimoNro) and (o.nombre_sede == nombreSede):
                ultimoNro = o.numero
        return ultimoNro
    def new(self):
        pass
