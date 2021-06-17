from datetime import datetime, timedelta
from datetime import date
from Modelo.Entrada import *

now = datetime.now()
print("La hora actual es {}".format(now.hour))
print("El minuto actual es {}".format(now.minute))
print("El segundo actual es {}".format(now.second))



def getEntradasFechaHoraVenta(self, entradasObj, duracionEstimada):
        entradasFechaHora = 0
        fecha_hora_actual = datetime.now()
        for i in range(0, len(entradasObj)):
            formato = "%H:%M:%S"
            lista = duracionEstimada.split(":")
            hora=int(lista[0])
            minuto=int(lista[1])
            segundo=int(lista[2])
            h1 = datetime.strptime(self.horaVenta, formato)
            dh = timedelta(hours=hora) 
            dm = timedelta(minutes=minuto)          
            ds = timedelta(seconds=segundo) 
            resultado1 =h1 + ds
            resultado2 = resultado1 + dm
            hora_fin = resultado2 + dh
            hora_fin = hora_fin.strftime(formato)
        return entradasFechaHora



entradasFechaHora = 0
fecha_hora_actual = datetime.now()
lista = "20:31:42".split(":")
hora=int(lista[0])
minuto=int(lista[1])
segundo=int(lista[2])
dh = timedelta(hours=hora) 
dm = timedelta(minutes=minuto)          
ds = timedelta(seconds=segundo) 
resultado1 = datetime.now() + ds
resultado2 = resultado1 + dm
hora_fin = resultado2 + dh
if hora_fin > fecha_hora_actual:
    entradasFechaHora += 1
print(entradasFechaHora)