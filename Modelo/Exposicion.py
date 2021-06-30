from Modelo.Detalle_Exposicion import Detalle_Exposicion
from datetime import datetime
from BaseDeDatos import CapaConexion

class Exposicion():

    #atributos de la clase Exposicion
    detalleExposicion = []
    fechaFin = ""
    fechaFinReplanificada = ""
    fechaInicio = ""
    fechaInicioReplanificada = ""
    horaApertura = 0
    horaCierre = 0
    nombre = ""

    def __init__(self, detalleExposicion, fechaFin, fechaFinReplanificada, fechaInicio, fechaInicioReplanificada, horaApertura, horaCierre, nombreExpo, nombreSede, empleado):
        #constructor del objeto Exposicion
        self.detalleExposicion = detalleExposicion
        self.fechaFin = fechaFin
        self.fechaFinReplanificada = fechaFinReplanificada
        self.fechaInicio = fechaInicio
        self.fechaInicioReplanificada = fechaInicioReplanificada
        self.horaApertura = horaApertura 
        self.horaCierre = horaCierre
        self.nombre = nombreExpo
        self.nombreSede = nombreSede
        self.empleado = empleado


    def calcularDuracionObrasExpuestas(self):
        pass

    def conocerDetalleExposicion(self):
        pass

    def conocerEmpleado(self):
        return self.empleado

    def conocerPublicoDestino(self):
        pass

    def conocerTipoExposicion(self):
        pass

    def esVigente(self, fecha):                
        #determinar si una exposicion es vigente o no, devolviendo false o true respectivamente
        fecha = datetime.date(fecha)
        if (self.fechaFin>fecha and self.fechaInicio<fecha):
            return True
        elif (self.fechaFinReplanificada>=fecha and self.fechaInicioReplanificada<=fecha):
            return True
        else:
            return False
  
    def getDetalleExposicionRes(self):
        #buscar todos los detalles de esa expo
        detalles = CapaConexion.obtenerDetalleExposiciones()
        # creacion del contador en tipo hh/mm/ss para contar el tiempo de la obra
        duracion_resumida = 0
        #comienzo del ciclo
        for d in detalles:
            detalle = Detalle_Exposicion(d[2], d[1], d[0])
            if self.detalleExposicion== detalle.exposicion:
                duracion_resumida +=  detalle.getObraResumida()
        #retrorna el total de la exposicion como un str en formato HH:MM:SS
        return duracion_resumida

    def getDetalleExposicionExtendida(self):
        #buscar todos los detalles de esa expo
        detalles = CapaConexion.obtenerDetalleExposiciones()
        # creacion del contador en tipo hh/mm/ss para contar el tiempo de la obra
        duracion_resumida = 0
        #comienzo del ciclo
        for d in detalles:
            detalle = Detalle_Exposicion(d[2], d[1], d[0])
            if self.detalleExposicion== detalle.exposicion:
                duracion_resumida +=  detalle.getObraExtendida()
        #retrorna el total de la exposicion como un str en formato HH:MM:SS
        return duracion_resumida

    def getNombre(self):
        return self.nombre



    

    