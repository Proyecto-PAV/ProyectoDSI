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
    
    def getDuracionResumida(nombre_obra):
        #obtenemos todas las obras
        obras = CapaConexion.getDuracionResumidaObra()
        #creamos los objetos obras hasta encontrar la que nos pasa por parametro y obtenemos su duracion
        for obra in obras:
            obj = Obra(obra[2],obra[3],obra[9],obra[4],obra[5],obra[6],obra[7],obra[8],obra[0],obra[1],obra[11])
            if obj.nombreObra==nombre_obra:
                return obj.duracionResumida

    