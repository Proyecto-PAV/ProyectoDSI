from Modelo.Estado import *
from BaseDeDatos.CapaConexion import *
from Gestor.Gestor import *
from datetime import datetime
from Modelo.Entrada import *
from Modelo.Sede import *

def prueba1():
    Sede.getEntradaVendidas('Museo Telon', '23:25:00')
if __name__ == "__main__":
    prueba1()
