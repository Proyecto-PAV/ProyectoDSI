from BaseDeDatos.CapaConexion import *
from typing import DefaultDict
from BaseDeDatos import CapaConexion
from datetime import datetime, timedelta
import time
from Modelo.Empleado import Empleado
from Modelo import Tarifa 


class Entrada():
    
    numero = 0
    fechaVenta = ""
    horaVenta = ""
    monto = 0
    id_tipo_entrada = 0
    id_tipo_visita = 0
    nombre_sede = ""
    dni_guia = 0

    def __init__(self, numero, fechaVenta, horaVenta, monto, id_tipo_entrada, id_tipo_visita, nombre_sede, dni_guia):
        self.numero = numero
        self.fechaVenta = fechaVenta
        self.horaVenta = horaVenta
        self.monto = monto
        self.id_tipo_entrada = id_tipo_entrada
        self.id_tipo_visita = id_tipo_visita
        self.nombre_sede = nombre_sede
        self.dni_guia = dni_guia

    def conocerGuiaAsignado(self):
        return self.guia

    def conocerSede(self):
        return self.sedes

    def conocerTarifa(self):
        pass

    def getNro(nombreSede):
        #buscamos todas las entradas de la BD e incializa el ultimo nro
        entradas = CapaConexion.obtenerEntradas()
        ultimoNro = 0
        for row in entradas:
            o = Entrada(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            if (o.numero > ultimoNro) and (o.nombre_sede == nombreSede):
                ultimoNro = o.numero
        return ultimoNro


    def new(numero, fechaVenta, horaVenta, monto, id_tipo_entrada, id_tipo_visita, nombre_sede, dni_guia):
        #crea el objeto nueva entrada y lo almacena en la BD
        nuevaEntrada = Entrada(numero, fechaVenta, horaVenta, monto, id_tipo_entrada, id_tipo_visita, nombre_sede, dni_guia)
        CapaConexion.almacenarEntrada(nuevaEntrada)
        return nuevaEntrada


    def esSedeActual(sede_actual):
        #busca todas las entradas de la BD
        entradas = CapaConexion.obtenerEntradas()      
        #crea el objeto entrada y almacena aquellas cuya sede sea la pasada por parametro
        EntradasDeSede = []
        for row in entradas:           
            objeto = Entrada(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])   
            if objeto.nombre_sede == sede_actual:    
                EntradasDeSede.append(objeto)

        #devuelve la coleccion de objetos completa
        return EntradasDeSede

    def getEntradasFechaHoraVenta(entradasObj, fechaHoraActual):
        #incializa el contador de entradas y obtiene la fecha actual
        entradasFechaHora = 0
        fecha_actual = datetime.date(fechaHoraActual)
        #por cada una de las entradas que nos pasa por parametro, validamos su fecha
        for entrada in entradasObj:           
            #si la fecha de la entrada coincide con la pasada por parametro incrementa el contador en 1
            if (entrada.fechaVenta == fecha_actual):
                entradasFechaHora += 1

        #retorna la cantidad de entradas vendidas hoy para el momento de la venta
        return entradasFechaHora
