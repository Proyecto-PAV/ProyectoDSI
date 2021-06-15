from Gestor.Gestor import GestorVentaEntradas

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
        self.habilitarPantalla()

        #aca se crea el objeto gestprVentaEntrada
        self.gestorVentaEntradas = GestorVentaEntradas()

        self.gestorVentaEntradas.tomarOpciónRegistrarVentaDeEntradas(self)
    

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

    def tomarSeleccionCantidadEntradasEmitir(self):
        pass

    def tomarSeleccionGuia(self):
        pass

    def tomarSeleccionTipoEntrada(self):
        pass

    def tomarSeleccionTipoVisita(self):
        pass

    """
    #! poner esta funcion en la pantalla inicio sesion
    def usuario(nUsuario, cUsuario):
        user = nUsuario
        contra = cUsuario
        cursor.execute('SELECT nombre_usuario, contraseña FROM usuarios WHERE nombre_usuario = ? and contraseña = ?', user, contra)
        row = cursor.fetchone()
        if row == None:
            return
        else:
            return True
    """


