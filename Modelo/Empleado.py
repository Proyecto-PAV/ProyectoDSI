from BaseDeDatos.CapaConexion import *

class Empleado():

    nombre = ""
    apellido = ""
    codigoValidacion = 0
    cuit = 00000000000
    dni = 00000000
    domicilio = ""
    fechaDeIngreso = ""
    mail = ""
    sedeDondeTrabaja = ""
    sexo = ""
    telefono = 0000000000

    def __init__(self, nombre, apellido, codValidacion, cuit, dni, domicilio, fechaDeIngreso, fechaNacimiento, mail, sedeDondeTrabaja, sexo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.codValidacion = codValidacion
        self.cuit = cuit
        self.dni = dni
        self.domicilio = domicilio
        self.fechaDeIngreso = fechaDeIngreso
        self.fechaNacimiento = fechaNacimiento
        self.mail = mail
        self.sedeDondeTrabaja = sedeDondeTrabaja
        self.sexo = sexo
        self.telefono = telefono

    def conocerCargo(self):
        pass
    def conocerHorario(self):
        pass
    
    """
    def getSedeDondeTrabaja(usuario):
        #consultar BD
        sedeDondeTrabaja = ObtenerSedeEmpleado(usuario.dni)
        return sedeDondeTrabaja
    """
    
    def getSedeDondeTrabaja(usuario):
        #consultar BD
        empleadosBd = ObtenerEmpleados()
        for e in empleadosBd:
            empleadoObj = Empleado(e[2], e[3], e[6], e[1], e[0], e[7], e[8], e[9], e[10], e[11], e[4], e[5])
            if empleadoObj.dni == usuario.dni:
                empleado = empleadoObj
        return empleado
    
