from Modelo.Tipo_Entrada import TipoEntrada
from Modelo.Tipo_visita import TipoVisita
from BaseDeDatos.CapaConexion import *

class Tarifa():
    
    #atributos de la clase Tarifa
    fechaFinVigencia = ""
    fechaInicioVifencia = ""
    monto = 0
    tipo_entrada = []
    tipo_visita = []
    

    def __init__(self, fechaFinVigencia, fechaInicioVifencia, monto, tipo_entrada, tipo_visita):
         #constructor del objeto Tarifa
        self.fechaFinVigencia = fechaFinVigencia
        self.fechaInicioVifencia = fechaInicioVifencia
        self.monto = monto
        self.tipo_entrada = tipo_entrada
        self.tipo_visita = tipo_visita
   
    def str(self):
        return "fechaFinVigencia: ", self.fechaFinVigencia, "fechaInicioVifencia: ", self.fechaInicioVifencia, "monto: ", self.monto, "tipo entrada: ", self.tipo_entrada, "tipo visita: ", self.tipo_visita
     
    def conocerTipoEntrada(self):
        #traemos todos los tipos de entrada de la BD
        tiposEntrasdasBd = obtenerTiposEntradas()
        for tipo in tiposEntrasdasBd:
            tE = TipoEntrada(tipo[1], tipo[0])
            #Si el tipo entrada creado coincide con el pasado por el parametro lo retorna
            if  self.tipo_entrada == tE.tipoEntrada:
                nombre_entrada = tE.getTipoEntrada()
                return nombre_entrada


    def conocerTipoVisita(self):
        #traemos todos los tipos de visita de la BD
        tiposVisitasBd = obtenerNombreVisita()
        for tipo in tiposVisitasBd:
            tV = TipoVisita(tipo[1], tipo[0])
            #Si el tipo visita creado coincide con el atributo del tipo de visita del ojeto que lo llama lo retorna
            if self.tipo_visita == tV.tipoVisita:
                nombre_visita = tV.getTipoVisita()
                return nombre_visita


    def getMonto(self):
        #esta funcio obtiene los nombres de los tipos 
            tEntrada = self.conocerTipoEntrada()
            tVisita = self.conocerTipoVisita()
            self.tipo_entrada = tEntrada
            self.tipo_visita = tVisita

    def esVigente(self, fecha):
        if ((datetime.date(fecha) > self.fechaInicioVifencia) and (datetime.date(fecha) < self.fechaFinVigencia)):
            return True
        else:
            return False  
 
 

 
    
    
        



