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


def ObtenerSesionesBd():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM sesiones')
    sesiones = cursor.fetchall()
    return sesiones

def ObtenerUsuariosBd():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    return usuarios

def ObtenerEmpleados():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()
    return empleados



def ObtenerTarifasEnVigencia(nombre_sede, fecha):
    #create_date = datetime.strptime(fecha, '%Y-%m-%dT%H:%M:%S.%f')
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("select id_tipo_entrada, id_tipo_visita from tarifas where nombre_sede =? AND YEAR(?) BETWEEN YEAR(fecha_inicio_vigencia) and YEAR(fecha_fin_vigencia)", nombre_sede, fecha)
    tarifas = cursor.fetchall()
    return tarifas


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

def obtenerSedes():
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM sedes")
    sedes = cursor.fetchall()
    return sedes





if __name__ == '__main__':
        ObtenerTodasLasSedes()
        