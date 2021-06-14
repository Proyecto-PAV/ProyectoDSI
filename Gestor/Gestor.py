from BaseDeDatos.CapaConexion import ObtenerSedeEmpleado
from Modelo.Sesion import *
from datetime import datetime
from Modelo.Sede import *

def ObtenerSedeActual():
    sede_actual = Sesion.getEmpleadoenSesion()

    return sede_actual


def getFechaYHoraActual():
    fecha_hora_actual = datetime.now()
    return fecha_hora_actual

def buscarTarifasExistentes(sede_actual, fecha_hora_actual):
    tarifas = Sede.getTarifasVigentes(sede_actual, fecha_hora_actual)
    
    return tarifas





if __name__=='__main__':
    nombre_sede = ObtenerSedeActual()
    fechaHoraActual = getFechaYHoraActual()
    tarifas, adicional_guia = buscarTarifasExistentes(nombre_sede, fechaHoraActual)