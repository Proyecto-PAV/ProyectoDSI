from BaseDeDatos import CapaConexion
from datetime import datetime, timedelta


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
    def getNro(self):
        pass
    def new(self):
        pass

    def esSedeActual(sede_actual):
        entradas = CapaConexion.obtenerEntradasPorSede(sede_actual)
        EntradasDeSede = []
        for row in entradas:
            objeto = Entrada(entradas[1],entradas[2],entradas[3],entradas[4])
            EntradasDeSede.append(objeto)
        return EntradasDeSede

    def getEntradasFechaHoraVenta(self, entradasObj, duracionEstimada):
        entradasFechaHora = 0
        fecha_hora_actual = datetime.now()
        for i in range(0, len(entradasObj)):
            lista = self.horaVenta.split(":")
            hora=int(lista[0])
            minuto=int(lista[1])
            segundo=int(lista[2])
            dh = timedelta(hours=hora) 
            dm = timedelta(minutes=minuto)          
            ds = timedelta(seconds=segundo) 
            resultado1 = duracionEstimada + ds
            resultado2 = resultado1 + dm
            hora_fin = resultado2 + dh
            if hora_fin > fecha_hora_actual:
                entradasFechaHora += 1
        return entradasFechaHora