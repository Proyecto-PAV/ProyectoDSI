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


class Sede: 

    def ObtenerTodasLasSedes(self):
        cnxn = self.conexion()
        cursor = cnxn.cursor()
        cursor.execute('select * from sedes')
        for row in cursor:
            print(row)


    def ObtenerSesionActiva():
        pass


Sede.ObtenerTodasLasSedes()