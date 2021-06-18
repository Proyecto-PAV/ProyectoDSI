from Modelo.Estado import *
from BaseDeDatos.CapaConexion import *
from Gestor.Gestor import *
from datetime import datetime
from Modelo.Entrada import *
from Modelo.Sede import *
import datetime
from Modelo.Reserva_Visita import *

def prueba1():
    c = Sede.getReservaVisita('Museo Telon','00:30:00')
    print(c)

if __name__ == "__main__":
    prueba1()
