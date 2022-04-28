import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 3091      


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 지정한 HOST와 PORT를 사용하여 서버에 접속합니다. 
clientSocket.connect((HOST, PORT))

# 메시지를 전송합니다. 
clientSocket.sendall('안녕'.encode())

# 메시지를 수신합니다. 
data = clientSocket.recv(1024)
print('Received', repr(data.decode()))

# 소켓을 닫습니다.
clientSocket.close()