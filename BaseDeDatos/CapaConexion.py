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
    cursor.execute('select nombre_usuario from sesiones where fecha_fin IS NULL')
    sesion = cursor.fetchone()
    return sesion[0]


def obtenerDniUsuario(nombre):
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("select dni_empleado from usuarios where nombre_usuario=?", nombre  )
    dni = cursor.fetchone()
    return dni[0]


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
def obtenerExposicionesEnVigencia(nombre_sede, fecha):
    #!comprobar el porque nos devuelve solo el primero
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM exposiciones WHERE nombre_sede=? \
        AND (? BETWEEN fecha_inicio_replanificada AND fecha_fin_replanificada \
        AND fecha_inicio_replanificada IS NOT NULL AND fecha_fin_replanificada IS NOT NULL) \
        OR (? BETWEEN fecha_inicio and fecha_fin) ", nombre_sede, fecha, fecha) 
    exposiciones = cursor.fetchall()
  
    return exposiciones


def obtenerNombreEntrada(nro):
    cnxn = conexion()
    cursor = cnxn.cursor()
    nombre= cursor.execute("select nombre from tipoEntradas where id_tipo_entrada ='" +nro+ "'")
    return nombre

def obtenerNombreVisita(nro):
    cnxn = conexion()
    cursor = cnxn.cursor()
    nombre= cursor.execute("select nombre from tipoVisitas where id_tipo_visita =' " + nro + " ' ")
    return nombre


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

def obtenerDetalleExposiciones(nombre_expo):
    cnxn = conexion()
    cursor = cnxn.cursor()
    #fijarse que en los detalles los nombres no se repiten y deberian
    cursor.execute ( "select * from detalleExposiciones WHERE nombre_exposicion=?", nombre_expo)
    detalles = cursor.fetchall()

    return detalles


def getDuracionResumidaObra(self, nombre):
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute ("select duracion_resumida from obras WHERE nombre_obra=?", nombre)
    obra = cursor.fetchone()

    return obra

'''
if __name__ == '__main__':
        ObtenerTodasLasSedes()
        '''