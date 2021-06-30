from Modelo.Reserva_Visita import ReservaVisita
import pyodbc 
from datetime import datetime

''' funcion de conexion generica con la BD '''
def conexion():
        
    server = 'tpai-server.database.windows.net'
    database = 'MUSEO'
    username = 'gzr'
    password = 'tpaimanero1.'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                        server+';DATABASE='+database+';UID='+username+';PWD=' + password)
    
    return cnxn

def obtenerTodasLasSedes():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute('select * from sedes')
    for row in cursor:
        print(row)

def obtenerSesionesBd():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM sesiones')
    sesiones = cursor.fetchall()
    return sesiones

def obtenerUsuariosBd():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    return usuarios

def obtenerEmpleados():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()
    return empleados

def obtenerTarifas():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM tarifas")
    tarifas = cursor.fetchall()
    return tarifas

def obtenerTiposEntradas():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM tipoEntradas")
    tiposEntradas = cursor.fetchall()
    return tiposEntradas

def obtenerSedeEmpleado(dni):
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("select nombre_sede from empleados where dni=?",dni )
    sedes = cursor.fetchone()
    return sedes[0]
   
def obtenerExposiciones():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM exposiciones") 
    exposiciones = cursor.fetchall()
    return exposiciones

def obtenerNombreVisita():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM tipoVisitas")
    tiposVisitas = cursor.fetchall()
    return tiposVisitas

def obtenerMonto(te, tv):
    cnxn = conexion()
    cursor = cnxn.cursor()
    monto = cursor.execute("select monto from tarifas \
            where id_tipo_entrada = ' " + te + " ' \
                 and id_tipo_visita = ' " + tv + " ' ")
    return monto

def obtenerDetalleExposiciones():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute ("select * from detalleExposiciones")
    detalles = cursor.fetchall()
    return detalles

def obtenerEstadosReservaVisita():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("select * from estados")
    estados = cursor.fetchall()
    return estados

def getObras():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute ("select * from obras")
    obra = cursor.fetchall()
    return obra

def obtenerSedes():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM sedes")
    sedes = cursor.fetchall()
    return sedes

def obtenerSalas():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute ("select * from salas")
    salas = cursor.fetchall()
    return salas

def obtenerEntradas():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("select * from entradas")
    entradas = cursor.fetchall()
    return entradas

def obtenerReservas():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("select * from reservasVisitas")
    reservas = cursor.fetchall()
    return reservas

def obtenerCambiosEstados():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("select * from cambiosEstados")
    cambiosEstados = cursor.fetchall()
    return cambiosEstados

def obtenerEstados():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("select * from estados")
    estados = cursor.fetchall()
    return estados

def almacenarEntrada(entrada):
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO entradas VALUES (?,?,?,?,?,?,?,?)", entrada.numero, entrada.fechaVenta, entrada.horaVenta, entrada.monto, entrada.id_tipo_entrada, entrada.id_tipo_visita, entrada.nombre_sede, entrada.dni_guia)
    cursor.commit()

def insertarEntrada(tipo_entrada, tipo_visita, monto, cantidad, total, guia):
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO detalle_entrada VALUES (?,?,?,?,?,?)", tipo_entrada, tipo_visita, monto, guia, total, cantidad)
    cursor.commit()

def borrarDetalles():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM detalle_entrada")
    cursor.commit()

def obtenerDetalles():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("select * from detalle_entrada")
    detalles = cursor.fetchone()
    return detalles
