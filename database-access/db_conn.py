import pyodbc

# connection
conn=pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=ISW-230601-1355\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')

cur=conn.cursor()

cur.execute('SELECT * FROM Training.dbo.Students')

for row in cur:
    for value in row:
        print(value,end=', ')
    print()

conn.close()