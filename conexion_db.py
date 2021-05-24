import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-CBP7KEN\SQLEXPRESS;'
                      'Database=GDA;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute(
    """SELECT * FROM GDA.dbo.empleados e WHERE e.apellido LIKE '%a' """)

for row in cursor:
    print(row)
