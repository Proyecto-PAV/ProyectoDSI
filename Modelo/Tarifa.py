from Modelo.Tipo_Entrada import TipoEntrada
from Modelo.Tipo_visita import TipoVisita
from BaseDeDatos.CapaConexion import *

class Tarifa():
    
    #atributos de la clase Tarifa
    fechaFinVigencia = ""
    fechaInicioVifencia = ""
    monto = 0
    

    def __init__(self, fechaFinVigencia, fechaInicioVifencia, monto, tipo_entrada, tipo_visita):
         #constructor del objeto Tarifa
        self.fechaFinVigencia = fechaFinVigencia
        self.fechaInicioVifencia = fechaInicioVifencia
        self.monto = monto
        self.tipo_entrada = tipo_entrada
        self.tipo_visita = tipo_visita
   
    def str(self):
        return "fechaFinVigencia: ", self.fechaFinVigencia, "fechaInicioVifencia: ", self.fechaInicioVifencia, "monto: ", self.monto, "tipo entrada: ", self.tipo_entrada, "tipo visita: ", self.tipo_visita
     
    def conocerTipoEntrada(self, tipo_entrada):
        #le mando por parametro el numero del tipo para q me devuelva el nombre
        nombre_entrada = TipoEntrada.getTipoEntrada(tipo_entrada)
        return nombre_entrada


    def conocerTipoVisita(self, visita):
        nombre_visita = TipoVisita.getTipoVisita(visita)
        return nombre_visita


    def getMonto(self):
        #obtiene los objetos tipo entrada y tipo visita de la tarifa y almacena en sus atributos
        tEntrada = self.conocerTipoEntrada(self.tipo_entrada)
        tVisita = self.conocerTipoVisita(self.tipo_visita)
        self.tipo_entrada = tEntrada
        self.tipo_visita = tVisita

    def esVigente(nombre_sede, fecha):
        #busca todas las tarifas de la BD
        tarifasBd = obtenerTarifas()
        t_vigentes_obj = []
        for tarifa in tarifasBd:
            #por cada tarifa obtenida crea su objeto
            objTarifa = Tarifa(tarifa[3], tarifa[4], tarifa[5], tarifa[0], tarifa[1])
            # si el objeto tarifa es de la sede y la fecha pasada por parametro, lo guarda en el vector 
            if (tarifa[2] == nombre_sede) and (datetime.date(fecha) > objTarifa.fechaInicioVifencia) and (datetime.date(fecha) < objTarifa.fechaFinVigencia):
                t_vigentes_obj.append(objTarifa)

        #retorna el vector de objeto tarifa que estan vigentes y son de la sede pasada por parametros
        return t_vigentes_obj  
 

 
    
    
        



