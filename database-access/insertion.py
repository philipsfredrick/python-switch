import pyodbc

# connection
conn=pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=ISW-230601-1355\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')

cur=conn.cursor()

studentFirstName = input("Enter your first name: ")
studentLastName = input("Enter your last name: ")
studentAddress = input("Enter your address: ")
studentContact = input("Enter your contacts here: ")
coursesId = int(input("Enter id of your course: "))

cur.execute("INSERT INTO Training.dbo.Students VALUES(?,?,?,?,?)",
            (studentFirstName,studentLastName,
             studentAddress,studentContact,coursesId))
cur.commit()

conn.close()
