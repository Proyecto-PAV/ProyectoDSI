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

    def getEstadoReservaConfirmada(cambio_estado, estadoConfirmado):
        #busca todos los estados de la BD
        estados = CapaConexion.obtenerEstados()
        #crea los objetos estado y busca el estado confirmado y valida si la reserva esta Confirmada
        for est in estados:
            estado = Estado(est[1], est[2], est[3], est[0])
            if estado.id == cambio_estado.nroAmbito and estado.id == estadoConfirmado.id:
                return True
        
        return False

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

        for estado_reserva in estado_reservaVisitaObj:

            if estado_reserva.nombre == 'Confirmado':
                objeto = Estado(estado_reserva.ambito, estado_reserva.descripcion, estado_reserva.nombre, estado_reserva.id)
                #devuelve el objeto confirmado
                return objeto
       


    
