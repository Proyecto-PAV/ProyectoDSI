import pyodbc
server = 'tpai-server.database.windows.net'
database = 'MUSEO'
username = 'gzr'
password = 'tpaimanero1.'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      server+';DATABASE='+database+';UID='+username+';PWD=' + password)
cursor = cnxn.cursor()

cursor.execute("SELECT s.nombre FROM dbo.sedes s;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()
