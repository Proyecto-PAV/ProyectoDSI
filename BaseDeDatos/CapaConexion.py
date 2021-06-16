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
   

def ObtenerTarifasEnVigencia(nombre_sede, fecha):
    #create_date = datetime.strptime(fecha, '%Y-%m-%dT%H:%M:%S.%f')
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("select id_tipo_entrada, id_tipo_visita from tarifas where nombre_sede =? AND YEAR(?) BETWEEN YEAR(fecha_inicio_vigencia) and YEAR(fecha_fin_vigencia)", nombre_sede, fecha)
    tarifas = cursor.fetchall()
    return tarifas


def ObtenerNombreEntrada(nro):
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("select nombre from tipoEntradas where id_tipo_entrada =?", nro)
    nombre = cursor.fetchone()
    return nombre[0]

def ObtenerNombreVisita(nro):
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("select nombre from tipoVisitas where id_tipo_visita =?", nro )
    nombre = cursor.fetchone()
    return nombre[0]


def ObtenerMonto(te, tv, ns):
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("select monto from tarifas where id_tipo_entrada =?  and id_tipo_visita =? and nombre_sede =?", te, tv, ns)
    monto = cursor.fetchone()
    return monto[0]


def ObtenerMontoGuiaSede(nombre):
    cnxn = conexion()
    cursor = cnxn.cursor()
    cursor.execute("select adicional_por_guia from sedes where nombre=?", nombre)
    adicionalMonto = cursor.fetchone()
    return adicionalMonto[0]






if __name__ == '__main__':
        ObtenerTodasLasSedes()
        