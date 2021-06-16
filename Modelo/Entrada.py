from BaseDeDatos import CapaConexion


class Entrada():

    fechaVenta = ""
    horaVenta = ""
    monto = 0
    numero = 0
    
    def __init__(self, fechaVenta, horaVenta, monto, numero):
        self.fechaVenta = fechaVenta
        self.horaVenta = horaVenta
        self.monto = monto
        self.numero = numero

    def conocerGuiaAsignado(self):
        pass
    def conocerSede(self):
        pass
    def conocerTarifa(self):
        pass
    def getNro(self):
        pass
    def new(self):
        pass

    def esSedeActual(sede_actual):
        entradas = CapaConexion.obtenerEntradasPorSede(sede_actual)
        EntradasDeSede = []
        for row in entradas:
            objeto = Entrada(entradas[1],entradas[2],entradas[3],entradas[4])
            EntradasDeSede.append(objeto)
        return EntradasDeSede

    def getEntradasFechaHoraVenta(entradasObj, duracionEstimada):
        entradasFechaHora = []
        for i in range(0, len(entradasObj)):
            objeto = Entrada(entradasObj[i].fechaVenta, entradasObj[i].fechaHora)
            entradasFechaHora.append(objeto)
        return entradasFechaHora