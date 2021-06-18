from Modelo.Tarifa import Tarifa
from BaseDeDatos.CapaConexion import *
from Modelo.Exposicion import *


class Sede():
    
    cantidadMaximaPorGuia = 0
    cantidadMaximaVisitantes = 0
    duracionExposicionesVigentes = 0 
    exposicionesVigentes = []
    nombre = ''
    reservaVisita = ''
    tarifasVigentes = False #Cambiar a booleano

    def __init__(self, cantidadMaximaPorGuia, cantidadMaximaVisitantes,
    duracionExposicionesVigentes,exposicionesVigentes,nombre,reservaVisita, tarifasVigentes, adicionalGuia):
        self.cantidadMaximaPorGuia = cantidadMaximaPorGuia
        self.cantidadMaximaVisitantes = cantidadMaximaVisitantes
        self.duracionExposicionesVigentes = duracionExposicionesVigentes
        self.exposicionesVigentes = exposicionesVigentes
        self.nombre = nombre
        self.reservaVisita = reservaVisita
        self.tarifasVigentes = tarifasVigentes
        self.adicionalGuia = adicionalGuia


    def calcularDuracionAExposicionesVigentes(self, duracionExposicionesVigentes):
        '''for exposicionesVigentes in self.exposicionesVigentes:
                if (exposicionesVigentes.esVigente() == True):
                    duracionExposicionesVigentes += exposicionesVigentes.
                    return duracionExposicionesVigentes
                else:
                    return None
        '''
        #Revisar y borrar este metodo
        pass
    
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
    #Se sigue con los def

    def getCantidadMaximaVisitantes(self):
        return self.cantidadMaximaVisitantes

    def getEntradaVendidas(self): #sede en ningun momento conoce la cantidad de entradas vendidas
        pass

    def getAdicionalPorGuia(sedeNombre):
        #obtiene el mondo adicional de la bd
        sedesBd = obtenerSedes()
        for sede in sedesBd:
            sedeObj = Sede(sede[2], sede[1], None, None, sede[0], None, None, sede[3])
            if sedeObj.nombre == sedeNombre:
                return sedeObj.adicionalGuia

    def getTarifasVigentes(nombre_sede, fecha_hora_actual):

        tarifasVigentes = Tarifa.esVigente(nombre_sede, fecha_hora_actual)

        for t in tarifasVigentes:
            t.getMonto()
        
        return tarifasVigentes

        return datos_tarifas, adicional_guia
    
    def getExposicionesCompletasVigentes(nombre):
        #levantamos todos las exposiciones de la BD que sean vigentes
        expo_vigentes = Exposicion.esVigente(nombre)
        #de esas vigentes obtenemos su duracion resumida
        duracion_resumida = Exposicion.getDetalleExposición(expo_vigentes)
        return duracion_resumida

    