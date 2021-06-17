from BaseDeDatos.CapaConexion import *
#from Modelo.Entrada import *

class Entrada():
    
    def __init__(self, numero, fechaVenta, horaVenta, monto, id_tipo_entrada, id_tipo_visita, nombre_sede, dni_guia):
        self.numero = numero
        self.fechaVenta = fechaVenta
        self.horaVenta = horaVenta
        self.monto = monto
        self.id_tipo_entrada = id_tipo_entrada
        self.id_tipo_visita = id_tipo_visita
        self.nombre_sede = nombre_sede
        self.dni_guia = dni_guia
        
        
nombre_sede = 'Museo Telon'

#!     TARIFA
def getNro(nombreSede):
        ultimoNro = 0
        entradas = ObtenerUltimoNumero()
        for row in entradas:
            o = Entrada(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            if (o.numero > ultimoNro) and (o.nombre_sede == nombreSede):
                ultimoNro = o.numero
        return ultimoNro
ultimo = getNro(nombre_sede)










#! CAPA CONEXION
def ObtenerUltimoNumero():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("select * from Entradas")
    entradas = cursor.fetchall()
    return entradas





#!    GESTOR

def obtenerUltimoNúmero(self, sedeActual):
        nombre = sedeActual.nombre
        ultimoNumero = Entrada.getNro(nombre)
        return ultimoNumero
    
def generarNumeroEntrada(ultimo_numero):
        numero_entrada = ultimo_numero + 1
        
        
def calcularMontoTotalAPagar(self, tarifa_seleccionada, cantidad_seleccionada, hayGuia, sedeActual):
        #!Tomando en cuanta que se le pasa un objeto de tarifa
        monto = 0
        montoAdicional = 0
        monto = tarifa_seleccionada.monto * cantidad_seleccionada
        if hayGuia == True:
            montoAdicional = sedeActual.getAdicionalPorGuia()
            monto = monto + montoAdicional
        return monto
    
print(ultimo)