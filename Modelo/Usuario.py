from Modelo.Empleado import Empleado
from BaseDeDatos.CapaConexion import obtenerUsuariosBd
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
    
    def getUsuario(sesionActiva):
        #busca todos los usuarios en la BD y crea sus objetos
        usuariosBd = obtenerUsuariosBd()
        for usuario in usuariosBd:
            usuarioObj = Usuario(usuario[1], usuario[2], usuario[0], usuario[3], usuario[4], None)
            if usuarioObj.nombre == sesionActiva.usuario:
                usu = usuarioObj

        #Para el usuario cuya sesion coincide con la pasada por parametro solicita su sede
        empleado = Empleado.getSedeDondeTrabaja(usu)
        usu.empleado = empleado
        return empleado.sedeDondeTrabaja, usu


