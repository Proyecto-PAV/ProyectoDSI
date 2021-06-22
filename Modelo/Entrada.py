from BaseDeDatos.CapaConexion import *
from typing import DefaultDict
from BaseDeDatos import CapaConexion
from datetime import datetime, timedelta
import time
from Modelo.Empleado import Empleado
from Modelo import Sede
from Modelo import Tarifa 


class Entrada():
    numero = 0
    fechaVenta = ""
    horaVenta = ""
    monto = 0
    numero = 0
    
    def __init__(self, fechaVenta, horaVenta, monto, numero, sede):
        self.fechaVenta = fechaVenta
        self.horaVenta = horaVenta
        self.monto = monto
        self.numero = numero
        self.sede = sede

    def conocerGuiaAsignado(self):
        return self.guia
    def conocerSede(self):
        return self.sedes
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
    def new(numero, fechaVenta, horaVenta, monto, id_tipo_entrada, id_tipo_visita, nombre_sede, dni_guia):
        nuevaEntrada = Entrada(numero, fechaVenta, horaVenta, monto, id_tipo_entrada, id_tipo_visita, nombre_sede, dni_guia)
        return nuevaEntrada
        return self.tarifa
    def getNro(self):
        return self.numero
    def new(self, fechaVenta, horaVenta, monto, numero, sedes, guia, tarifa):
        return Entrada(self, numero, fechaVenta, horaVenta, monto, sedes, guia, tarifa)
        pass
    

    def esSedeActual(sede_actual):
        #busca todas las entradas de la sede de la BD
        entradas = CapaConexion.obtenerEntradasPorSede()      
        #crea el objeto entrada y almacena aquellas cuya sede sea la pasada por parametro
        EntradasDeSede = []
        for row in entradas:           
            objeto = Entrada(row[1],row[2],row[3],row[0], row[4])    
            if objeto.sede == sede_actual:    
                EntradasDeSede.append(objeto)
        #devuelve la coleccion de objetos completa
        return EntradasDeSede

    def getEntradasFechaHoraVenta(entradasObj, duracionEstimada):
        #incializa el contador de entradas y obtiene la fecha actual
        #! la fecha podemos pasarla por parametro
        entradasFechaHora = 0
        fecha_hora_actual = datetime.now()
        #por cada una de las entradas que nos pasa por parametro, validamos su fecha
        for i in range(0, len(entradasObj)):   
            #! si suponemos que la entrada cuenta para todo el dia, esto seria mas sencillo
            horaVentaString = entradasObj[i].horaVenta.strftime('%H:%M:%S')
            
            lista = horaVentaString.split(":")
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
           
            E = datetime.combine(entradasObj[i].fechaVenta, datetime.min.time())
            
            fecha_fin = hora_fin + E           
            dia1=fecha_fin.day
            dia2=fecha_hora_actual.day
            
            #si la fecha de la entrada es la correspondiente, incrementa el contador en 1
            if (fecha_fin > fecha_hora_actual) and (dia1 == dia2):
                entradasFechaHora += 1
        #retorna la cantidad de entradas vendidas para el momento de venta
        return entradasFechaHora
