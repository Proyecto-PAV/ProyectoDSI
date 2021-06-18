from BaseDeDatos.CapaConexion import *
from Modelo.Sesion import Sesion
from datetime import datetime
from Modelo.Sede import *
from Modelo.Estado import *

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

    def tomarOpcionRegistrarVentaDeEntradas(self, pantallaVentaEntradas):
        self.pantallaVentaEntradas = pantallaVentaEntradas
        #este metodo desencadena toda la logica        
        self.sedeActual = self.ObtenerSedeActual()



    def actualizarPantallas(self):
        pass

    def buscarEstadoConfirmada():
        estado_reservaVisitaObj = []
        estado_reservaVisitaObj = Estado.esAmbitoReservaaVisita()
        estado_reservaConfirmadaObj = []
        estado_reservaConfirmadaObj = Estado.esConfirmada(estado_reservaVisitaObj)
        return estado_reservaConfirmadaObj
    
    def validarCantidadDeEntradasMenorCapaMaxima(duracionEstimada, estadosConfirmados, entradasAEmitir):
        sede_actual = GestorVentaEntradas.sedeActual
        cantidadReservas = Sede.getReservaVisita(sede_actual, duracionEstimada)
        cantidadEntradasVendidas = Sede.getEntradaVendidas(sede_actual, duracionEstimada, estadosConfirmados)
        cantidadMaximaVisitantes = Sede.getCantidadMaximaVisitantes(sede_actual)
        sum = cantidadReservas + cantidadEntradasVendidas
        cuposDisp = cantidadMaximaVisitantes - sum
        if(entradasAEmitir <= cuposDisp):
            print("se puden comprar")
            return True
        else:
            print("No hay cupo disponible")
            return False
        #?Finaliza aca?
        #return

    """
    def buscarTarifasVigentes(self, sede_actual, fecha_hora_actual):
        tarifas = Sede.getTarifasVigentes(sede_actual, fecha_hora_actual)

        return tarifas
    """
    def calcularDuracionEstimada(self):
        pass

    def calcularMontoTotalAPagar(self):
        pass

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
        #? Que atributo se pone en el igual
        estadosConfirmados = self.buscarEstadoConfirmada(self)
        self.validarCantidadDeEntradasMenorCapaMaxima(self, estadosConfirmados, estadosConfirmados)

    def tomarSeleccionTipoVisitaYTipoEntradaYGuia(self):
        pass

    

    def finCU(self):
        pass




