
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
    
    def esAmbitoObra(self):
        pass

    def esPendienteAsigDeposito(self):
        pass

    def getEstadoReservaConfirmada(self):
        pass
