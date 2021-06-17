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
ayer = datetime.now() - timedelta(days=1)
lista = "20:31:42".split(":")
lista2 = "01:00:00".split(":")
hora=int(lista[0])
minuto=int(lista[1])
segundo=int(lista[2])
dh = timedelta(hours=hora) 
dm = timedelta(minutes=minuto)          
ds = timedelta(seconds=segundo) 
hora2=int(lista2[0])
minuto2=int(lista2[1])
segundo2=int(lista2[2])
dh2 = timedelta(hours=hora2) 
dm2 = timedelta(minutes=minuto2)          
ds2 = timedelta(seconds=segundo2) 
resultado1 = ds2 + ds
resultado2 = resultado1 + dm +dm2
hora_fin = resultado2 + dh + dh2
fecha_fin = hora_fin + fecha_hora_actual
if fecha_fin > fecha_hora_actual:
    entradasFechaHora += 1
print(entradasFechaHora)