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

    def getNro(self):
        #buscamos todas las entradas de la BD e incializa el ultimo nro
        return self.numero

    '''
    def new(numero, fechaVenta, horaVenta, monto, id_tipo_entrada, id_tipo_visita, nombre_sede, dni_guia):
        #crea el objeto nueva entrada y lo almacena en la BD
        nuevaEntrada = Entrada(numero, fechaVenta, horaVenta, monto, id_tipo_entrada, id_tipo_visita, nombre_sede, dni_guia)
        CapaConexion.almacenarEntrada(nuevaEntrada)
        return nuevaEntrada
    '''

    def new(self):
        #almacena el objeto en la BD
        CapaConexion.almacenarEntrada()


    def esSedeActual(self, sede_actual):
        #devuelve la coleccion de objetos completa
        if self.nombre_sede == sede_actual:
            return True
        else:
            return False

    def getEntradasFechaHoraVenta(self, fechaHoraActual):
        #separa la fecha de la hora del atributo del gestor
        fecha_actual = datetime.date(fechaHoraActual)
        if (self.fechaVenta == fecha_actual):
            #retorna 1 o 0 dependiendo si la entrada fue vendida el dia de la fecha actual u otro día
            return 1
        else:
            return 0
