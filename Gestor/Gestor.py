from BaseDeDatos.CapaConexion import *
from Modelo.Sesion import Sesion
from datetime import datetime
from Modelo.Sede import *


class GestorVentaEntradas():

    pantallaVentaEntradas = None
    pantallaCantidadActualPrincipal = None
    impresoraEntrada = None
    pantallaCantidadActualSala = None
    entrada = None
    sesion = None
    cantidadEventos = 0
    capacidadMaximaSede = 0
    confirmacionVenta = True
    duracionEstimada = 0
    empleado = ''
    fechaHoraActual = ''
    hayGuia = True
    montoTotalAPagar = 0
    numeroEntrada = 0
    sedeActual = ""
    tipoEntrada = None
    tipoVisita = None

    def _init_(self, pantallaVentaEntradas, pantallaCantidadActualPrincipal, impresoraEntrada, entrada, sesion, pantallaCantidadActualSala, cantidadEventos, capacidadMaximaSede, confirmacionVenta, duracionEstimada, empleado, fechaHoraActual,
                 hayGuia, montoTotalAPagar, numeroEntrada, sedeActual, tipoEntrada, tipoVisita):
        self.pantallaVentaEntradas = pantallaVentaEntradas
        self.pantallaCantidadActualPrincipal = pantallaCantidadActualPrincipal
        self.impresoraEntrada = impresoraEntrada
        self.pantallaCantidadActualSala = pantallaCantidadActualSala
        self.entrada = entrada
        self.sesion = sesion
        self.cantidadEventos = cantidadEventos
        self.capacidadMaximaSede = capacidadMaximaSede
        self.confirmacionVenta = confirmacionVenta
        self.duracionEstimada = duracionEstimada
        self.empleado = empleado
        self.fechaHoraActual = fechaHoraActual
        self.hayGuia = hayGuia
        self.montoTotalAPagar = montoTotalAPagar
        self.numeroEntrada = numeroEntrada
        self.sedeActual = sedeActual
        self.tipoEntrada = tipoEntrada
        self.tipoVisita = tipoVisita

    def tomarOpciónRegistrarVentaDeEntradas(self, pantallaVentaEntradas):
        self.pantallaVentaEntradas = pantallaVentaEntradas
        #este metodo desencadena toda la logica
        
        self.sedeActual = self.ObtenerSedeActual()



    def actualizarPantallas(self):
        pass

    def buscarEstadoConfirmada(self):
        pass
    def buscarTarifasVigentes(self, sede_actual, fecha_hora_actual):
        tarifas = Sede.getTarifasVigentes(sede_actual, fecha_hora_actual)

        return tarifas
    def calcularDuracionEstimada(self):
        pass

    def calcularMontoTotalAPagar(self, tipoEntrada, tipoVisita, cantidad_entradas):
        #?Se le pasa la cantidad de entradas seleccionada por el usuario y la entrada con el tipo de entrada y el tipo de visita de cada entrada
        #?Suponemos que en el paso 3 y 6 se guardan en variables estos parametros
        #?Tambien suponemos que entradas es un vector con el convinatorio de todas las entradas posibles que arroje (select id_tipo_entrada, id_tipo_visita from tarifas where nombre_sede like 'Museo Telon')
        total = 0
        '''monto_por_entrada = 0
        #*Ejemplo cuando se piden 11 entradas de menores y 10 de jubilados
        #entradas = [e1, e2, e3, e4, e5, e6, e7, e8, e19, e0]
        #cantidad_entradas = [0, 11, 10, 0, 0, 0, 0, 0, 0, 0]
        for row in cantidad_entradas:
            if row != 0:
                monto_por_entrada = CapaConexion.ObtenerMonto(entradas[row][0], entradas[row][1])
                total = total + monto_por_entrada
                
        #al final es con un tipo de entrada y tipo de visita fijo
        return total'''
        
        
        
        
        

    def generarNúmeroEntrada(self):
        pass

    def imprimirEntradasGeneradas(self):
        pass

    def ObtenerSedeActual(self):
        #preguntar si hay que inicializar con none la fecha de inicio
        self.sesion = Sesion(None, None, None, None, None, None)
        sede_actual = self.sesion.getEmpleadoenSesion()

        return sede_actual

    def getFechaYHoraActual(self):
        fecha_hora_actual = datetime.now()
        return fecha_hora_actual

    def obtenerUltimoNúmero(self):
        pass

    def solicitarSeleccionTipoEntraTipoVisitayGuia(self):
        pass

    def tomarConfirmacionVenta(self):
        pass


    def tomarSeleccionDeCantidadDeEntradasAEmitir(self):
        pass

    def tomarSeleccionTipoVisitaYTipoEntradaYGuia(self):
        pass

    def validarCantidadDeEntradasMenorCapaMáxima(self):
        pass

    def finCU(self):
        pass




