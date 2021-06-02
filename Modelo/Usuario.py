from Modelo import Sesion
from Modelo import Exposicion
class usuario():

    caducidad = ''
    contraseña = ''
    nombre = ''
    usuarioLogueado = False

    def __init__(self, caducidad, contraseña, nombre, usuarioLogueado):
        self.caducidad = caducidad
        self.contraseña = contraseña
        self.nombre = nombre
        self.usuarioLogueado = usuarioLogueado
    
    def conocerEmpleado(self):
        pass

    def getEmpleadoenSesion(self, empleadoSesion):
        Sesion.getEmpleadoenSesion(empleadoSesion)
