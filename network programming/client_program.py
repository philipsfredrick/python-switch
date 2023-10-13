import socket

def client_program():

    host = '10.100.100.147'
    port = 5000
    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = input("Enter ur message: ")

    while message.lower().strip()!='weldon':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print("Recieve from server: "+ data)
        message = input("->")
    client_socket.close()

if __name__ == '__main__':

    client_program()
