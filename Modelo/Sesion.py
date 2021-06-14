
from Modelo.Usuario import *
from BaseDeDatos import CapaConexion

class Sesion():
    
    empleadoSesion = ''
    fechaFin = ''
    fechaInicio = ''
    horaFin = ''
    horaInicio = ''


    def __init__(self, empleadoSesion, fechaFin, fechaInicio, horaFin, horaInicio):
        self.empleadoSesion = empleadoSesion
        self.fechaFin = fechaFin
        self.fechaInicio = fechaInicio
        self.horaFin = horaFin
        self.horaInicio = horaInicio
    

    def conocerUsuario(usuario):
        usuario.getUsuarios()

    def getEmpleadoenSesion():
        #obtener las sesiones que no tengan fecha fin
            
        usuarioSesion = CapaConexion.ObtenerSesionActiva()
        sedeEmpleado = usuario.getUsuario(usuarioSesion)

        return sedeEmpleado
