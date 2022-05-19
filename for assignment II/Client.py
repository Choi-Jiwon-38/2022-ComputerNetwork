import socket

print("TCP Client is running")

serverPort = 3091
serverName = '127.0.0.1'

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

request_message = input('Input: ')
clientSocket.send(request_message.encode())
receive_message = clientSocket.recv(1024)

print("server: ", receive_message)