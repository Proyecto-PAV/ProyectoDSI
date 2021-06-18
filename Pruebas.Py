from Modelo.Estado import *
from BaseDeDatos.CapaConexion import *
from Gestor.Gestor import *
from datetime import datetime
from Modelo.Entrada import *
from Modelo.Sede import *
import datetime
from Modelo.Reserva_Visita import *

def prueba1():
    estado_reservaConfirmadaObj = GestorVentaEntradas.buscarEstadoConfirmada()
    for i in range(0, len(estado_reservaConfirmadaObj)):  
        print(estado_reservaConfirmadaObj[i].ambito)
    return estado_reservaConfirmadaObj
    
def prueba2(estadosConfirmados):
    GestorVentaEntradas.validarCantidadDeEntradasMenorCapaMaxima('00:30:00', estadosConfirmados, 5)
if __name__ == "__main__":
    estado_reservaConfirmadaObj = prueba1()
    prueba2(estado_reservaConfirmadaObj)