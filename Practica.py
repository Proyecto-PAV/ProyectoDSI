from Gestor.Gestor import *

gestor1 = GestorVentaEntradas(None, None,None,None,None,None,25,700,None,None,None,None,None,None,None,None,None,None)

gestor1.sedeActual = gestor1.ObtenerSedeActual()

ultimonumero = gestor1.obtenerUltimoNúmero(gestor1.sedeActual)

nuevo = gestor1.generarNumeroEntrada()

gestor1.fechaHoraActual=gestor1.getFechaYHoraActual()

print(nuevo)
