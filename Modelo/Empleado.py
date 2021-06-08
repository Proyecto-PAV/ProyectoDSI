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
    cargos = []
    horaIngreso = ""
    horaSalida = ""


    def __init__(self, nombre, apellido, codValidacion, cuit, dni, domicilio, fechaDeIngreso, fechaNacimiento, mail, sedeDondeTrabaja, sexo, telefono, cargos,horaIngreso, horaSalida):
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
        self.cargos = cargos
        self.horaIngreso = horaIngreso
        self.horaSalida = horaSalida

    def conocerCargo(self):
        return self.cargos
    def conocerHorario(self):
        return self.horaIngreso,self.horaSalida
    def getSedeDondeTrabaja(self):
        return self.sedeDondeTrabaja

