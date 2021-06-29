from datetime import datetime, time, timedelta
from Modelo import Obra
from BaseDeDatos import CapaConexion
from Modelo.Obra import *

class Detalle_Exposicion():

     #atributos de la clase DetalleExposicion
    lugarAsignado = ""
    obra = ""
    exposicion = ""

    def __init__(self, lugarAsignado, obra, exposicion):
        #constructor del objeto DetalleExposicion
        self.lugarAsignado = lugarAsignado
        self.obra = obra
        self.exposicion = exposicion

    def conocerObra(self):
        return self.obra

    def buscarDuracExtObra(self):
        pass

    def conocerPared(self):
        pass

    def getObraResumida(self):
        #levantar todas las Obras de la BD
        obras = CapaConexion.getObras()
        #creamos los objetos obras hasta encontrar la que nos pasa por parametro y obtenemos su duracion
        for obra in obras:
            obj = Obra(obra[2],obra[3],obra[9],obra[4],obra[5],obra[6],obra[7],obra[8],obra[0],obra[1],obra[11], None, None)
            if self.obra == obj.nombreObra:
                #obtener duracion resumida de la obra del detalle y separar sus unidades
                tiempo = obj.getDuracionResumida()
                #convertir el formato a int en minutos
                t_obra = self.convertirMinutos(tiempo)
                #retornamos la duracion en minutos
                return t_obra

    def getObraExtendida(self):
        #levantar todas las Obras de la BD
        obras = CapaConexion.getObras()
        #creamos los objetos obras hasta encontrar la que nos pasa por parametro y obtenemos su duracion
        for obra in obras:
            obj = Obra(obra[2],obra[3],obra[9],obra[4],obra[5],obra[6],obra[7],obra[8],obra[0],obra[1],obra[11], None, None)
            if self.obra == obj.nombreObra:
                #obtener duracion resumida de la obra del detalle y separar sus unidades
                tiempo = obj.getDuracionExtendida()
                #convertir el formato a int en minutos
                t_obra = self.convertirMinutos(tiempo)
                #retornamos la duracion en minutos
                return t_obra

    def convertirMinutos(t_obra):
        #convierte el tiempo h/m/s a minutos
        t_str = t_obra.strftime('%H:%M:%S')
        t_vec = t_str.split(":")
        hh = int(t_vec[0])
        mm = int(t_vec[1])
        ss = int(t_vec[2])
        tiempo_final_min = hh*60 + mm + (ss/60)
        return tiempo_final_min
         

