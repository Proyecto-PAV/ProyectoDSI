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


def ObtenerTodasLasSedes():
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

def obtenerTiposVisitas():
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
if __name__ == '__main__':
        ObtenerTodasLasSedes()
        