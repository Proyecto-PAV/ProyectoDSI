
from Modelo.Usuario import Usuario
from BaseDeDatos.CapaConexion import *

class Sesion():
    """
    empleadoSesion = ''
    fechaFin = ''
    fechaInicio = ''
    horaFin = ''
    horaInicio = ''
    usuario = ''
    """

    def __init__(self, empleadoSesion, fechaFin, fechaInicio, horaFin, horaInicio, usuario):
        self.empleadoSesion = empleadoSesion
        self.fechaFin = fechaFin
        self.fechaInicio = fechaInicio
        self.horaFin = horaFin
        self.horaInicio = horaInicio
        self.usuario = usuario
    

    def conocerUsuario(self, usuario):
        usuario.getUsuarios()

    def getEmpleadoenSesion(self):
        #obtener las sesiones que no tengan fecha fin
        #? probado no me tira error al acceder a la bd, al realizar el metodo obtener sesion activa
        #? para que esta el dni en sesion no iria solo en usuario?
        usuarioSesion = ObtenerSesionActiva()

        self.usuario = Usuario(None, None, usuarioSesion, None, None, None)
        sedeEmpleado = self.usuario.getUsuario(usuarioSesion)
        return sedeEmpleado
