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


def obtenerSesionActiva():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM sesiones')
    sesiones = cursor.fetchall()
    return sesiones


def obtenerDniUsuario(nombre):
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
def obtenerSedeEmpleado(dni):
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
def obtenerExposiciones():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM exposiciones") 
    exposiciones = cursor.fetchall()
      
    return exposiciones


def obtenerNombreEntrada(nro):
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM tipoEntradas")
    tiposEntradas = cursor.fetchall()
    return tiposEntradas

def obtenerTiposVisitas():
    def obtenerNombreVisita(nro):
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM tipoVisitas")
    tiposVisitas = cursor.fetchall()
    return tiposVisitas

#?para mi no tiene sentido dejarla porque el monto ya lo obtenemos por medio de la bd
"""
def ObtenerMonto(te, tv, ns):
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("select monto from tarifas where id_tipo_entrada =?  and id_tipo_visita =? and nombre_sede =?", te, tv, ns)
    monto = cursor.fetchone()
    return monto[0]
"""
'''
def cambiarFechaSesion(te, tv, ns):
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("select monto from tarifas where id_tipo_entrada =?  and id_tipo_visita =? and nombre_sede =?", te, tv, ns)
    monto = cursor.fetchone()
'''
def obtenerMonto(te, tv):
    cnxn = conexion()
    cursor = cnxn.cursor()
    monto = cursor.execute("select monto from tarifas \
            where id_tipo_entrada = ' " + te + " ' \
                 and id_tipo_visita = ' " + tv + " ' ")
    return monto


def obtenerMontoGuiaSede(nombre):
    cnxn = conexion()
    cursor = cnxn.cursor()
    monto = cursor.execute("select adicional_por_guia from sedes where nombre='" +nombre+ "'")
    return monto

def obtenerDetalleExposiciones():
    cnxn = conexion()
    cursor = cnxn.cursor()
    #fijarse que en los detalles los nombres no se repiten y deberian/es recomendable
    cursor.execute ("select * from detalleExposiciones")
    detalles = cursor.fetchall()
    return detalles


def getDuracionResumidaObra():
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

def obtenerEntradas():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("select * from Entradas")
    entradas = cursor.fetchall()
    return entradas


#!hay q eliminar esto o no
def obtenerSalas():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute ("select * from salas")
    salas = cursor.fetchall()
    return salas


'''
if __name__ == '__main__':
        ObtenerTodasLasSedes()
        '''