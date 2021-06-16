from Modelo.Detalle_Exposicion import Detalle_Exposicion
from datetime import datetime
from BaseDeDatos.CapaConexion import *

class Exposicion():

    detalleExposicion = []
    fechaFin = ""
    fechaFinReplanificada = ""
    fechaInicio = ""
    fechaInicioReplanificada = ""
    horaApertura = 0
    horaCierre = 0
    nombre = ""

    def __init__(self, detalleExposicion, fechaFin, fechaFinReplanificada, fechaInicio, fechaInicioReplanificada, horaApertura, horaCierre, nombreSede, empleado):
        self.detalleExposicion = detalleExposicion
        self.fechaFin = fechaFin
        self.fechaFinReplanificada = fechaFinReplanificada
        self.fechaInicio = fechaInicio
        self.fechaInicioReplanificada = fechaInicioReplanificada
        self.horaApertura = horaApertura 
        self.horaCierre = horaCierre
        self.nombre = nombreSede
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

    def esVigente(self,nombre_sede):
        #! preguntar como saber si es completa -con conocerTipoExposicion?
        fecha = datetime.now()
        v_vigentes = obtenerExposicionesEnVigencia(nombre_sede, fecha)
        expo_vigentes_obj = [] 
        
        for obj in v_vigentes:
            expo = Exposicion(None, obj[3], None, obj[1], None, obj[5], obj[6], obj[7], None)
            expo_vigentes_obj.append(expo) 
        
        return expo_vigentes_obj
        

    def getDetalleExposición(self, vigentes):
        #calcular el total de la duracion 
        duracion_total = 0
        for e in vigentes:
            duracion_total +=  Detalle_Exposicion.getObra(e.nombre)

        return duracion_total


    

    