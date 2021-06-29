from Modelo.Sala import *
from Interfaz.PantallaCantActualSala import *
from Interfaz.PantallaCantidadActualPrinci import *
from Modelo.Sesion import Sesion
from datetime import datetime
from Modelo.Sede import Sede
from Modelo.Tarifa import *
from Modelo.Estado import *
from Interfaz.ImpresorEntrada import *
from Modelo.Entrada import *

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
    sedeActual = ""
    tipoEntrada = None
    tipoVisita = None
    estadoConfirmado_Reserva = []

    def __init__(self, pantallaVentaEntradas, pantallaCantidadActualPrincipal, impresoraEntrada, entradas, sesion, pantallaCantidadActualSala, cantidadEntradas, capacidadMaximaSede, confirmacionVenta, duracionEstimada, empleado, fechaHoraActual,
                 hayGuia, montoTotalAPagar, numeroEntrada, sedeActual, tipoEntrada, tipoVisita, estadoConfirmadoRes):
         #constructor del objeto controlador Gestor
        self.pantallaVentaEntradas = pantallaVentaEntradas
        self.pantallaCantidadActualPrincipal = pantallaCantidadActualPrincipal
        self.impresoraEntrada = impresoraEntrada
        self.pantallaCantidadActualSala = pantallaCantidadActualSala
        self.entradas = entradas
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
        self.pantallaVentaEntradas = pantallaVentaEntradas
        #este metodo desencadena toda la logica
        
        self.sedeActual = self.ObtenerSedeActual()
        self.fechaHoraActual = self.getFechaYHoraActual()
        
        tarifasVigentes, montoAdicionalGuia = self.buscarTarifasVigentes()
        return tarifasVigentes, montoAdicionalGuia

    def ObtenerSedeActual(self):
        #Trae todas las sesiones de la BD y crea los objetos correspondientes a cada sesión
        sesionesBd = obtenerSesionesBd()
        for sesion in sesionesBd:
            sesionObj = Sesion(None, sesion[2], sesion[1], sesion[4], sesion[3], sesion[0])
            if sesionObj.fechaFin == None:
                #se trabaja sobre la sesión cuya fecha de fin sea none ya que esa será la actual
                sesionActiva = sesionObj
        #de dicha sesion se obtiene el empleado
        sede_actual = sesionActiva.getEmpleadoenSesion()
        return sede_actual

    def getFechaYHoraActual(self):
        #obtiene la fecha y hora actual
        fecha_hora_actual = datetime.now()
        return fecha_hora_actual
    
    def buscarTarifasVigentes(self):
        #busca las tarifas vigentes de la sede y el monto adicional de la sede
        sedesBd = obtenerSedes()
        for sede in sedesBd:
            sedeObj = Sede(sede[2], sede[1], None, None, sede[0], None, None, sede[3])
            if sedeObj.nombre == self.sedeActual:
                self.sedeActual = sedeObj
                montoAdicional = sedeObj.getAdicionalPorGuia()
        tarifasVigentes = self.sedeActual.getTarifasVigentes(self.fechaHoraActual)
        return tarifasVigentes, montoAdicional

    def tomarSeleccionTipoVisitaYTipoEntradaYSinGuia(self, tipo_visita, tipo_entrada, guia):
        duracion = self.calcularDuracionEstimada(tipo_visita)
        self.hayGuia = guia
        return duracion

    def calcularDuracionEstimada(self, tipo_visita):
        fecha = self.fechaHoraActual
        if tipo_visita == 'Completa':
            #si el tipo de visita seleccionado es completa, busca la duracion resumida
            duracion = self.sedeActual.getExposicionesCompletasVigentes(fecha)
        elif tipo_visita == 'Por Exposicion':
            #si el tipo de visita seleccionado es por exposicion, busca la duracion extendida
            duracion = self.sedeActual.getPorExposicionVigentes(fecha)

        self.duracionEstimada = duracion
        return duracion

    def tomarSeleccionDeCantidadDeEntradasAEmitir(self, cantidad):
        estadoConfirmado = self.buscarEstadoConfirmada()
        validacion = self.validarCantidadDeEntradasMenorCapaMaxima(cantidad, estadoConfirmado)
        if validacion:
            self.cantidadEntradasEmitir = cantidad
        return validacion

    def buscarEstadoConfirmada(self):
        #Busca en la BD todos los estados de Reserva Visita
        estados_reservaVisita =  CapaConexion.obtenerEstadosReservaVisita()
        #por cada estado obtenido, crea su objeto y si pertenece al ambito reservaVisita lo almacena
        estados_reservaVisita_obj =[]
        for row in estados_reservaVisita:  
            objeto = Estado(row[1], row[2], row[3], row[0]) 
            rdo = objeto.esAmbitoReservaVisita()
            if rdo:
                estados_reservaVisita_obj.append(objeto)

        #busca el estado Confirmado de Reserva Visita
        for estado_reserva in estados_reservaVisita_obj:
            confir = estado_reserva.esConfirmada()
            if confir:
                #retorna el objeto EstadoConfirmado y lo almacena en su atributo del gestor
                self.estadoConfirmado_Reserva = estado_reserva
                return estado_reserva
    
    def validarCantidadDeEntradasMenorCapaMaxima(self, entradasAEmitir, estadoConfirmado):
        #recupera el nombre de la sede actual y el estado confirmado de Rerserva Visita
        duracionEstimada = self.duracionEstimada
        sede_actual = self.sedeActual
        fecha_actual = self.fechaHoraActual
        #! objeto estado confirmado lo puede recuperar el gestor como atributo propio
        #obtiene la cantidad de alumnos dentro del museo con reserva para el momento de la venta
        cantidadAlumnosConReservas = self.sedeActual.getReservaVisita(duracionEstimada, estadoConfirmado, fecha_actual)
        #obtiene la cantidad de personas que compraron una entrada hasta el momento de la venta
        cantidadEntradasVendidas = Sede.getEntradaVendidas(sede_actual, fecha_actual)
        #busca la capacidad maxima de la sede 
        cantidadMaximaVisitantes = self.sedeActual.getCantidadMaximaVisitantes()
        self.capacidadMaximaSede = cantidadMaximaVisitantes
        #Suma la cantidad de gente total que se encuentra en este instante en el museo
        total_visitantes = cantidadAlumnosConReservas + cantidadEntradasVendidas
        cuposDisp = cantidadMaximaVisitantes - total_visitantes
        #valida que la cantidad de entradas a emitir no supere la capacidad maxima de la sede
        if(entradasAEmitir <= cuposDisp):
            return True
        else:
            return False        



    def actualizarPantallas(self):
        #actualiza la pantalla principal a partir de pasado por el parametro
        self.pantallaCantidadActualPrincipal = PantallaCantidadActualPrinci(0, self.capacidadMaximaSede)
        PantallaCantidadActualPrinci.actualizarCantidadActualPrincipal(self.pantallaCantidadActualPrincipal, self.cantidadEntradasEmitir)
        #crea el objeto pantallas salas y actualizar la pantalla sala, verificar el que son muchas
        #buscar todas las salas de la sede
        salas = CapaConexion.obtenerSalas()
        # por cada sala obtenida, creamos el objeto sala cuya sede sea la pasada por parametro
        for s in salas:
            sala = Sala(s[2],s[0],None,s[1])
            resultado = sala.conocerSalasSede(self.sedeActual.nombre)
        #actualizar pantallas de estas salas 
            if resultado:
                self.pantallaCantidadActualSala = PantallaCantActualSala(sala.nombre, 0, self.capacidadMaximaSede)
                PantallaCantActualSala.actualizarCantidadActualSala(self.pantallaCantidadActualSala, self.cantidadEntradasEmitir)

    def calcularMontoTotalAPagar(self, tarifa_seleccionada, cantidad_seleccionada, hayGuia):
        #definimos el monto inicial en base a los datos pasados por parametro
        montoAdicional = 0
        monto = tarifa_seleccionada.monto * cantidad_seleccionada
        if hayGuia == True:
            # si se define una entrada con guia, se le suma al monto total su adicional
            montoAdicional = self.sedeActual.getAdicionalPorGuia()
            monto = monto + montoAdicional
        return monto
        
    def generarNumeroEntrada(self):
        numero_entrada = self.numeroEntrada + 1
        return numero_entrada

    def imprimirEntradasGeneradas(self):
        entras_emitidas = self.entradas
        ImpresorEntrada.imprimirEntradasGeneradas(entras_emitidas)
        

    def obtenerUltimoNumero(self):
        #obtiene las entradas de la BD
        entradas = CapaConexion.obtenerEntradas()
        ultimoNro = 0
        for row in entradas:
            o = Entrada(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            numero = o.getNro()
            if (numero > ultimoNro) and (o.nombre_sede == self.sedeActual.nombre):
                ultimoNro = o.numero
        self.numeroEntrada = ultimoNro

    def solicitarSeleccionTipoEntraTipoVisitayGuia(self):
        pass

    def tomarConfirmacionVenta(self):
        #por cada una de las entradas lo ejecura
        # Guarda en el atributo del gestor el ultimo numero para poder llamar al generar ultimo numero y que ya tenga este
        self.obtenerUltimoNumero()
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
            fechayHora = self.fechaHoraActual.strftime('%Y-%m-%d %H:%M:%S')
            fechayHora = fechayHora.split(" ")
            #valida si la entrada tiene asignado un guia o no, crea su objeto y almacena en el vector
            if self.hayGuia == True:
                nuevaEntrada = Entrada(numeroEntrada, fechayHora[0], fechayHora[1], self.montoTotalAPagar, self.tipoEntrada, self.tipoVisita, nombreSede, empleado)
                nuevaEntrada.new()
                entradas_emitidas.append(ent)
            else:
                ent = Entrada.new(numeroEntrada, fechayHora[0], fechayHora[1], self.montoTotalAPagar, self.tipoEntrada, self.tipoVisita, nombreSede, None)
                entradas_emitidas.append(ent)
            #sumo 1 al contador
            n+=1
        self.entradas = entradas_emitidas
        impresion = self.imprimirEntradasGeneradas()
        self.actualizarPantallas()    





    def finCU(self):
        exit()




