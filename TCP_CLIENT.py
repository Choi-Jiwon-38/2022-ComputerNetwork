import socket

serverPort = 3091
serverName = '127.0.0.1'

def create_socket_and_send_message(request_message):
    # create client socket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    clientSocket.send(request_message.encode('utf-8'))

    # checking response
    receive_message = clientSocket.recv(65535)
    print(receive_message.decode())

    # closing client socket
    clientSocket.close()

# GET method - 200 OK
request_message = 'GET /meow.html HTTP/1.1\r\n'
request_message += 'Host: 127.0.0.1:12000\r\n'
request_message += 'User-Agent: Safari/537.36\r\n'
request_message += 'Connection: Keep-Alive\r\n\n'

create_socket_and_send_message(request_message)

# GET method - 404 Not Found
request_message = 'GET /mmmmmmeow.html HTTP/1.1\r\n'
request_message += 'Host: 127.0.0.1:12000\r\n'
request_message += 'User-Agent: Safari/537.36\r\n'
request_message += 'Connection: Keep-Alive\r\n'

create_socket_and_send_message(request_message)

# PUT method - 201 Create 
put_content = 'Hello my name is Choi Jiwon'
request_message = 'PUT /introduce-myself.txt HTTP/1.1\r\n'
request_message += 'Host: 127.0.0.1:12000\r\n'
request_message += 'Content-type: text/plain\r\n'
request_message += 'Content-length: ' + str(len(put_content)) +'\r\n\n'
request_message += put_content + '\r\n\n'

create_socket_and_send_message(request_message)

# POST method - 201 Create or 200 OK
post_content = 'Cat is meow meow, Dog is bow bow'
request_message = 'POST /bowbow.txt HTTP/1.1\r\n'
request_message += 'Host: 127.0.0.1:12000\r\n'
request_message += 'Content-type: text/plain\r\n'
request_message += 'Content-length: ' + str(len(post_content)) +'\r\n\n'
request_message += post_content + '\r\n\n'

create_socket_and_send_message(request_message)

# POST method - 200 OK 
post_content = 'Kookmin university computer science'
request_message = 'POST /introduce-myself.txt HTTP/1.1\r\n'
request_message += 'Host: 127.0.0.1:12000\r\n'
request_message += 'Content-type: text/plain\r\n'
request_message += 'Content-length: ' + str(len(post_content)) +'\r\n\n'
request_message += post_content + '\r\n\n'

create_socket_and_send_message(request_message)

# OPTIONS method - 200 OK 
request_message = 'OPTIONS * HTTP/1.1\r\n'
request_message += 'Host: www.localhost:' + str(serverPort) +'\r\n'
request_message += 'Accept: *\r\n\n'

create_socket_and_send_message(request_message)

# DELETE method - 200 OK 
request_message = 'DELETE /introduce-myself.txt HTTP/1.1\r\n'
request_message += 'Host: 127.0.0.1:12000\r\n\n'

create_socket_and_send_message(request_message)

# HEAD method - 200 OK
request_message = 'HEAD /meow.html HTTP/1.1\r\n'
request_message += 'Host: 127.0.0.1:12000\r\n'
request_message += 'User-Agent: Safari/537.36\r\n'
request_message += 'Connection: Keep-Alive\r\n\n'

create_socket_and_send_message(request_message)

