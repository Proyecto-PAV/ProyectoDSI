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

    def getEmpleadoenSesion(self):
        #para la sesion activa busca el usuario de la misma, lo define como atributo de la Sesion
        # y retorna la sede
        usuariosBd = obtenerUsuariosBd()
        for usuario in usuariosBd:
            usuarioObj = Usuario(usuario[1], usuario[2], usuario[0], usuario[3], usuario[4], None)
            if usuarioObj.nombre == self.usuario:
                usu = usuarioObj
        self.empleadoSesion = usu.nombre
        sedeEmpleado = usu.getUsuario()
        return sedeEmpleado



