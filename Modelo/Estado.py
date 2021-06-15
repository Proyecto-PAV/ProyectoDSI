

class Estado():

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

    def esAmbitoReservaaVisita():
        estados_reservaVisita =  ObtenerEstadosReservaVisita()
        print(estados_reservaVisita)
        print("hola")
        estados_reservaVisita_obj = []
        for i in estados_reservaVisita():    
            objeto = Estado('ReservaVisita', None, None, None) #? Con que atributo creamos el objeto
            estados_reservaVisita_obj.append(objeto)
            
        return estados_reservaVisita_obj

    
if __name__ == "__main__":
    Estado.esAmbitoReservaaVisita()