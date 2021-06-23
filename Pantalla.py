from Gestor.Gestor import *

class PantallaVentaEntradas:

    def __init__(self, botonConfirmacionVenta, botonRegistrarVenta, comboSeleccionNroEntradas, labelTipoEntrada, labelTipoVisita, listadodetalleVenta, 
    listadoMontoTarifas, listadoTarifas, ventanaHabilitada, gestorVentaEntradas):
        self.gestorVentaEntradas = gestorVentaEntradas
        self.botonConfirmacionVenta = botonConfirmacionVenta
        self.botonRegistrarVenta = botonRegistrarVenta
        self.comboSeleccionNroEntradas = comboSeleccionNroEntradas
        self.labelTipoEntrada = labelTipoEntrada
        self.labelTipoVisita = labelTipoVisita
        self.listadodetalleVenta = listadodetalleVenta
        self.listadoMontoTarifas = listadoMontoTarifas
        self.listadoTarifas = listadoTarifas
        self.ventanaHabilitada = ventanaHabilitada

    def tomarOpcionRegistrarVentaEntradas(self):
        #self.habilitarPantalla()
        #aca se crea el objeto gestprVentaEntrada
        self.gestorVentaEntradas = GestorVentaEntradas(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        tarifasVigentes, montoAdicionalGuia = self.gestorVentaEntradas.tomarOpcionRegistrarVentaDeEntradas(self)
        return tarifasVigentes, montoAdicionalGuia
    

    def habilitarPantalla(self):
        pass

    def mostrarDetalleVenta(self):
        pass

    def mostrarListadoMontoTarifas(self):
        pass

    def solicitarConfirmacionVenta(self):
        pass

    def solicitarSeleccionCantidadEntradasEmitir(self):
        pass

    def tomarConfirmacionVenta(self):
        pass

    def tomarSeleccionDeCantidadEntradasEmitir(self, cantidad):
        validacion = self.gestorVentaEntradas.tomarSeleccionDeCantidadDeEntradasAEmitir(cantidad)
        return validacion

    def tomarDatosEntrada(self, tipo_visita, tipo_entrada, guia):
        duracion = self.gestorVentaEntradas.tomarSeleccionTipoVisitaYTipoEntradaYSinGuia(tipo_visita, tipo_entrada, guia)


