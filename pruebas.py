from Modelo.Sesion import Sesion
from Modelo.Usuario import Usuario
from BaseDeDatos.CapaConexion import *
from Gestor.Gestor import GestorVentaEntradas
from datetime import datetime
from Modelo.Tarifa import Tarifa
from Modelo.Sede import Sede

gestor = GestorVentaEntradas()
tarifasVigentes, montoAdicionalGuia = gestor.tomarOpciónRegistrarVentaDeEntradas()
print(montoAdicionalGuia)
for tarifa in tarifasVigentes:
    print(tarifa.str())

gestor = GestorVentaEntradas()
sede = gestor.ObtenerSedeActual()
print(sede)

fecha_hora_actual = datetime.now()
sede = Sede(None, None, None, None,'Museo Telon', None, None, None)
tarifas = sede.getTarifasVigentes("Museo Telon", fecha_hora_actual)
for tarifa in tarifas:
    print(tarifa.str())



tarifasVigentes, montoAdicionalGuia = gestor.tomarOpciónRegistrarVentaDeEntradas()
print(tarifasVigentes, montoAdicionalGuia)


monto = sede.getAdicionalPorGuia()
print(monto)


tarifa = Tarifa(None, None, None, 1, 1)
tarifa.getMonto('Museo Telon')

fecha_hora_actual = datetime.now()
tarifas  = ObtenerTarifasEnVigencia("Museo Telon", fecha_hora_actual )
t_vigentes_obj = []
for tarifa in tarifas:
    obj = Tarifa(None, None, None, tarifa[0], tarifa[1])
    t_vigentes_obj.append(obj)
    print(obj.str())




dni = ObtenerDniUsuario("admin")
print(dni)

sede = ObtenerSedeEmpleado(42439269)
print(sede)

usuario = Usuario(None, None, None, None, None, None)
sedeEmpleado = usuario.getUsuario("admin")


sesion = Sesion(None, None, None, None, None, None)
empleado = sesion.getEmpleadoenSesion()
print(empleado)