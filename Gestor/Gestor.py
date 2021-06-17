from BaseDeDatos.CapaConexion import *
from Modelo.Sesion import Sesion
from datetime import datetime
from Modelo.Sede import Sede
from Modelo.Entrada import *
from Modelo.Tarifa import *
from Modelo.Entrada import *


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
    UltimoNumeroEntrada = 0
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
        self.fechaHoraActual = self.getFechaYHoraActual()
        
        tarifasVigentes, montoAdicionalGuia = self.buscarTarifasVigentes()
        return tarifasVigentes, montoAdicionalGuia

    def actualizarPantallas(self):
        pass

    def buscarEstadoConfirmada(self):
        pass
    
    def buscarTarifasVigentes(self):
        tarifasVigentes = Sede.getTarifasVigentes(self.sedeActual, self.fechaHoraActual)
        montoAdicional = Sede.getAdicionalPorGuia(self.sedeActual)

        return tarifasVigentes, montoAdicional


    def calcularDuracionEstimada(self):
        pass

    def calcularMontoTotalAPagar(self, tarifa_seleccionada, cantidad_seleccionada, hayGuia, sedeActual):
        #!Tomando en cuanta que se le pasa un objeto de tarifa
        monto = 0
        montoAdicional = 0
        monto = tarifa_seleccionada.monto * cantidad_seleccionada
        if hayGuia == True:
            montoAdicional = sedeActual.getAdicionalPorGuia()
            monto = monto + montoAdicional
        return monto
        
        
        
    def generarNumeroEntrada(self, ultimo_numero):
        numero_entrada = ultimo_numero + 1

    def imprimirEntradasGeneradas(self):
        pass

    def ObtenerSedeActual(self):
        #preguntar si hay que inicializar con none la fecha de inicio
        sede_actual = Sesion.getEmpleadoenSesion()
        return sede_actual

    def getFechaYHoraActual(self):
        fecha_hora_actual = datetime.now()
        return fecha_hora_actual

    def obtenerUltimoNúmero(self, sedeActual):
        nombre = sedeActual.nombre
        ultimoNumero = getNro(nombre)
        return ultimoNumero

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




