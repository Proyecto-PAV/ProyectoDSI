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
def ObtenerExposicionesEnVigencia(nombre_sede, fecha):
    #corroborar la matriz
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute( "select * from exposiciones WHERE nombre_sede=? AND  \
        ( ? BETWEEN fecha_inicio_replanificada AND fecha_fin_replanificada  \
        AND fecha_inicio_replanificada IS NOT NULL AND fecha_fin_replanificada IS NOT NULL)\
        OR (? BETWEEN fecha_inicio and fecha_fin) )", nombre_sede, fecha, fecha)

    exposiciones = cursor.fetchone()
    return exposiciones


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






if __name__ == '__main__':
        ObtenerTodasLasSedes()
        