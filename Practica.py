from Gestor.Gestor import *

gestor1 = GestorVentaEntradas(None, None,None,None,None,None,25,700,None,None,None,None,None,None,None,None,None,None)

gestor1.sedeActual = gestor1.ObtenerSedeActual()

ultimonumero = gestor1.obtenerUltimoNúmero(gestor1.sedeActual)

nuevo = gestor1.generarNumeroEntrada()

gestor1.fechaHoraActual=gestor1.getFechaYHoraActual()

montoAdicional = 0

tarifas, montoAdicional = gestor1.buscarTarifasVigentes()

cantidad = 10

hayguia = True

total = gestor1.calcularMontoTotalAPagar(tarifas[0], cantidad, hayguia, gestor1.sedeActual)

print(total)
