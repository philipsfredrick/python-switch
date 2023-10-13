import socket

s = socket.socket()
host = socket.gethostname()
port = 8000

s.connect((host,port))
s.send("Hello Server".encode())
print(s.recv(1024).decode())

s.close()
