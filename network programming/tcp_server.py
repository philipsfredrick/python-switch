import socket

s = socket.socket()
host = socket.gethostname()
port = 8000

s.bind((host,port))

print("Waiting for connection...")
s.listen(5)

while True:
    conn,addr = s.accept()
    print("Got connection from", addr)
    print(conn.recv(1024).decode())
    conn.send("Server says Hi".encode())
    conn.close()
