
from BaseDeDatos import CapaConexion
from Modelo.Estado import *

class Cambio_Estado():
    #atributos de la clase Cambio_Estado
    estado = 0
    fechaHoraFin = ""
    fechaHoraInicio = ""

    def __init__(self, estado, fechaHoraFin, fechaHoraInicio):
         #constructor del objeto Cambio_Estado
        self.estado = estado
        self.fechaHoraFin = fechaHoraFin
        self.fechaHoraInicio = fechaHoraInicio

    def conocerEstado(self):
        return self.estado

    def getCambiosEstado(cambio_estadoObj):
        estados = Estado.getEstadoReservaConfirmada(cambio_estadoObj)
        return estados

    def new(self, estado, fechaHoraInicio, fechaHoraFin):
        return Cambio_Estado(self, estado, fechaHoraInicio, fechaHoraFin)

    def esEstadoActual(reserva):
        #obtener todos los cambios de estados de la BD
        cambios_estados = CapaConexion.obtenerCambiosEstados()
        #por cada cambio de estado lo crea como objeto y si no tiene fecha fin y coincide con el ambito ReservaVisita corta el ciclo y retorna
        for row in cambios_estados:
            objeto = Cambio_Estado(row[0], row[3], row[2])
            #retorna el objeto que no tiene fechaFin y que pertence a la reserva que se pasa por parametro
            #* se debe agregar el ambito a los atributos de Cambio estado? para poder hacer esta validacion
            if objeto.fechaHoraFin == None and objeto.nroAmbito==reserva.numeroReserva:
                return objeto

    