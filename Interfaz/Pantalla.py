import pyodbc
server = 'tpai-server.database.windows.net'
database = 'MUSEO'
username = 'gzr'
password = 'tpaimanero1.'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      server+';DATABASE='+database+';UID='+username+';PWD=' + password)
cursor = cnxn.cursor()

def usuario(nUsuario, cUsuario):
    user = nUsuario
    contra = cUsuario
    cursor.execute('SELECT nombre_usuario, contraseña FROM usuarios WHERE nombre_usuario = ? and contraseña = ?', user, contra)
    row = cursor.fetchone()
    if row == None:
        return
    else:
        return True



