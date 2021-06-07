
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

    def getCambiosEstado(self):
        pass

    def new(self, estado, fechaHoraInicio, fechaHoraFin):
        return Cambio_Estado(self, estado, fechaHoraInicio, fechaHoraFin)

    def esEstadoActual(self):
        if self.fechaHoraFin == '':
            return True
        else:
            return False
