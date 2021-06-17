from Modelo.Reserva_Visita import ReservaVisita
import pyodbc 

''' funcion de conexion generica con la BD '''
def conexion():
        
    server = 'tpai-server.database.windows.net'
    database = 'MUSEO'
    username = 'gzr'
    password = 'tpaimanero1.'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                        server+';DATABASE='+database+';UID='+username+';PWD=' + password)
    
    return cnxn




def ObtenerTodasLasSedes():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute('select * from sedes')
    for row in cursor:
        print(row)


def ObtenerSesionActiva():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute('select nombre_usuario from sesiones where fecha_fin IS NULL')
    sesion = cursor.fetchone()
    return sesion[0]


def ObtenerDniUsuario(nombre):
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("select dni_empleado from usuarios where nombre_usuario=?", nombre  )
    dni = cursor.fetchone()
    return dni[0]


def ObtenerSedeEmpleado(dni):
    cnxn = conexion()
    cursor = cnxn.cursor()
    
    cursor.execute("select nombre_sede from empleados where dni=?",dni )
    sedes = cursor.fetchone()
    return sedes[0]
   
"""
def ObtenerSedeEmpleado():
    cnxn = conexion()
    cursor = cnxn.cursor()
    sede = cursor.execute("select nombre_sede from empleados where dni=42439269" )
    return sede
"""
def ObtenerTarifasEnVigencia(nombre_sede, fecha):
    #corroborar la matriz
    cnxn = conexion()
    cursor = cnxn.cursor()
    tarifas = cursor.execute("select id_tipo_entrada, id_tipo_visita from tarifas  \
                where nombre_sede = '" + nombre_sede + "' AND YEAR('"+fecha+"') \
                BETWEEN YEAR('fecha_inicio_vigencia') and YEAR('fecha_fin_vigencia')")
    return tarifas


def ObtenerNombreEntrada(nro):
    cnxn = conexion()
    cursor = cnxn.cursor()
    nombre= cursor.execute("select nombre from tipoEntradas where id_tipo_entrada ='" +nro+ "'")
    return nombre

def ObtenerNombreVisita(nro):
    cnxn = conexion()
    cursor = cnxn.cursor()
    nombre= cursor.execute("select nombre from tipoVisitas where id_tipo_visita =' " + nro + " ' ")
    return nombre


def ObtenerMonto(te, tv):
    cnxn = conexion()
    cursor = cnxn.cursor()
    monto = cursor.execute("select monto from tarifas \
            where id_tipo_entrada = ' " + te + " ' \
                 and id_tipo_visita = ' " + tv + " ' ")
    return monto


def ObtenerMontoGuiaSede(nombre):
    cnxn = conexion()
    cursor = cnxn.cursor()
    monto = cursor.execute("select adicional_por_guia from sedes where nombre='" +nombre+ "'")
    return monto

def ObtenerCantidadDeAlumnosConfirmados(fechaHora):
    cnxn = conexion()
    cursor = cnxn.cursor()
    cantidad = cursor.execute("select SUM(cantidad_alumnos_confirmada) from reservasVisitas where fecha_hora_reserva ='" + fechaHora + "'")
    return cantidad

def ObtenerCantidadAlumnosConfirmado():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cantidad = cursor.execute("select SUM(cantidad_alumnos_confirmada) from reservasVisitas where fecha_hora_reserva ='" +  + "'")
    return cantidad

def obtenerEstadosReservaVisita():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("select * from estados where  nombre_ambito = 'ReservaVisita' ")
    estados = cursor.fetchall()
    return estados

def obtenerEntradasPorSede():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("select numero, fecha_venta, hora_venta,monto, nombre_sede from entradas")
    entradas = cursor.fetchall()
    return entradas


if __name__ == '__main__':
        ObtenerTodasLasSedes()
        