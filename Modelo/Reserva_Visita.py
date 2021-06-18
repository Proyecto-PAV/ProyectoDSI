from BaseDeDatos import CapaConexion
from datetime import datetime, timedelta
from Modelo.Cambio_estado import Cambio_Estado
import time

class ReservaVisita():

    cantidadAlumnos = 0
    cantidadAlumnosConfirmada = 0
    duracionEstimada = 0 
    fechaCreacion = ""
    fechaHoraReserva = ""
    horaFinReal = 0
    horaInicioReal = 0
    numeroReserva = 0

    def __init__(self, cantidadAlumnos, cantidadAlumnosConfirmada, duracionEstimada, fechaCreacion, fechaHoraReserva, horaFinReal, horaInicioReal, fechaReal, numeroReserva, empleado, exposicion, sede):
       #!TUVIMOS QUE AGREGAR Y CAMBIAR ATRIBUTOS: fechaReal
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

    def esParaFechaYHora(duracionEstimada,sede_actual):
        reservas = CapaConexion.obtenerReservas()
        reservasObj = []
        for row in reservas:
            objeto = ReservaVisita(row[6], row[7], duracionEstimada, row[1], row[2], row[4], row[5], row[0], 'NULL', 'NULL', row[8])      
         
            if (row[4] < (datetime.now().time()) < row[5]) and ((datetime.today().date()) == row[5] and row[8] == sede_actual):
            
                reservasObj.append(objeto)
    
        return reservasObj

    def getCantidadAlumnosConfirmados(reservasObj):
        cantidadAlumnosConfirmada = 0
        for i in range(0, len(reservasObj)):          
            cantidadAlumnosConfirmada =+ reservasObj[i].cantidadAlumnosConfirmada        
        return cantidadAlumnosConfirmada

        
