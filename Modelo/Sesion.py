
from Modelo.Usuario import Usuario
from BaseDeDatos.CapaConexion import *

class Sesion():

    empleadoSesion = ''
    fechaFin = ''
    fechaInicio = ''
    horaFin = ''
    horaInicio = ''
    usuario = ''
  

    def __init__(self, empleadoSesion, fechaFin, fechaInicio, horaFin, horaInicio, usuario):
        self.empleadoSesion = empleadoSesion
        self.fechaFin = fechaFin
        self.fechaInicio = fechaInicio
        self.horaFin = horaFin
        self.horaInicio = horaInicio
        self.usuario = usuario
    

    def conocerUsuario(self, usuario):
        usuario.getUsuarios()

    def getEmpleadoenSesion():
        #obtener las sesiones que no tengan fecha fin
        sesionesBd = obtenerSesionesBd()
        for sesion in sesionesBd:
            sesionObj = Sesion(None, sesion[2], sesion[1], sesion[4], sesion[3], sesion[0])
            if sesionObj.fechaFin == None:
                sesionActiva = sesionObj
        
        sedeEmpleado, usuario = Usuario.getUsuario(sesionActiva)
        sesionActiva.empleadoSesion = usuario.nombre
        return sedeEmpleado



