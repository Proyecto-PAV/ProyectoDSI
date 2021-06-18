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

    def __init__(self, pantallaVentaEntradas, pantallaCantidadActualPrincipal, impresoraEntrada, entrada, sesion, pantallaCantidadActualSala, cantidadEventos, capacidadMaximaSede, confirmacionVenta, duracionEstimada, empleado, fechaHoraActual,
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
        
        
    def generarNumeroEntrada(self):
        numero_entrada = self.numeroEntrada + 1
        return numero_entrada

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
        nombre = sedeActual
        self.numeroEntrada = Entrada.getNro(nombre)
        numeroEntrada = self.numeroEntrada
        return numeroEntrada

    def solicitarSeleccionTipoEntraTipoVisitayGuia(self):
        pass

    def tomarConfirmacionVenta(self):
        # Guarda en el atributo del gestor el ultimo numero para poder llamar al generar ultimo numero y que ya tenga este
        self.numeroEntrada = self.obtenerUltimoNúmero(self.sedeActual)
        # Guarda en la variable numero entrada el numero que se le va a poner la entrada
        numeroEntrada = self.generarNumeroEntrada()
        # Guarda en el atributo del gestor el ultimo numero de entrada generado
        self.numeroEntrada = numeroEntrada
        nombreSede = self.sedeActual
        empleado = self.empleado
        FechayHora = self.fechaHoraActual.strftime('%Y-%m-%d %H:%M:%S')
        FechayHora = FechayHora.split(" ")

        if self.hayGuia == True:
            Entrada.new(numeroEntrada, FechayHora[0], FechayHora[1], self.montoTotalAPagar, self.tipoEntrada, self.tipoVisita, nombreSede, empleado.nombre, empleado.dni)
        else:
            Entrada.new(numeroEntrada, FechayHora[0], FechayHora[1], self.montoTotalAPagar, self.tipoEntrada, self.tipoVisita, nombreSede, empleado.nombre)
        #? El metodo new de Entrada devuelve el objeto nuevo pero donde hay que guardarlo?
        

    def tomarSeleccionDeCantidadDeEntradasAEmitir(self):
        pass

    def tomarSeleccionTipoVisitaYTipoEntradaYGuia(self):
        pass

    def validarCantidadDeEntradasMenorCapaMáxima(self):
        pass

    def finCU(self):
        pass




