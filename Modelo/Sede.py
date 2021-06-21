from Modelo.Tarifa import Tarifa
from BaseDeDatos.CapaConexion import *
from Modelo.Exposicion import *


from Modelo.Entrada import *
class Sede():
    
    #atributos de la clase Sede
    cantidadMaximaPorGuia = 0
    cantidadMaximaVisitantes = 0
    duracionExposicionesVigentes = 0 
    exposicionesVigentes = []
    nombre = ''
    reservaVisita = ''
    tarifasVigentes = [] 

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

    def getCantidadMaximaVisitantes(sede_actual):
        return sede_actual.cantidadMaximaVisitantes

    def getAdicionalPorGuia(sedeNombre):
        #obtiene las sede de la BD e instancia como objetos
        sedesBd = obtenerSedes()
        for sede in sedesBd:
            sedeObj = Sede(sede[2], sede[1], None, None, sede[0], None, None, sede[3])
            if sedeObj.nombre == sedeNombre:
                #Retorna el objeto cuyo nombre coincida con el pasado por parametro
                return sedeObj.adicionalGuia

    def getTarifasVigentes(nombre_sede, fecha_hora_actual):
        #busca las tarifas vigentes a la fecha actual
        tarifasVigentes = Tarifa.esVigente(nombre_sede, fecha_hora_actual)
        #por cada tarifa vigente obtenida, obtiene su monto, tipo visita y tipo entrada
        for t in tarifasVigentes:
            t.getMonto()
        #obtener el monto adicional definido para cada sede
        montoAdicional = Sede.getAdicionalPorGuia(nombre_sede)
        
        return tarifasVigentes, montoAdicional

    
    def getExposicionesCompletasVigentes(nombre):
        #levantamos todos las exposiciones de la BD que sean vigentes
        expo_vigentes = Exposicion.esVigente(nombre)
        #de esas vigentes obtenemos su duracion resumida
        duracion_resumida = Exposicion.getDetalleExposición(expo_vigentes)
        return duracion_resumida


    def getReservaVisita(sede_actual, duracionEstimada, estadoConfirmado, fecha_actual):
        #busca las reservas para la fecha y hora de hoy
        reservasObj = ReservaVisita.esParaFechaYHora(duracionEstimada, sede_actual, fecha_actual)
        #busca la cantidad de alumnos confirmados en las reservas 
        cantidadAlumnosConfirmados = ReservaVisita.getCantidadAlumnosConfirmados(reservasObj, estadoConfirmado)
        return cantidadAlumnosConfirmados

    def getEntradaVendidas(sede_actual, duracionEstimada):
        
        entradasObj = Entrada.esSedeActual(sede_actual)
        EntradasVendidasActual = Entrada.getEntradasFechaHoraVenta(entradasObj, duracionEstimada)
        print (EntradasVendidasActual)
        return EntradasVendidasActual
