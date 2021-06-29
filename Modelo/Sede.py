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
    
    def getExposicionesCompletasVigentes(nombre, tipo_visita):
        #levantamos todos las exposiciones de la BD que sean vigentes
        expo_vigentes = Exposicion.esVigente(nombre)
        #de esas vigentes obtenemos su duracion resumida
        duracion_resumida = Exposicion.getDetalleExposición(expo_vigentes, tipo_visita)
        return duracion_resumida

    def getReservaVisita(sede_actual, duracionEstimada, estadoConfirmado, fecha_actual):
        #busca las reservas para la fecha y hora de hoy
        reservasObj = ReservaVisita.esParaFechaYHora(duracionEstimada, sede_actual, fecha_actual)
        #busca la cantidad de alumnos confirmados en las reservas 
        cantidadAlumnosConfirmados = ReservaVisita.getCantidadAlumnosConfirmados(reservasObj, estadoConfirmado)
        return cantidadAlumnosConfirmados

    def getEntradaVendidas(sede_actual, fechaHoraActual):
        #busca toda la coleccion de entradas registradas de la sede pasada por parametro
        entradasObj = Entrada.esSedeActual(sede_actual)
        #filtra aquellas entradas que son para la fecha y hora de hoy y retorna la cantidad que coincide
        entradasVendidasActual = Entrada.getEntradasFechaHoraVenta(entradasObj, fechaHoraActual)
        #retorna la cantidad de personas en el museo que han ido particular
        return entradasVendidasActual
