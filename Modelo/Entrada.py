from typing import DefaultDict
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
            lista2 = duracionEstimada.split(":")
            hora=int(lista[0])
            minuto=int(lista[1])
            segundo=int(lista[2])
            dh = timedelta(hours=hora) 
            dm = timedelta(minutes=minuto)          
            ds = timedelta(seconds=segundo) 
            hora2=int(lista2[0])
            minuto2=int(lista2[1])
            segundo2=int(lista2[2])
            dh2 = timedelta(hours=hora2) 
            dm2 = timedelta(minutes=minuto2)          
            ds2 = timedelta(seconds=segundo2) 
            resultado1 = ds2 + ds
            resultado2 = resultado1 + dm +dm2
            hora_fin = resultado2 + dh + dh2
            fecha_fin = hora_fin + self.fechaVenta
            if fecha_fin > fecha_hora_actual:
                entradasFechaHora += 1
        return entradasFechaHora