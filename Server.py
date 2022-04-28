import socket # module import

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# SOCK_STREAM : socket of TCP
# AF_INET : address format, IPv4 <- commonly used


HOST = socket.gethostbyname(socket.gethostname())
print(HOST)

serverSocket.bind(HOST)

serverSocket.listen()
clientSocket, address = serverSocket.acept()

print('Connected by', address)

while 1:
    data = clientSocket.recv(1024)

    if not data:
        break

    print('Received from', address, data.decode())

    clientSocket.sendall(data)

clientSocket.close()
serverSocket.close()