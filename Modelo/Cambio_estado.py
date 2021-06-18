from BaseDeDatos import CapaConexion
from Modelo.Estado import *

class Cambio_Estado():
    estado = ""
    fechaHoraFin = ""
    fechaHoraInicio = ""

    def __init__(self, estado, fechaHoraFin, fechaHoraInicio):
        self.estado = estado
        self.fechaHoraFin = fechaHoraFin
        self.fechaHoraInicio = fechaHoraInicio

    def conocerEstado(self):
        return self.estado

    def getCambiosEstado(cambios_estadosObj):
        estados = Estado.getEstadoReservaConfirmada(cambios_estadosObj)
        return estados

    def new(self, estado, fechaHoraInicio, fechaHoraFin):
        return Cambio_Estado(self, estado, fechaHoraInicio, fechaHoraFin)

    def esEstadoActual():
        cambios_estados = CapaConexion.obtenerCambiosEstados()
        cambios_estadosObj = []
        for row in cambios_estados:
            print(row)
            objeto = Cambio_Estado(row[0], row[2], row[1])
            if row[2] == 'NULL':
                cambios_estadosObj.append(objeto)
                break
        return cambios_estadosObj

    