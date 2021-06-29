
from BaseDeDatos import CapaConexion
from Modelo.Estado import *

class Cambio_Estado():
    #atributos de la clase Cambio_Estado
    estado = 0
    nroAmbito = 0
    fechaHoraFin = ""
    fechaHoraInicio = ""

    def __init__(self, estado, nro, fechaHoraFin, fechaHoraInicio):
         #constructor del objeto Cambio_Estado
        self.estado = estado
        self.nroAmbito = nro
        self.fechaHoraFin = fechaHoraFin
        self.fechaHoraInicio = fechaHoraInicio

    def conocerEstado(self):
        return self.estado

    def getCambiosEstado(self, cambio_estado):
        #busca todos los estados de la BD
        estados = CapaConexion.obtenerEstados()
        #crea los objetos estado y busca el estado confirmado y valida si la reserva esta Confirmada
        for est in estados:
            estado = Estado(est[1], est[2], est[3], est[0])
            if cambio_estado.estado == estado.id:
                rdo = estado.getEstadoReservaConfirmada(cambio_estado)
        return rdo

    def new(self, estado, fechaHoraInicio, fechaHoraFin):
        return Cambio_Estado(self, estado, fechaHoraInicio, fechaHoraFin)

    def esEstadoActual(self, nro):
        #retorna true si el estado de la reserva pasada por parametro es el actual
        if self.fechaHoraFin == None and self.nroAmbito==nro:
            return True 
        else:
            return False

    