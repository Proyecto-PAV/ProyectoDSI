from BaseDeDatos.CapaConexion import *
class Entrada():
    
    numero = 0
    fechaVenta = ""
    horaVenta = ""
    monto = 0
    id_tipo_entrada = 0
    id_tipo_visita = 0
    nombre_sede = ""
    dni_guia = 0

    def __init__(self, numero, fechaVenta, horaVenta, monto, id_tipo_entrada, id_tipo_visita, nombre_sede, dni_guia):
        self.numero = numero
        self.fechaVenta = fechaVenta
        self.horaVenta = horaVenta
        self.monto = monto
        self.id_tipo_entrada = id_tipo_entrada
        self.id_tipo_visita = id_tipo_visita
        self.nombre_sede = nombre_sede
        self.dni_guia = dni_guia
    
    def conocerGuiaAsignado(self):
        pass
    def conocerSede(self):
        pass
    def conocerTarifa(self):
        pass
    def getNro(nombreSede):
        ultimoNro = 0
        entradas = obtenerEntradas()
        for row in entradas:
            o = Entrada(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            if (o.numero > ultimoNro) and (o.nombre_sede == nombreSede):
                ultimoNro = o.numero
        return ultimoNro
    def new(numero, fechaVenta, horaVenta, monto, id_tipo_entrada, id_tipo_visita, nombre_sede, dni_guia):
        nuevaEntrada = Entrada(numero, fechaVenta, horaVenta, monto, id_tipo_entrada, id_tipo_visita, nombre_sede, dni_guia)
        return nuevaEntrada
