from BaseDeDatos import CapaConexion

class Estado():

    #atributos de la clase Estado
    ambito = ''
    descripcion = ''
    nombre = ''
    id=0

    def __init__(self, ambito, descripcion, nombre, nro_id):
         #constructor del objeto Estado
        self.ambito = ambito
        self.descripcion = descripcion
        self.nombre = nombre
        self.id = nro_id

    def esAmbitoObra(self):
        pass

    def esPendienteAsigDeposito(self):
        pass

    def getEstadoReservaConfirmada(self, estadoConfirmado):
        if self.nombre == estadoConfirmado.nombre:
            return True
        else:
            return False

    def esAmbitoReservaVisita(self):
        if self.ambito == "ReservaVisita":
            return True
        else:
            return False

    def esConfirmada(self):
        if self.nombre == 'Confirmado':
            return True
        else:
            return False
       


    
