from BaseDeDatos.CapaConexion import *
from Modelo.Sesion import Sesion
from datetime import datetime
from Modelo.Sede import *
from Modelo.Entrada import *
from Modelo.Tarifa import *
from Interfaz.PantallaCantActualSala import *
from Interfaz.PantallaCantidadActualPrinci import *
from Modelo.Estado import *
from Interfaz.ImpresorEntrada import *
from Modelo.Sala import *

class GestorVentaEntradas():

    #atributos de la clase de analisis GestorVentaEntradas
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
    UltimoNumeroEntrada = 0
    sedeActual = ""
    tipoEntrada = None
    tipoVisita = None
    estadoConfirmado_Reserva = []

    def __init__(self, pantallaVentaEntradas, pantallaCantidadActualPrincipal, impresoraEntrada, entrada, sesion, pantallaCantidadActualSala, cantidadEntradas, capacidadMaximaSede, confirmacionVenta, duracionEstimada, empleado, fechaHoraActual,
                 hayGuia, montoTotalAPagar, numeroEntrada, sedeActual, tipoEntrada, tipoVisita, estadoConfirmadoRes):
         #constructor del objeto controlador Gestor
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
        self.estadoConfirmado_Reserva = estadoConfirmadoRes
        

    def tomarOpcionRegistrarVentaDeEntradas(self, pantallaVentaEntradas):
        #guarda al objeto pantalla en los atributos del gestor
        self.pantallaVentaEntradas = pantallaVentaEntradas
        #este metodo desencadena toda la logica
        #busca la sede actual y guarda su nombre en el atributo sedeActual        
        self.sedeActual = self.ObtenerSedeActual()
        #obtiene la fecha y hora actual del sistema
        self.fechaHoraActual = self.getFechaYHoraActual()
        #busca las tarifas vigentes para la sede actual y ademas obtiene el monto adicional del guia
        tarifasVigentes, montoAdicionalGuia = self.buscarTarifasVigentes()
        return tarifasVigentes, montoAdicionalGuia

    def actualizarPantallas(self, pantallaSala, pantallaPrincipal):
        #! verificar si este es necesario o simplemente es un actualizar en interfaz
        #actualiza la pantalla principal a partir de pasado por el parametro
        self.pantallaCantidadActualPrincipal = pantallaPrincipal
        PantallaCantidadActualPrinci.actualizarCantidadActualPrincipal(self.pantallaCantidadActualPrincipal, self.cantidadEntradasEmitir)
        #crea el objeto pantallas salas y actualizar la pantalla sala, verificar el que son muchas
        self.pantallaCantidadActualSala= pantallaSala
        #buscar todas las salas de la sede
        #! agregar la dependencia del gestor a la sala
        salas = Sala.conocerSalas(self.sedeActual)
        #actualizar pantallas de estas salas 
        for s in salas:
            PantallaCantActualSala.actualizarCantidadActualSala(self.pantallaCantidadActualSala, self.cantidadEntradasEmitir)
    
            

    def buscarTarifasVigentes(self):
        #obtiene las tarifas vigentes a al fecha de hoy de la sede actual y el monto adicional del guia
        tarifasVigentes, montoAdicional = Sede.getTarifasVigentes(self.sedeActual, self.fechaHoraActual)
                
        return tarifasVigentes, montoAdicional


    def buscarEstadoConfirmada(self):
        #busca todos los estados de ReservaVisita
        estado_reservaVisitaObj = Estado.esAmbitoReservaVisita()
        #busca el estado Confirmado de Reserva Visita
        estado_reservaConfirmadaObj = Estado.esConfirmada(estado_reservaVisitaObj)
        #retorna el vector de objetos EstadoConfirmado y lo almacena en su atributo
        self.estadoConfirmado_Reserva = estado_reservaConfirmadaObj
        return estado_reservaConfirmadaObj
    
    def validarCantidadDeEntradasMenorCapaMaxima(self, duracionEstimada, entradasAEmitir):
        #recupera el nombre de la sede actual y el estado confirmado de Rerserva Visita
        sede_actual = self.sedeActual
        estado_confirmado = self.estadoConfirmado_Reserva
        fecha_actual = self.fechaHoraActual
        #obtiene la cantidad de alumnos dentro del museo con reserva para el momento de la venta
        cantidadAlumnosConReservas = Sede.getReservaVisita(sede_actual, duracionEstimada, estado_confirmado, fecha_actual)
        #obtiene la cantidad de personas que compraron una entrada hasta el momento de la venta
        cantidadEntradasVendidas = Sede.getEntradaVendidas(sede_actual, fecha_actual)
        #busca la capacidad maxima de la sede 
        cantidadMaximaVisitantes = Sede.getCantidadMaximaVisitantes(sede_actual)
        #Suma la cantidad de gente total que se encuentra en este instante en el museo
        total_visitantes = cantidadAlumnosConReservas + cantidadEntradasVendidas
        cuposDisp = cantidadMaximaVisitantes - total_visitantes
        #valida que la cantidad de entradas a emitir no supere la capacidad maxima de la sede
        if(entradasAEmitir <= cuposDisp):
            return True
        else:
            return False
        

    """
    def buscarTarifasVigentes(self, sede_actual, fecha_hora_actual):
        tarifas = Sede.getTarifasVigentes(sede_actual, fecha_hora_actual)

        return tarifasVigentes, montoAdicional
        return tarifas
    """
    def calcularDuracionEstimada(self):
        actual = self.sedeActual
        duracion = Sede.getExposicionesCompletasVigentes(actual)
        self.duracionEstimada=duracion


    def calcularMontoTotalAPagar(self, tarifa_seleccionada, cantidad_seleccionada, hayGuia):
        #!Tomando en cuanta que se le pasa un objeto de tarifa
        #definimos el monto inicial en base a los datos pasados por parametro
        montoAdicional = 0
        monto = tarifa_seleccionada.monto * cantidad_seleccionada
        if hayGuia == True:
            # si se define una entrada con guia, se le suma al monto total su adicional
            montoAdicional = Sede.getAdicionalPorGuia(self.sedeActual)
            monto = monto + montoAdicional
        return monto
        
        
    def generarNumeroEntrada(self):
        numero_entrada = self.numeroEntrada + 1
        return numero_entrada

    def imprimirEntradasGeneradas(entras_emitidas):
        impresor = ImpresorEntrada.imprimirEntradasGeneradas(entras_emitidas)
        

    def ObtenerSedeActual(self):
        #?preguntar si hay que inicializar con none la fecha de inicio
        #Llama al logueado:Usuario para obtener la sede
        sede_actual = Sesion.getEmpleadoenSesion()
        return sede_actual

    def getFechaYHoraActual(self):
        #obtiene la fecha y hora actual
        fecha_hora_actual = datetime.now()
        return fecha_hora_actual

    def obtenerUltimoNumero(self):
        nombre = self.sedeActual
        self.numeroEntrada = Entrada.getNro(nombre)
        numeroEntrada = self.numeroEntrada
        return numeroEntrada

    def solicitarSeleccionTipoEntraTipoVisitayGuia(self):
        pass

    def tomarConfirmacionVenta(self):
        #por cada una de las entradas lo ejecura
        # Guarda en el atributo del gestor el ultimo numero para poder llamar al generar ultimo numero y que ya tenga este
        self.numeroEntrada = self.obtenerUltimoNúmero(self.sedeActual)
        #recupero la cantidad de entradas a emitir e inicializo el contador y el vector de entradas emitidas
        entradas_emitidas = []
        n=0
        cantidad = self.cantidadEntradasEmitir
        while n < cantidad:
            # Guarda en la variable numero entrada el numero que se le va a poner la entrada
            numeroEntrada = self.generarNumeroEntrada()
            # Guarda en el atributo del gestor el ultimo numero de entrada generado y recupero los datos del gestor
            self.numeroEntrada = numeroEntrada
            nombreSede = self.sedeActual
            empleado = self.empleado
            FechayHora = self.fechaHoraActual.strftime('%Y-%m-%d %H:%M:%S')
            FechayHora = FechayHora.split(" ")
            #valida si la entrada tiene asignado un guia o no, crea su objeto y almacena en el vector
            if self.hayGuia == True:
                ent = Entrada.new(numeroEntrada, FechayHora[0], FechayHora[1], self.montoTotalAPagar, self.tipoEntrada, self.tipoVisita, nombreSede, empleado.dni)
                entradas_emitidas.append(ent)
            else:
                ent = Entrada.new(numeroEntrada, FechayHora[0], FechayHora[1], self.montoTotalAPagar, self.tipoEntrada, self.tipoVisita, nombreSede, None)
                entradas_emitidas.append(ent)
            #sumo 1 al contador
            n+=1
        
        #retornamos las entradas emitidas
        return entradas_emitidas
        

    def tomarSeleccionDeCantidadDeEntradasAEmitir(self):
        #? Que atributo se pone en el igual
        estadosConfirmados = self.buscarEstadoConfirmada(self)
        self.validarCantidadDeEntradasMenorCapaMaxima(self, estadosConfirmados, estadosConfirmados)

    def tomarSeleccionTipoVisitaYTipoEntradaYGuia(self):
        pass

    

    def finCU(self):
        pass




