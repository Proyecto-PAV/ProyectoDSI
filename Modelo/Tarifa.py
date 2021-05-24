from Modelo import Tipo_Entrada
class Tarifa():
    
    fechaFinVigencia = ""
    fechaInicioVifencia = ""
    monto = 0
    montoAdicionalGuia = 0

    def __init__(self, fechaFinVigencia, fechaInicioVifencia, monto, montoAdicionalGuia):
        self.fechaFinVigencia = fechaFinVigencia
        self.fechaInicioVifencia = fechaInicioVifencia
        self.monto = monto
        self.montoAdicionalGuia = montoAdicionalGuia
   
    def conocerTipoEntrada(self):
        pass
    
    def conocerTipoVisita(self):
        pass
    
    def esVigente(self):
        pass
    
    def getAdicionalPorGuia(self):
        pass
    
    def getMonto(self):
        pass