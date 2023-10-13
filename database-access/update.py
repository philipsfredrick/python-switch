import pyodbc

# connection
# conn=pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=ISW-230601-1355\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')

# cur=conn.cursor()

# studentId = int(input("Please enter your student id: "))
# studentFirstName = input("Enter your first name: ")
# studentLastName = input("Enter your last name: ")


# cur.execute("UPDATE Training.dbo.Students SET student_first_name = ?, student_last_name = ? WHERE ID = ?",
#             (studentFirstName,studentLastName,studentId))
# cur.commit()

# conn.close()
conn=pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=ISW-230601-1355\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')


class DatabaseAccess:
    def update(self):
        cur=conn.cursor()

        studentId = int(input("Please enter your student id: "))
        studentFirstName = input("Enter your first name: ")
        studentLastName = input("Enter your last name: ")

        cur.execute("UPDATE Training.dbo.Students SET student_first_name = ?, student_last_name = ? WHERE ID = ?",
            (studentFirstName,studentLastName,studentId))
        cur.commit()

        conn.close()

    def delete(self):
        cur=conn.cursor()

        studentId = int(input("Enter ID for DELETE: "))
        
        cur.execute('DELETE FROM Training.dbo.Students WHERE ID = ?',(studentId))

        cur.commit()

        conn.close()

    def selectById(self):
        cur=conn.cursor()

        studentId = int(input("Enter ID to SELECT ROW: "))
        
        cur.execute('SELECT * FROM Training.dbo.Students WHERE ID = ?',(studentId))

        for row in cur:
            for value in row:
                print(value,end=', ')
            print()
        cur.commit()

        conn.close()

    def createTable(self):
        try:
            cur = conn.cursor()
            cur.execute("CREATE TABLE Training.dbo.employees(eno int,ename varchar(10),esal decimal(10,2),eaddr varchar(10))")
            print("Table created successfully")
            conn.commit()
        except pyodbc.Error as e:
            if conn:
                conn.rollback()
                print(e)
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
    
    def multipleInsert(self):
        try:
            cur=conn.cursor()
            sql = "INSERT INTO Training.dbo.employees VALUES(?,?,?,?)"
            records = [(1,'Harry',30000,'UK'),(2,'Gary',40000,'Spain'),(3,'Cole',50000,'US')]
            cur.executemany(sql,records)
            conn.commit()
            print("Record Inserted Successfully")
        except pyodbc.Error as e:
            if conn:
                conn.rollback()
                print(e)
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    # def multipleRequests(self):
    #     try:
    #         cur = conn.cursor()
    #         while True:
    #             eno = int(input("Enter your employee number: "))
    #             ename = input("Enter employee name: ")
    #             esal = float(input("Enter your salary: "))
    #             eaddr = input("Enter your address: ")
    #             sql = "INSERT INTO Training.dbo.employees VALUES(?,?,?,?)"
    #     except:
if __name__ == '__main__':
    myDB = DatabaseAccess()
    # myDB.update()
    # myDB.delete()
    # myDB.selectById()
    # myDB.createTable()
    myDB.multipleInsert()
    # DatabaseAccess().update()