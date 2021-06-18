from datetime import datetime, time, timedelta
from Modelo import Obra
from BaseDeDatos import CapaConexion
from Modelo.Obra import *

class Detalle_Exposicion():

    lugarAsignado = ""
    obra = ""
    exposicion = ""

    def __init__(self, lugarAsignado, obra, exposicion):
        self.lugarAsignado = lugarAsignado
        self.obra = obra
        self.exposicion = exposicion

    def conocerObra(self):
        return self.obra

    def buscarDuracExtObra(self):
        pass

    def conocerPared(self):
        pass

    def getObra(nombre_expo):
        #buscar todos los detalles de esa expo
        detalles = CapaConexion.obtenerDetalleExposiciones()
        #instancia los objetos y suma la duracion de esta exposicion
        detalles_obj =[]
        # creacion del contador en tipo hh/mm/ss para contar el tiempo de la obra
        duracion_resumida = 0
        #comienzo del ciclo
        for d in detalles:
            detalle = Detalle_Exposicion(d[2], d[1], d[0])
            detalles_obj.append(detalle)
            #obtener duracion resumida de la obra del detalle y separar sus unidades
            tiempo = Obra.getDuracionResumida(detalle.obra)
            #convertir el formato a int en minutos
            t_obra = Detalle_Exposicion.convertirMinutos(tiempo)
            #sumar al contador de minutos
            duracion_resumida = duracion_resumida + t_obra
        
        #retornamos la duracion en minutos
        return duracion_resumida


    def convertirMinutos(t_obra):
        #convierte el tiempo h/m/s a minutos
        t_str = t_obra.strftime('%H:%M:%S')
        t_vec = t_str.split(":")
        hh = int(t_vec[0])
        mm = int(t_vec[1])
        ss = int(t_vec[2])
        tiempo_final_min = hh*60 + mm + (ss/60)
        return tiempo_final_min
         


    #para mi este metodo no va
    def getDetalleExposicion(self, exposiciones):
        pass