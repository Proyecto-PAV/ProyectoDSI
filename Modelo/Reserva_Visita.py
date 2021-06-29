from BaseDeDatos import CapaConexion
from datetime import datetime, timedelta
from Modelo.Cambio_estado import Cambio_Estado
import time

class ReservaVisita():

     #atributos de la clase ReservaVisita
    cantidadAlumnos = 0
    cantidadAlumnosConfirmada = 0
    duracionEstimada = 0 
    fechaCreacion = ""
    fechaHoraReserva = ""
    horaFinReal = 0
    horaInicioReal = 0
    numeroReserva = 0
    empleado = []
    exposicion = []
    sede = []
    cambiosEstados = []

    def __init__(self, cantidadAlumnos, cantidadAlumnosConfirmada, duracionEstimada, fechaCreacion, fechaHoraReserva, horaFinReal, horaInicioReal, numeroReserva, empleado, exposicion, sede, cambiosEstados):
        #constructor del objeto ReservaVisita
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

    def conocerExposicion(self):
        return self.exposicion

    def conocerSede(self):
        return self
    
    def convertirMinutos(tiempo):
        #convierte el tiempo h/m/s a minutos
        if isinstance(tiempo, str):
            t_vec = tiempo.split(":")
        else:
            t_str = tiempo.strftime('%H:%M:%S')
            t_vec = t_str.split(":")
        hh = int(t_vec[0])
        mm = int(t_vec[1])
        ss = int(t_vec[2])
        tiempo_final_min = hh*60 + mm + (ss/60)
        return tiempo_final_min

    def convertirTiempo(min):
        #convertir los minutos en 'h/m/s'
        hs = min/60
        ms = (hs - int(hs)) * 60
        ss = (ms - int(ms)) * 60
        hs = int(hs)
        ms = int(ms)
        ss = int(ss)
        tiempo_final = str(hs)+':'+str(ms)+':'+str(ss)
        return tiempo_final

    def esParaFechaYHora(self, duracionEstimada, fecha):
        #inicializacion de variables para determinar la franja horaria de la visita
        duracion = self.convertirMinutos(duracionEstimada)
        hora_de_fecha = datetime.time(fecha)
        fechaActualEnMinutos = self.convertirMinutos(hora_de_fecha)
        hora_fin = fechaActualEnMinutos + duracion
        hora_fin = self.convertirTiempo(hora_fin)
        #para la reserva, devuelvo True si es de este horario o False si no
        v_reserva = datetime.strftime(self.fechaHoraReserva, "%Y-%m-%d %H:%M:%S")
        fechaHoraReserva = v_reserva.split(" ")
        #                           Si no funciona cambiar por datetime.time(fecha)
        if ( self.horaInicioReal <= (hora_de_fecha) <= self.horaFinReal) and ((fecha) == (self.fechaCreacion)):
            return True
                # Si la reserva no inicio y esta reservada en el tiempo estimado de la venta de entrada Y           es una reserva de la fecha de hoy  
        elif ((str(self.horaInicioReal) <= hora_fin or fechaHoraReserva[1] <= hora_fin) and (fecha == self.fechaCreacion)): 
            return True
        else:
            return False

    def getCantidadAlumnosConfirmados(self, estadoConfirmado):
        #busca su cantidad de alumnos confirmada y lo retorna
        #busca entre todos los cambios de estado, el que coincide con el del parametro
        cambios_estados = CapaConexion.obtenerCambiosEstados()
        #p or cada cambio de estado lo crea como objeto 
        for row in cambios_estados:
            cambio = Cambio_Estado(row[0], row[1], row[3], row[2])
            #busca el estado actual de la reserva
            es_confirmada = cambio.esEstadoActual(self.numeroReserva)          
            if es_confirmada:
                actual = cambio
                break
        #para el estado actual de la reserva, determina si es Confirmado
        actual_confir = actual.getCambiosEstado(estadoConfirmado)      
        if actual_confir:
            #si es confirmado, suma la cantidad de alumnos confirmados de esta reserva
            cantidadAlumnosConfirmada = self.cantidadAlumnosConfirmada
            return cantidadAlumnosConfirmada
        else:
            #si no se devuelve 0
            return 0