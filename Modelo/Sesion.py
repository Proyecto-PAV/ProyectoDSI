from Modelo.Usuario import *


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
        #llamar a la clase usuario
        #obtener las sesiones que no tengan fecha fin
        #SELECT empleadoSesion FROM Sesiones WHERE FechaFIN IS NULL
        usuarioSesion=''
        sedeEmpleado = usuario.getUsuario(usuarioSesion)

        return sedeEmpleado
