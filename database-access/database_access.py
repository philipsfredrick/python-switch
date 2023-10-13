import pyodbc

for driver in pyodbc.drivers():
    print(driver)

# Steps for python database programming
# 1. Import database-specific module
# 2. Establish a connection towards a database with credentials in a secured way
# 3. Create Cursor object
# 4. Use in-built methods to execute SQL queries
# 5. Commit or rollback
# 6. Fetch result from your driver.
# import socket

# s = socket.socket()
# host = socket.gethostbyname()
# port = 9999

# s.bind((host,port))

# print("Waiting for connection....")
# s.listen(5)

# while True:
#     conn,addr = s.accept()
#     print("Got connection from", addr)
#     conn.send("Server saying Hi.".encode())
#     conn.close

