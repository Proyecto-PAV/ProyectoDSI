from BaseDeDatos import CapaConexion

class Estado():

    ambito = ''
    descripcion = ''
    nombre = ''

    def __init__(self, ambito, descripcion, estadoReserva, nombre):
        self.ambito = ambito
        self.descripcion = descripcion
        self.nombre = nombre


    def esAmbitoObra(self):
        pass

    def esPendienteAsigDeposito(self):
        pass

    def getEstadoReservaConfirmada(self):
        pass

    def esAmbitoReservaaVisita():
        
        estados_reservaVisita =  CapaConexion.obtenerEstadosReservaVisita()
        
        estados_reservaVisita_obj = []
        for row in estados_reservaVisita():    
            objeto = Estado(row[1], row[2],row[3]) #? Con que atributo creamos el objeto
            estados_reservaVisita_obj.append(objeto)
            
        return estados_reservaVisita_obj

    def esConfirmada(estado_reservaVisita):
        pass

    
