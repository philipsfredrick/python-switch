import pyodbc

# connection
conn=pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=ISW-230601-1355\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')

class Activity:
    def createTable(self):
        try:
            cur = conn.cursor()
            qStr = "CREATE TABLE Training.dbo.studentRecords(id int not null identity(1,1), name varchar(10), course_code varchar(10), mark int, grade varchar(5), employee_status varchar(30))"
            cur.execute(qStr)
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

    def insertRecords(self):
        try:
            cur=conn.cursor()
            studentRecords = []
            count = 0
            while True:
                name = input("Enter your name please: ")
                course_code = input("Enter your course code: ")
                mark = int(input("Enter your marks: "))
                # while mark > 100:
                #     print("Error!!!. Student mark cannot be greater than 100")
                #     mark = int(input("Enter your marks: "))
                if mark > 100:
                    print("Error!!!. Student scores should not be greater than 100")
                    mark = int(input("Enter your marks: "))
                if mark >=75 and mark <= 100:
                    grade = "A"
                    employment_status = "automatic employment"
                elif mark >= 65 and mark <=74:
                    grade = "B"
                    employment_status = "open to work"
                elif mark >= 55 and mark <= 64:
                    grade = "C"
                    employment_status = "open to work"
                else:
                    grade = "F"
                    employment_status = "probation"
                student = []
                student.append(name)
                student.append(course_code)
                student.append(mark)
                student.append(grade)
                student.append(employment_status)
                studentRecords.append(tuple(student))
                count += 1
                if count == 10:
                    break
            for student in studentRecords:
                sql = "INSERT INTO Training.dbo.studentRecords VALUES(?,?,?,?,?)"
                cur.execute(sql,student)
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

    def displayRecords(self):
        cur=conn.cursor()

        cur.execute('SELECT * FROM Training.dbo.studentRecords')

        for row in cur:
            for value in row:
                print(value,end=', ')
            print()
        conn.close()
    def displayRecordsByStatus(self):
        cur=conn.cursor()

        cur.execute("SELECT * FROM Training.dbo.studentRecords ORDER BY 'employee_status'")

        for row in cur:
            for value in row:
                print(value,end=', ')
            print()
        conn.close()


if __name__ == '__main__':
    acDB = Activity()
    # acDB.createTable()
    # acDB.insertRecords()
    # acDB.displayRecords()
    acDB.displayRecordsByStatus()
    