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

    def getEstadoReservaConfirmada(cambio_estadoObj):
        estadosConfirmados = []
        for i in range(0, len(cambio_estadoObj)):
            if cambio_estadoObj[i].ambito == 'Confirmado':
                estadosConfirmados.append(cambio_estadoObj[i])
        return estadosConfirmados

    def esAmbitoReservaVisita():
        #Busca en la BD todos los estados de Reserva Visita
        estados_reservaVisita =  CapaConexion.obtenerEstadosReservaVisita()
        #por cada estado obtenido, crea su objeto y si pertenece a la clase reservaVisita lo almacena
        estados_reservaVisita_obj =[]
        for row in estados_reservaVisita:    
            objeto = Estado(row[1], row[2], row[3], row[0]) 
            if(row[1] == 'ReservaVisita'):
                estados_reservaVisita_obj.append(objeto)
        #devuelve el vector con los objetos de ReservaVisita
        return estados_reservaVisita_obj

    def esConfirmada(estado_reservaVisitaObj):
        #Almacena todos los estados confirmados, si es que hay, de la ReservaVisita
       
        for i in range(0, len(estado_reservaVisitaObj)):
            
            if estado_reservaVisitaObj[i].nombre == 'Confirmado':
                objeto = Estado(estado_reservaVisitaObj[i].ambito, estado_reservaVisitaObj[i].descripcion, estado_reservaVisitaObj[i].nombre)
                #devuelve el objeto confirmado
                return objeto
       


    
