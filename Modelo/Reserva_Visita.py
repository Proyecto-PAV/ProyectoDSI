from BaseDeDatos import CapaConexion
from datetime import datetime, timedelta
from Modelo.Cambio_estado import Cambio_Estado
import time

class ReservaVisita():

    #!agregar atributos
    cantidadAlumnos = 0
    cantidadAlumnosConfirmada = 0
    duracionEstimada = 0 
    fechaCreacion = ""
    fechaHoraReserva = ""
    horaFinReal = 0
    horaInicioReal = 0
    numeroReserva = 0

    def __init__(self, cantidadAlumnos, cantidadAlumnosConfirmada, duracionEstimada, fechaCreacion, fechaHoraReserva, horaFinReal, horaInicioReal, numeroReserva, empleado, exposicion, sede, cambiosEstados):
 
        self.cantidadAlumnos = cantidadAlumnos
        self.cantidadAlumnosConfirmada = cantidadAlumnosConfirmada
        self.duracionEstimada = duracionEstimada
        self.fechaCreacion = fechaCreacion
        self.fechaHoraReserva = fechaHoraReserva
        self.horaFinReal = horaFinReal
        self.horaInicioReal = horaInicioReal
        self.numeroReserva = numeroReserva
        self.empleado = empleado
        self.exposicion = exposicion
        self.sede = sede
        self.cambiosEstados = cambiosEstados


    def conocerAsignacionGuia(self):
        pass 

    def conocerCambioEstado(self):
        pass

    def conocerEmpleado(self):
        return self.empleado

    def conocerEscuela(self):
        pass

    def conocerExposición(self):
        return self.exposicion

    def conocerSede(self):
        return self

    def esParaFechaYHora(duracionEstimada,sede_actual, fecha):
        #obtiene todas las reservas de la BD
        reservas = CapaConexion.obtenerReservas()
        reservasObj = []
        #por cada reserva obtenida, instancia el objeto y almacena si pertenece a la sede y es de la fecha y hora actual
        for row in reservas:
            
            objeto = ReservaVisita(row[6], row[7], duracionEstimada, row[1], row[2], row[5], row[4], row[0], 'NULL', 'NULL', row[8], 'NULL')      
         
            if ( objeto.horaInicioReal < (datetime.time(fecha)) < objeto.horaFinReal) and ((datetime.date(fecha)) == (datetime.date(objeto.fechaCreacion)) and objeto.sede == sede_actual):
            
                reservasObj.append(objeto)
        #retorna el vector de objetos con reservas para la fecha y hora estimada
        return reservasObj

    def getCantidadAlumnosConfirmados(reservasObj, estadoConfirmado):
        #para cada reserva que viene por parametro, busca su cantidad de alumnos confirmada y lo suma al contador
        #estado = Cambio_Estado.getCambiosEstado(actual_cambio_estado)
        cantidadAlumnosConfirmada = 0
        for reserva in reservasObj:
            #busca el estado actual de la reserva
            actual_cambio_estado = Cambio_Estado.esEstadoActual(reserva)          
            if actual_cambio_estado.estado == estadoConfirmado.id:
                #si el estado de esta reserva es Confirmada, suma su cantidad de alumnos confirmada
                cantidadAlumnosConfirmada =+ reserva.cantidadAlumnosConfirmada        
        #despues de recorrer todas las reservas de la fecha, retorna la cantidad sumada total
        return cantidadAlumnosConfirmada
        
