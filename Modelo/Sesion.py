from Modelo.Usuario import Usuario
from BaseDeDatos.CapaConexion import *

class Sesion():

    #atributos de la clase Sesion
    empleadoSesion = ''
    fechaFin = ''
    fechaInicio = ''
    horaFin = ''
    horaInicio = ''
    usuario = ''
  
    
    def __init__(self, empleadoSesion, fechaFin, fechaInicio, horaFin, horaInicio, usuario):
        #constructor del objeto Sesion
        self.empleadoSesion = empleadoSesion
        self.fechaFin = fechaFin
        self.fechaInicio = fechaInicio
        self.horaFin = horaFin
        self.horaInicio = horaInicio
        self.usuario = usuario
    

    def conocerUsuario(self, usuario):
        #metodo para retornar el usuario de la Sesion
        usuario.getUsuarios()

    def getEmpleadoenSesion():
        #obtener todas las sesiones de la BD y crear sus objetos
        sesionesBd = obtenerSesionesBd()
        for sesion in sesionesBd:
            sesionObj = Sesion(None, sesion[2], sesion[1], sesion[4], sesion[3], sesion[0])
            if sesionObj.fechaFin == None:
                sesionActiva = sesionObj
        
        #para la sesion activa busca el usuario de la misma, lo define como atributo de la Sesion
        # y retorna la sede
        sedeEmpleado, usuario = Usuario.getUsuario(sesionActiva)
        sesionActiva.empleadoSesion = usuario.nombre
        return sedeEmpleado



