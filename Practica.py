from Modelo.Tarifa import *
from Modelo.Sede import *

tarifa_seleccionada = Tarifa('2021-12-31', '2021-01-01', 250, 1, 1)
sedeActual = Sede(None, None, None, None, 'Museo Telon', None, None)
cantidad_seleccionada = 10
hayGuia = True
print(tarifa_seleccionada.str())

def calcularMontoTotalAPagar(tarifa_seleccionada, cantidad_seleccionada, hayGuia, sedeActual):
    #!Tomando en cuanta que se le pasa un objeto de tarifa
    monto = 0
    montoAdicional = 0
    monto = tarifa_seleccionada.monto * cantidad_seleccionada
    if hayGuia == True:
        montoAdicional = sedeActual.getAdicionalPorGuia()
        monto = monto + montoAdicional
    return monto

monto = calcularMontoTotalAPagar(tarifa_seleccionada, cantidad_seleccionada, hayGuia, sedeActual)
print (monto)