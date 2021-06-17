from BaseDeDatos.CapaConexion import *
#from Modelo.Entrada import *

class Entrada():
    
    def __init__(self, numero, fechaVenta, horaVenta, monto, id_tipo_entrada, id_tipo_visita, nombre_sede, dni_guia):
        self.numero = numero
        self.fechaVenta = fechaVenta
        self.horaVenta = horaVenta
        self.monto = monto
        self.id_tipo_entrada = id_tipo_entrada
        self.id_tipo_visita = id_tipo_visita
        self.nombre_sede = nombre_sede
        self.dni_guia = dni_guia
        
        
nombre_sede = 'Museo Telon'

ultimo = getNro(nombre_sede)


print(ultimo)