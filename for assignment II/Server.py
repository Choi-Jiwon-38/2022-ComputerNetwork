import socket

serverPort = 3091
serverIp = '127.0.0.1'
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverIp, serverPort))

serverSocket.listen()
print('TCP server is running')

while 1:
    connectionSocket, addr = serverSocket.accept()
    print('TCP Client Connected . . .')
    message = connectionSocket.recv(1024)
    print("receive: ", message)

    connectionSocket.send(message)
    connectionSocket.close()
