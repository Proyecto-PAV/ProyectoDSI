from BaseDeDatos.CapaConexion import *
from Modelo.Sesion import Sesion
from datetime import datetime
from Modelo.Sede import *
from Modelo.Sala import *
from Interfaz.PantallaCantActualSala import *
from Interfaz.PantallaCantidadActualPrinci import *

class GestorVentaEntradas():

    pantallaVentaEntradas = None
    pantallaCantidadActualPrincipal = None
    impresoraEntrada = None
    pantallaCantidadActualSala = None
    entrada = None
    sesion = None
    cantidadEntradasEmitir= 0
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

    def __init__(self, pantallaVentaEntradas, pantallaCantidadActualPrincipal, impresoraEntrada, entrada, sesion, pantallaCantidadActualSala, cantidadEntradas, capacidadMaximaSede, confirmacionVenta, duracionEstimada, empleado, fechaHoraActual,
                 hayGuia, montoTotalAPagar, numeroEntrada, sedeActual, tipoEntrada, tipoVisita):
        self.pantallaVentaEntradas = pantallaVentaEntradas
        self.pantallaCantidadActualPrincipal = pantallaCantidadActualPrincipal
        self.impresoraEntrada = impresoraEntrada
        self.pantallaCantidadActualSala = pantallaCantidadActualSala
        self.entrada = entrada
        self.sesion = sesion
        self.cantidadEntradasEmitir = cantidadEntradas
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



    def actualizarPantallas(self, pantallaSala, pantallaPrincipal):
        #* atibutos del gestor necesarios: CantidadEntradas, nombre de salas y capacidad Maxima
     
        #crear objeto pantalla y actualizar la pantalla principal
        self.pantallaCantidadActualPrincipal = pantallaPrincipal
        PantallaCantidadActualPrinci.actualizarCantidadActualPrincipal(self.pantallaCantidadActualPrincipal, self.cantidadEntradasEmitir)
        #crear objeto pantallas salas y actualizar la pantalla sala, verificar el que son muchas
        self.pantallaCantidadActualSala= pantallaSala
        #buscar todas las salas de la sede
        salas = Sala.conocerSalas(self.sedeActual)
        #actualizar pantallas de estas salas primero creando el objeto
        for s in salas:
            sl = Sala(s.nombre, s.numero, s.superficie, s.nombreSede)
            if sl.nombre == self.pantallaCantidadActualSala.nombreSala:
               PantallaCantActualSala.actualizarCantidadActualSala(self.pantallaCantidadActualSala, self.cantidadEntradasEmitir)
            

       
        

    def buscarEstadoConfirmada(self):
        pass
    """
    def buscarTarifasVigentes(self, sede_actual, fecha_hora_actual):
        tarifas = Sede.getTarifasVigentes(sede_actual, fecha_hora_actual)

        return tarifas
    """
    def calcularDuracionEstimada(self):
        actual = self.sedeActual
        duracion = Sede.getExposicionesCompletasVigentes(actual)
        self.duracionEstimada=duracion


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
        pass

    def tomarSeleccionTipoVisitaYTipoEntradaYGuia(self):
        pass

    def validarCantidadDeEntradasMenorCapaMáxima(self):
        pass

    def finCU(self):
        pass




