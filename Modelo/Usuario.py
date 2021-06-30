from Modelo.Empleado import Empleado
from BaseDeDatos.CapaConexion import *


class Usuario():
    #atributos de la clase Usuario
    caducidad = ''
    contraseña = ''
    nombre = ''
    usuarioLogueado = False
    empleado = ''

    def __init__(self, caducidad, contraseña, nombre, usuarioLogueado, dni, empleado):
        #constructor del objeto Usuario
        self.caducidad = caducidad
        self.contraseña = contraseña
        self.nombre = nombre
        self.usuarioLogueado = usuarioLogueado
        self.dni = dni
        self.empleado = empleado

    def conocerEmpleado():
        pass
    
    def getUsuario(self):
        #Para el usuario cuya sesion coincide con la pasada por parametro solicita su sede
        empleadosBd = obtenerEmpleados()
        for e in empleadosBd:
            empleadoObj = Empleado(e[2], e[3], e[6], e[1], e[0], e[7], e[8], e[9], e[10], e[11], e[4], e[5])
            if empleadoObj.dni == self.dni:
                emp = empleadoObj
        sede = emp.getSedeDondeTrabaja()
        return sede


