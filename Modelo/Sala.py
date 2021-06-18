from BaseDeDatos import CapaConexion

class Sala():
    
    sala = ""
    numero  = 0
    superficie = 0
    nombreSede = ''

    def __init__(self, nombre, numero, superficie, nombre_sede):
        self.nombre = nombre
        self.numero = numero
        self.superficie = superficie
        self.nombreSede = nombre_sede


    def conocerSalas(nombre_sede):
        # buscamos las salas de BD y creamos el vector vacio
        salas = CapaConexion.obtenerSalas()
        salas_obj=[]
        # por cada sala obtenida, creamos el objeto sala cuya sede sea la pasada por parametro
        for s in salas:
            sala = Sala(s[2],s[0],None,s[1])
            if sala.nombreSede==nombre_sede:
                salas_obj.append(sala)
        
        return salas_obj

        
