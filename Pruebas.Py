from Modelo.Estado import *
from BaseDeDatos.CapaConexion import *
from Gestor.Gestor import *
from datetime import datetime

fecha_hora_actual = datetime.now()
print(fecha_hora_actual)

def prueba1():
    GestorVentaEntradas.tomarSeleccionDeCantidadDeEntradasAEmitir(GestorVentaEntradas)
if __name__ == "__main__":
    
    prueba1()

print("La hora actual es {}".format(now.hour))
print("El minuto actual es {}".format(now.minute))
print("El segundo actual es {}".format(now.second))