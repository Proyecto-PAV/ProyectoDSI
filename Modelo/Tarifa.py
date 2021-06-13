from Modelo import Tipo_Entrada
from Modelo import Tipo_visita
class Tarifa():
    
    fechaFinVigencia = ""
    fechaInicioVigencia = ""
    monto = 0

    def __init__(self, fechaFinVigencia, fechaInicioVifencia, monto, tipo_entrada, tipo_visita):
        self.fechaFinVigencia = fechaFinVigencia
        self.fechaInicioVigencia = fechaInicioVigencia
        self.monto = monto
        self.tipo_entrada = Tipo_Entrada
        self.tipo_visita = Tipo_visita
    
    
    def conocerTipoEntrada(self, entrada):
        
        Tipo_Entrada.getTipoEntrada(entrada)
    
    
    def conocerTipoVisita(self, visita):
        
        Tipo_visita.getTipoVisita(visita)
    
    def esVigente(self, fecha):
        
        if fecha <= fechaFinVigencia and fecha >= fechaInicioVigencia:
            return True
        else:
            return False
    
    
    def getMonto(self):
        return self.monto