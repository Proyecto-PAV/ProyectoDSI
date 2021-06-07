
class estado():

    ambito = ''
    descripcion = ''
    estadoReserva = ''
    nombre = ''

    def __init__(self, ambito, descripcion, estadoReserva, nombre):
        self.ambito = ambito
        self.descripcion = descripcion
        self.estadoReserva = estadoReserva
        self.nombre = nombre
    
    def esAmbitoObra(ambito):
        if ambito == 'Obra':
            return True
        else:
            return False

    def esAmbitoReservaVisita(ambito):
        if ambito == 'Reserva Visita':
            return True
        else:
            return False

    def esConfirmada(estadoReserva):
        if estadoReserva == 'Confirmada':
            return True
        else:
            return False

    def esPendienteAsigDeposito(nombre):
        if nombre == 'PendienteAsigDeposito':
            return True
        else:
            return False

    def getEstadoReservaConfirmada(estadoReserva):
        if estadoReserva == 'Confirmada':
            return estadoReserva
        else:
            pass
