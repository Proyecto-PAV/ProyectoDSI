from Modelo import Tipo_Entrada
from Modelo import Tipo_visita
class Tarifa():
    
    fechaFinVigencia = ""
    fechaInicioVigencia = ""
    monto = 0

    def __init__(self, fechaFinVigencia, fechaInicioVifencia, monto):
        self.fechaFinVigencia = fechaFinVigencia
        self.fechaInicioVigencia = fechaInicioVigencia
        self.monto = monto
    
    
    def conocerTipoEntrada(self, entrada):
        
        Tipo_Entrada.getTipoEntrada(entrada)
    
    
    def conocerTipoVisita(self, visita):
        
        Tipo_visita.getTipoVisita(visita)
    
    def esVigente(self, fecha):
        
        if fecha <= fechaFinVigencia and fecha >= fechaInicioVigencia:
            print ("La fecha esta en vigencia")
        else:
            print ("La fecha ingresada esta fuera de vigencia")
    
    
    def getMonto(self):
        return self.monto