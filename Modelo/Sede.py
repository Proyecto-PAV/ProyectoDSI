from Modelo.Tarifa import *
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
    duracionExposicionesVigentes,exposicionesVigentes,nombre,reservaVisita, tarifasVigentes):
        self.cantidadMaximaPorGuia = cantidadMaximaPorGuia
        self.cantidadMaximaVisitantes = cantidadMaximaVisitantes
        self.duracionExposicionesVigentes = duracionExposicionesVigentes
        self.exposicionesVigentes = exposicionesVigentes
        self.nombre = nombre
        self.reservaVisita = reservaVisita
        self.tarifasVigentes = tarifasVigentes


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

    def getEntradaVendidas(): #sede en ningun momento conoce la cantidad de entradas vendidas
        pass

    def getAdicionalPorGuia(sede):
        #conectar BD
        monto_sede = CapaConexion.ObtenerMontoGuiaSede(sede)
        return monto_sede

    def getTarifasVigentes(nombre_sede, fecha_hora_actual):
        
        filtrar_tarifas = Tarifa.esVigente(nombre_sede, fecha_hora_actual)
        datos_tarifas = Tarifa.getMonto(filtrar_tarifas)
        adicional_guia = Sede.getAdicionalPorGuia(nombre_sede)

        return datos_tarifas, adicional_guia
    
    def getExposicionesCompletasVigentes(self, nombre):
        expo_vigentes = Exposicion.esVigente(nombre)
        duracion_resumida = Exposicion.getDetalleExposición(expo_vigentes)
        return duracion_resumida
                
