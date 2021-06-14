from BaseDeDatos import CapaConexion

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

    
    def getSedeDondeTrabaja(dni):
        #consultar BD
        sedeDondeTrabaja = CapaConexion.ObtenerSedeEmpleado(dni)
        return sedeDondeTrabaja

