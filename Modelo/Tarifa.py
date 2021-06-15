from Modelo.Tipo_visita import *
from Modelo.Tipo_Entrada import *
from BaseDeDatos.CapaConexion import ObtenerTarifasEnVigencia

class Tarifa():
    
    fechaFinVigencia = ""
    fechaInicioVifencia = ""
    monto = 0
    #montoAdicionalGuia = 0

    def __init__(self, fechaFinVigencia, fechaInicioVifencia, monto, tipo_entrada, tipo_visita):
        self.fechaFinVigencia = fechaFinVigencia
        self.fechaInicioVifencia = fechaInicioVifencia
        self.monto = monto
        #! aca faltan tipo entrada y tipo visita
        self.tipo_entrada = tipo_entrada
        self.tipo_entrada = tipo_visita
   
     
    def conocerTipoEntrada(self, entrada):
        self.tipo_entrada = TipoEntrada(None, None)
        nombre_entrada= self.tipoEntrada.getTipoEntrada(entrada)
        return nombre_entrada

    def conocerTipoVisita(self, visita):
        nombre_visita = TipoVisita.getTipoVisita(visita)
        return nombre_visita

    def esVigente(nombre_sede, fecha):
        t_vigentes = ObtenerTarifasEnVigencia(nombre_sede, fecha)
        t_vigentes_obj = []
        for row in t_vigentes:
            obj = Tarifa(None, None, None, None, row[0], row[1])
            t_vigentes_obj.append(obj)

        return t_vigentes_obj  


    def getMonto(self, tarifas):
        #por cada fila devuelta en la matriz de 2 columnas y n filas,
        # buscamos el tipo de entrada y visita y obtenemos su monto para printear
        v = []
        for entrada in t_vigentes_obj:
            tipo_entrada = self.conocerTipoEntrada(tarifa.tipo_entrada)
            
        for row in tarifas:
             #tipo_entrada = self.conocerTipoEntrada( row.tipo_entrada)
            tipo_entrada = self.conocerTipoEntrada(row[0] )
            tipo_visita = self.conocerTipoVisita(row[1] )
            monto = CapaConexion.ObtenerMonto(row[0], row[1])
            v.append(tipo_entrada, tipo_visita, monto)
        
        return v
    



