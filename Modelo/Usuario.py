from Modelo.Empleado import Empleado
from BaseDeDatos.CapaConexion import ObtenerDniUsuario


class Usuario():

    caducidad = ''
    contraseña = ''
    nombre = ''
    usuarioLogueado = False
    empleado = ''

    def __init__(self, caducidad, contraseña, nombre, usuarioLogueado, dni, empleado):
        self.caducidad = caducidad
        self.contraseña = contraseña
        self.nombre = nombre
        self.usuarioLogueado = usuarioLogueado
        self.dni = dni
        self.empleado = empleado
    
    def getUsuario(self, nombreUsuario):
        dni = ObtenerDniUsuario(nombreUsuario)
        self.empleado = Empleado(None, None, None, None, dni, None, None, None, None, None, None, None)
        sede = self.empleado.getSedeDondeTrabaja(dni)

        #!no es necesario 
        self.empleado.sedeDondeTrabaja = sede
        return sede


