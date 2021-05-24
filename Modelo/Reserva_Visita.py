class ReservaVisita:

    cantidadAlumnos = 0
    cantidadAlumnosConfirmada = 0
    duracionEstimada = 0 
    fechaHoraCreacion = ""
    fechaHoraReserva = ""
    horaFinReal = 0
    horaInicioReal = 0
    numeroReserva = 0

    def __init__(self, cantidadAlumnos, cantidadAlumnosConfirmada, duracionEstimada, fechaHoraCreacion, fechaHoraReserva, horaFinReal, horaInicioReal, numeroReserva):
        self.cantidadAlumnos = cantidadAlumnos
        self.cantidadAlumnosConfirmada = cantidadAlumnosConfirmada
        self.duracionEstimada = duracionEstimada
        self.fechaHoraCreacion = fechaHoraCreacion
        self.fechaHoraReserva = fechaHoraReserva
        self.horaFinReal = horaFinReal
        self.horaInicioReal = horaInicioReal
        self.numeroReserva = numeroReserva

    def conocerAsignacionGuia(self):
        pass 

    def conocerCambioEstado(self):
        pass

    def conocerEmpleado(self):
        pass

    def conocerEscuela(self):
        pass

    def conocerExposición(self):
        pass

    def conocerSede(self):
        pass

    def esParaFechaYHora(self):
        pass

    def getCantidadAlumnosConfirmados(self):
        pass
