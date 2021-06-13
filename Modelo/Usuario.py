from Modelo.Empleado import *

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
    
    def getUsuario(self):
        dni= self.getDNI(usuario)
        sede = Empleado.getSedeDondeTrabaja(dni)
        return sede

    
    def getDNI(nombreUsuario):
        #consutlar BD para obtener el dni
        dni=0
        return dni 
