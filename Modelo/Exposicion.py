import datetime
from BaseDeDatos import CapaConexion

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
        fecha_actual = datetime.now()
        v_vigentes = CapaConexion.ObtenerExposicionesEnVigencia(nombre_sede, fecha_actual)
        expo_vigentes_obj = [] 
        
        for obj in v_vigentes:
            expo = Exposicion(None, obj[3], obj[4],obj[1], obj[2], obj[5], obj[6], obj[7], None)
            expo_vigentes_obj.append(expo) 
        
        return expo_vigentes_obj
        

    def getDetalleExposición(self):
        return self.detalleExposicion
    