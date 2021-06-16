#from Modelo import Tipo_Entrada
from BaseDeDatos import CapaConexion


class Obra():
    
    alto = 0
    ancho = 0
    codigoSensor = 0
    descripcion = ""
    duracionExtendida = 0.0
    duracionResumida = 0.0
    fechaCreacion = ""
    fechaPrimerIngreso = ""
    nombreObra = ""
    peso = 0
    valuacion = 0

    def __init__(self, alto, ancho, codigoSensor, descripcion, duracionExtendida, duracionResumida, fechaCreacion, fechaPrimerIngreso, nombreObra, peso, valuacion):
        self.alto = alto
        self.ancho = ancho
        self.codigoSensor = codigoSensor
        self.descripcion = descripcion
        self.duracionExtendida = duracionExtendida
        self.duracionResumida = duracionResumida
        self.fechaCreacion = fechaCreacion
        self.fechaPrimerIngreso = fechaPrimerIngreso
        self.nombreObra = nombreObra
        self.peso = peso
        self.valuacion = valuacion
   
    def conocerArtista(self):
        pass
    
    def conocerCambioEstado(self):
        pass
    
    def conocerCompra(self):
        pass
    
    def conocerDonacion(self):
        pass
    
    def conocerEmpleado(self):
        pass
    
    def conocerEstilo(self):
        pass
    
    def conocerPrestamo(self):
        pass
    
    def conocerPrestamoAMuseo(self):
        pass
    
    def conocerRestauracion(self):
        pass
    
    def conocerSectorAsignado(self):
        pass
    
    def conocerTecnica(self):
        pass
    
    def conocerTematica(self):
        pass
    
    def conocerTipoIngreso(self):
        pass
    
    def crearCambioEstado(self):
        pass
    
    def getDuracionResumida(self, nombre_obra):
        obras = CapaConexion.getDuracionResumidaObra(nombre_obra)
        Obra(obras[2],obras[3],obras[9],obras[4],obras[5],obras[6],obras[7],obras[8],obras[0],obras[1],obras[11])
        return self.duracionResumida
    