from Modelo.Tipo_visita import *
from Modelo.Tipo_Entrada import *
from BaseDeDatos import CapaConexion

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
   
     
    def conocerTipoEntrada(self, entrada):
        nombre_entrada= TipoEntrada.getTipoEntrada(entrada)
        return nombre_entrada

    def conocerTipoVisita(self, visita):
        nombre_visita = TipoVisita.getTipoVisita(visita)
        return nombre_visita

    def esVigente(nombre_sede, fecha):

        t_vigentes = CapaConexion.ObtenerTarifasEnVigencia(nombre_sede, fecha)

        return t_vigentes       


    def getMonto(self, tarifas):
        #por cada fila devuelta en la matriz de 2 columnas y n filas,
        # buscamos el tipo de entrada y visita y obtenemos su monto para printear
        v = []
        for row in tarifas:
            tipo_entrada = self.conocerTipoEntrada(row[0] )
            tipo_visita = self.conocerTipoVisita(row[1] )
            monto = CapaConexion.ObtenerMonto(row[0], row[1])
            v.append(tipo_entrada, tipo_visita, monto)
        
        return v
        