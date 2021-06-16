from Modelo.Tipo_Entrada import TipoEntrada
from Modelo.Tipo_visita import TipoVisita
from BaseDeDatos.CapaConexion import *

class Tarifa():
    
    fechaFinVigencia = ""
    fechaInicioVifencia = ""
    monto = 0
    #montoAdicionalGuia = 0

    def __init__(self, fechaFinVigencia, fechaInicioVifencia, monto, tipo_entrada, tipo_visita):
        self.fechaFinVigencia = fechaFinVigencia
        self.fechaInicioVifencia = fechaInicioVifencia
        self.monto = monto
        self.tipo_entrada = tipo_entrada
        self.tipo_visita = tipo_visita
   
    def str(self):
        return "fechaFinVigencia: ", self.fechaFinVigencia, "fechaInicioVifencia: ", self.fechaInicioVifencia, "monto: ", self.monto, "tipo entrada: ", self.tipo_entrada, "tipo visita: ", self.tipo_visita
     
    def conocerTipoEntrada(self, tipo_entrada):
        tipoEntrada = TipoEntrada(None, None)
        nombre_entrada = tipoEntrada.getTipoEntrada(tipo_entrada)
        return nombre_entrada

    def conocerTipoVisita(self, visita):
        tipoVisita = TipoVisita(None, None)
        nombre_visita = tipoVisita.getTipoVisita(visita)
        return nombre_visita

    def esVigente(self, nombre_sede, fecha):
        t_vigentes = ObtenerTarifasEnVigencia(nombre_sede, fecha)
        t_vigentes_obj = []
        for tarifa in t_vigentes:
            obj = Tarifa(None, None, None, tarifa[0], tarifa[1])
            t_vigentes_obj.append(obj)

        return t_vigentes_obj  

 
    def getMonto(self, ns):
            tEntrada = self.conocerTipoEntrada(self.tipo_entrada)
            tVisita = self.conocerTipoVisita(self.tipo_visita)
            monto = ObtenerMonto(self.tipo_entrada, self.tipo_visita, ns)
            self.monto = monto
            self.tipo_entrada = tEntrada
            self.tipo_visita = tVisita
    
        



