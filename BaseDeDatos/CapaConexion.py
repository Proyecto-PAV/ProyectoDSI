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
    nombre = cursor.execute('select nombre_usuario from sesiones where fecha_fin IS NULL')
    return nombre


def ObtenerDniUsuario(nombre):
    cnxn = conexion()
    cursor = cnxn.cursor()
    dni = cursor.execute("select dni_empleado from usuarios where nombre_usuario= '" + nombre + "'" )
    return dni


def ObtenerSedeEmpleado(dni):
    cnxn = conexion()
    cursor = cnxn.cursor()
    sede = cursor.execute("select nombre_sede from empleados where dni= '" + dni + "'" )
    return sede

if __name__ == '__main__':
        ObtenerTodasLasSedes()