
class usuario():

    caducidad = ''
    contraseña = ''
    nombre = ''
    usuarioLogueado = 0

    def __init__(self, caducidad, contraseña, nombre, usuarioLogueado):
        self.caducidad = caducidad
        self.contraseña = contraseña
        self.nombre = nombre
        self.usuarioLogueado = usuarioLogueado
    
    def conocerEmpleado(self):
        pass

    def getEmpleadoenSesion(self):
        pass
