from BaseDeDatos import CapaConexion

class Estado():

    ambito = ''
    descripcion = ''
    nombre = ''

    def __init__(self, ambito, descripcion, nombre):
        self.ambito = ambito
        self.descripcion = descripcion
        self.nombre = nombre

    def esAmbitoObra(self):
        pass

    def esPendienteAsigDeposito(self):
        pass

    def getEstadoReservaConfirmada(cambios_estadosObj):
        estadosConfirmados = []
        for i in range(0, len(cambios_estadosObj)):
            if cambios_estadosObj[i].ambito == 'Confirmado':
                estadosConfirmados.append(cambios_estadosObj[i])
        return estadosConfirmados

    def esAmbitoReservaaVisita():
        estados_reservaVisita =  CapaConexion.obtenerEstadosReservaVisita()
       
        estados_reservaVisita_obj = []  
        for row in estados_reservaVisita:    
            objeto = Estado(row[1], row[2], row[3]) #? Con que atributo creamos el objeto
            if(row[1] == 'ReservaVisita'):
                estados_reservaVisita_obj.append(objeto)
        return estados_reservaVisita_obj

    def esConfirmada(estado_reservaVisitaObj):
        EstadosConfirmados = []
        for i in range(0, len(estado_reservaVisitaObj)):
            
            if estado_reservaVisitaObj[i].nombre == 'Confirmado':
               objeto = Estado(estado_reservaVisitaObj[i].ambito, estado_reservaVisitaObj[i].descripcion, estado_reservaVisitaObj[i].nombre)
               EstadosConfirmados.append(objeto)
               
        return EstadosConfirmados


    
