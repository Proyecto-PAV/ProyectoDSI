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

    def getObra(self, nombre_expo):
        #buscar todos los detalles de esa expo
        detalles = CapaConexion.obtenerDetalleExposiciones(nombre_expo)
        #instanciar los objetos y sumar la duracion de esta exposicion
        detalles_obj =[]
        duracion_resumida = 0
        for d in detalles:
            detalle = Detalle_Exposicion(d[2], d[1], d[0])
            detalles_obj.append(detalle)
            #obtener duracion resumida de la obra del detalle -corroborar con el POO
            duracion_resumida += Obra.getDuracionResumida(d[1])
        
        return duracion_resumida



    #para mi este metodo no va
    def getDetalleExposicion(self, exposiciones):
        pass