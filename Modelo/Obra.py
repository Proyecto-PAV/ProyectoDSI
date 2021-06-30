from BaseDeDatos import CapaConexion


class Obra():
    
     #atributos de la clase Obra
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
    empleado = []
    cambioEstado = []

    def __init__(self, alto, ancho, codigoSensor, descripcion, duracionExtendida, duracionResumida, fechaCreacion, fechaPrimerIngreso, nombreObra, peso, valuacion, empleado, cambioEstado):
        #constructor del objeto Obras
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
        self.empleado = empleado
        self.cambioEstado = cambioEstado
   
    def conocerArtista(self):
        pass
    
    def conocerCambioEstado(self):
        return self.cambioEstado
    
    def conocerCompra(self):
        pass
    
    def conocerDonacion(self):
        pass
    
    def conocerEmpleado(self):
        return self.empleado
    
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
    
    def getDuracionResumida(self):
        #devuelve la duracion resumida de la obra
        return self.duracionResumida

    def getDuracionExtendida(self):
        #devuelve la duracion extendida de la obra
        return self.duracionExtendida
    