from BaseDeDatos.CapaConexion import *
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

    def esAmbitoReservaVisita():
        estados_reservaVisita = []
        print(estados_reservaVisita)
        estados_reservaVisita_obj = []
        for i in estados_reservaVisita():
            objeto = Estado('ReservaVisita', None, None, None) #? Con que atributo creamos el objeto
            estados_reservaVisita_obj.append(objeto)

        return estados_reservaVisita_obj

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
