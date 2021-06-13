from Modelo.Empleado import *
from BaseDeDatos import CapaConexion


class usuario():

    caducidad = ''
    contraseña = ''
    nombre = ''
    usuarioLogueado = False

    def __init__(self, caducidad, contraseña, nombre, usuarioLogueado, dni):
        self.caducidad = caducidad
        self.contraseña = contraseña
        self.nombre = nombre
        self.usuarioLogueado = usuarioLogueado
        self.dni = dni
    
    def getUsuario(nombreUsuario):
        dni= CapaConexion.ObtenerDniUsuario(nombreUsuario)
        sede = Empleado.getSedeDondeTrabaja(dni)
        return sede


