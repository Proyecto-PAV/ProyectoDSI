from BaseDeDatos import CapaConexion

class Sala():
    
     #atributos de la clase Sala
    nombre = ""
    numero  = 0
    superficie = 0
    nombreSede = ''

    def __init__(self, nombre, numero, superficie, nombre_sede):
        #constructor del objeto Sala
        self.nombre = nombre
        self.numero = numero
        self.superficie = superficie
        self.nombreSede = nombre_sede


    def conocerSalasSede(self, nombre):
        #devuelve true o false segun el nombre de la sede que se pasa por parametro
        if self.nombreSede == nombre: 
            return True
        else:
            return False

        
