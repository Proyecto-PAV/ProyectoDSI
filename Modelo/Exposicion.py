from Modelo.Detalle_Exposicion import Detalle_Exposicion
from datetime import datetime
from BaseDeDatos.CapaConexion import *
import time

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

    def esVigente(nombre_sede):
        #? preguntar como saber si es completa -con conocerTipoExposicion?
        #obtener fecha actual y todas las exposiciones
        fecha = datetime.date(datetime.now())
        exposiciones = obtenerExposiciones()
        
        #filtrar exposiciones por las vigentes y almacenarlas en un nuevo vector
        vigentes=[]
        for exp in exposiciones:
           
            expo = Exposicion(None,exp[3], exp[2], exp[1], exp[2], exp[5], exp[6], exp[7],exp[8])

            if (expo.fechaFin>fecha and expo.fechaInicio<fecha) and (expo.nombre==nombre_sede):
                vigentes.append(expo)
            elif (expo.fechaFinReplanificada>fecha and expo.fechaInicioReplanificada<fecha) and (expo.nombre==nombre_sede):
                vigentes.append(expo)
        
        return vigentes
  
    def getDetalleExposición(vigentes):

        #calcular el total de la duracion 
        v=[]
        for expo in vigentes:
            v.append(Detalle_Exposicion.getObra(expo.nombre))

        return v
        
        duracion_total = 0
        for e in vigentes:
            duracion_total +=  Detalle_Exposicion.getObra(e.nombre)

        return duracion_total


    def getNombre(self):
        return self.nombre

#?solo de test, borrar dps
    def mostrarExpo(expo):
        print ( str(expo.detalleExposicion)+ '-'+
        str(expo.fechaFin)+ '-'+
        str(expo.fechaFinReplanificada)+'-'+
        str(expo.fechaInicio)+'-'+
        str(expo.fechaInicioReplanificada )+'-'+
        str(expo.horaApertura )+'-'+
        str(expo.horaCierre )+'-'+
        str(expo.nombre )+'-'+
        str(expo.empleado) )


    

    