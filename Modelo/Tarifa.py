from Modelo.Tipo_visita import *
from Modelo.Tipo_Entrada import *
from BaseDeDatos import CapaConexion

class Tarifa():
    
    fechaFinVigencia = ""
    fechaInicioVifencia = ""
    monto = 0
    montoAdicionalGuia = 0

    def __init__(self, fechaFinVigencia, fechaInicioVifencia, monto, montoAdicionalGuia, tipo_entrada, tipo_visita):
        self.fechaFinVigencia = fechaFinVigencia
        self.fechaInicioVifencia = fechaInicioVifencia
        self.monto = monto
        self.montoAdicionalGuia = montoAdicionalGuia
        #! aca faltan tipo entrada y tipo visita
        self.tipo_entrada = tipo_entrada
        self.tipo_entrada = tipo_visita
   
     
    def conocerTipoEntrada(self, entrada):
        nombre_entrada= TipoEntrada.getTipoEntrada(entrada)
        return nombre_entrada

    def conocerTipoVisita(self, visita):
        nombre_visita = TipoVisita.getTipoVisita(visita)
        return nombre_visita

    def esVigente(nombre_sede, fecha):
        #?aca se podria dvolver una coleccion de objetos en vez de devolver una matriz
        #?creando objeto por objeto mediante por ejemplo un for
        t_vigentes = CapaConexion.ObtenerTarifasEnVigencia(nombre_sede, fecha)
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
    

esVigente("Museo Telon", "2021-07-01")

