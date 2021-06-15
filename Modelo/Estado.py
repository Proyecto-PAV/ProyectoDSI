from BaseDeDatos import CapaConexion
class estado():

    ambito = ''
    descripcion = ''
    nombre = ''

    def __init__(self, ambito, descripcion, nombre):
        self.ambito = ambito
        self.descripcion = descripcion
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
            objeto = Estado('ReservaVisita', None, None) #? Con que atributo creamos el objeto
            estados_reservaVisita_obj.append(objeto)

        return estados_reservaVisita_obj


    def esPendienteAsigDeposito(self, nombre):
        if nombre == 'PendienteAsigDeposito':
            return True
        else:
            return False

    def esAmbitoReservaVisita(self):
        estados_reservaVisita =  CapaConexion.obtenerEstadosReservaVisita()
        estados_reservaVisita_obj = []
        for row in estados_reservaVisita():    
            objeto = Estado(row[1], row[2],row[3]) 
            estados_reservaVisita_obj.append(objeto)
            
        return estados_reservaVisita_obj

    def esConfirmada(self, estadosReservaVisita):
        estadosConfirmados = []
        for i in estadosReservaVisita:
            if i[3] == 'Confirmado':
                estadosConfirmados.append(estadosReservaVisita[i])
        return estadosConfirmados
