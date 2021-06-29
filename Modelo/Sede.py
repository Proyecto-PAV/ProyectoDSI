'''
from Modelo.Tarifa import *
from BaseDeDatos.CapaConexion import *

'''
from Modelo.Entrada import *
from Modelo.Tarifa import Tarifa
from BaseDeDatos.CapaConexion import *
from Modelo.Exposicion import *


class Sede():
    
    #atributos de la clase Sede
    cantidadMaximaPorGuia = 0
    cantidadMaximaVisitantes = 0
    duracionExposicionesVigentes = 0 
    exposicionesVigentes = []
    nombre = ''
    reservaVisita = ''
    tarifasVigentes = []
    adicionalGuia = 0


    def __init__(self, cantidadMaximaPorGuia, cantidadMaximaVisitantes,
    duracionExposicionesVigentes,exposicionesVigentes,nombre,reservaVisita, tarifasVigentes, adicionalGuia):
        #constructor del objeto Sede
        self.cantidadMaximaPorGuia = cantidadMaximaPorGuia
        self.cantidadMaximaVisitantes = cantidadMaximaVisitantes
        self.duracionExposicionesVigentes = duracionExposicionesVigentes
        self.exposicionesVigentes = exposicionesVigentes
        self.nombre = nombre
        self.reservaVisita = reservaVisita
        self.tarifasVigentes = tarifasVigentes
        self.adicionalGuia = adicionalGuia

    
    def conocerColeccion(self):
        pass
    def conocerDeposito(self):
        pass
    def conocerEmpleado(self):
        pass
    def conocerExposicion(self):
        pass
    def conocerHorario(self):
        pass
    def conocerPlanta(self):
        pass
    def conocerTarifa(self):
        pass


    def getCantidadMaximaVisitantes(sede_actual):
        #Busca todas las sede y para aquella cuyo nombre coincida con el de parametro, retorna su cantidad max de visitantes
        sedesBd = obtenerSedes()
        for sede in sedesBd:
            sedeObj = Sede(sede[2], sede[1], None, None, sede[0], None, None, sede[3])
            if sedeObj.nombre == sede_actual.nombre:
                return sedeObj.cantidadMaximaVisitantes

    def getAdicionalPorGuia(self):
        return self.adicionalGuia

    def getTarifasVigentes(self, fecha_hora_actual):
        #traemos todas las tarifas de la BD
        tarifasBd = obtenerTarifas()
        t_montos = []
        for tarifa in tarifasBd:
            if tarifa[2] == self.nombre:
                objTarifa = Tarifa(tarifa[3], tarifa[4], tarifa[5], tarifa[0], tarifa[1])
                #validamos que las tarifas sean vigentes
                resultado = objTarifa.esVigente(fecha_hora_actual)
                if resultado:
                    #para todas las tarifas vigentes traemos su monto
                    objTarifa.getMonto()
                    t_montos.append(objTarifa)
        return t_montos
    
    def getExposicionesCompletasVigentes(nombre, fecha):
        #levantamos todos las exposiciones de la BD
        exposiciones = obtenerExposiciones()
        duracion_resumida = 0
        for exp in exposiciones:
            expo = Exposicion(None,exp[3], exp[2], exp[1], exp[2], exp[5], exp[6], exp[0], exp[7], exp[8])
            if expo.nombreSede == nombre:
                #Se determina si la exposicion de la sede actual es vigente para la fecha actual
                rdo = expo.esVigente(fecha)
                if rdo:
                    #si es vigente, obtiene la duracion de su/s detalle/s
                    duracion_resumida += expo.getDetalleExposicionRes()

        return duracion_resumida

    def getPorExposicionVigentes(self, fecha):
        #levantamos todos las exposiciones de la BD
        exposiciones = obtenerExposiciones()
  
        duracion_ext = 0
        for exp in exposiciones:
            expo = Exposicion(None,exp[3], exp[2], exp[1], exp[2], exp[5], exp[6], exp[0], exp[7], exp[8])
            if expo.nombreSede == self.nombre:
                #Se determina si la exposicion de la sede actual es vigente para la fecha actual
                rdo = expo.esVigente(fecha)
                if rdo:
                    #si es vigente, obtiene la duracion de su/s detalle/s
                    duracion_ext += expo.getDetalleExposicionRes()

        return duracion_ext

    def getReservaVisita(self, duracionEstimada, estadoConfirmado, fecha_actual):
        #busca las reservas de la BD y crea su objeto
        reservas = CapaConexion.obtenerReservas()
        cantidadAlumnosConfirmados = 0
        for row in reservas:
            res = ReservaVisita(row[6], row[7], None, row[1], row[2], row[5], row[4], row[0], None, None, row[8], None)
            #filtro la reserva para la sede actual
            if res.sede == self.nombre: 
                #Filtro la reserva si es de la fecha y hora actual para la duracion estimada de la venta
                reservaFH = res.esParaFechaYHora(duracionEstimada, fecha_actual)
                if reservaFH:
                    cantidadAlumnosConfirmados += res.getCantidadAlumnosConfirmados(estadoConfirmado)
        return cantidadAlumnosConfirmados

    def getEntradaVendidas(sede_actual, fechaHoraActual):
        #busca toda la coleccion de entradas registradas de la sede pasada por parametro
        entradasObj = Entrada.esSedeActual(sede_actual)
        #filtra aquellas entradas que son para la fecha y hora de hoy y retorna la cantidad que coincide
        entradasVendidasActual = Entrada.getEntradasFechaHoraVenta(entradasObj, fechaHoraActual)
        #retorna la cantidad de personas en el museo que han ido particular
        return entradasVendidasActual
