import socket
import datetime
import os

serverPort = 3091
serverIp = '127.0.0.1'
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverIp, serverPort))

print(os.listdir())


serverSocket.listen()
print('TCP server is running')

while 1:
    connectionSocket, addr = serverSocket.accept()
    try:    
        message = connectionSocket.recv(65535).decode()
        request_headers = message.split()
        if request_headers[2] == 'HTTP/1.1' and request_headers[0] in ['GET', 'HEAD']:
            try: # 존재하는 주소로 접근하는 경우 / html 파일에 접근할 수 있는 경우
                html_file = open(request_headers[1][1:], 'r')
                html_file_content = html_file.read()
                html_file.close()
                
                respomse_message = 'HTTP/1.1 200 OK\n'
                respomse_message += 'Content-Type: text/html\n'
                respomse_message += 'Content-Length: ' + str(len(html_file_content)) + '\n'
                response_message += 'Date: '  + datetime.datetime.now().strftime("%a, %d %b %Y %H:%M") + ' KST\n'
                
                if request_headers[2] == 'GET': # GET 명령어는 HTML 본문을 읽어옴 -> HEAD는 상태 확인 용도
                    response_message += html_file_content + '\n\n'
                else: # HEAD의 경우에는 html 본문을 return 하지 않으므로 생략
                    pass 
            
            except: # 존재하지 않는 주소에 접근하려는 경우
                response_message = 'HTTP/1.1 404 Not Found\n'
                response_message += 'Content-Type: text/html\n'
                response_message += 'Date: ' + datetime.datetime.now().strftime("%a, %d %b %Y %H:%M") + ' KST\n'
        
        elif request_headers[2] == 'HTTP/1.1' and request_headers[0] in ['PUT', 'POST']:
            if request_headers[0] == 'PUT':
                html_file_length = 0
                html_file = open(request_headers[1][1:], 'w')
                for i in range(9, len(request_headers)):
                    html_file.write(request_headers[i] + ' ')
                    html_file_length = len(request_headers[i] + 1)
                html_file.close()

                respomse_message = 'HTTP/1.1 201 Created\n'
                respomse_message += 'Location: http://localhost:' + str(serverPort) + request_headers[1]
                respomse_message += 'Content-Type: text/plain\n'
                respomse_message += 'Content-Length: ' + str(html_file_length) + '\n'
                response_message += 'Date: '  + datetime.datetime.now().strftime("%a, %d %b %Y %H:%M") + ' KST\n\n'
                response_message += 'http://localhost:' + str(serverPort) + request_headers[1]
            else: # request_headers[0] == 'POST':
                try:
                    html_file = open(request_headers[1][1:], 'a') # mode a는 파일의 마지막에 새로운 내용을 추가할 때 사용
                    html_file_updated_content = ""

                    for i in range(9, len(request_headers)):
                        html_file.write(request_headers[i] + ' ')
                        html_file_updated_content += request_headers[i] + ''
                    html_file.close()

                    respomse_message = 'HTTP/1.1 200 OK\n'
                    respomse_message += 'Location: http://localhost:' + str(serverPort) + request_headers[1]
                    respomse_message += 'Content-Type: text/plain\n'
                    respomse_message += 'Content-Length: ' + len(html_file_updated_content) + '\n'
                    response_message += 'Date: '  + datetime.datetime.now().strftime("%a, %d %b %Y %H:%M") + ' KST\n\n'
                    response_message += html_file_updated_content
                
                except FileNotFoundError: # 존재하지 않는 경우에는 PUT처럼 생성해줌.
                    respomse_message = 'HTTP/1.1 201 Created\n'
                    respomse_message += 'Location: http://localhost:' + str(serverPort) + request_headers[1]
                    respomse_message += 'Content-Type: text/plain\n'
                    respomse_message += 'Content-Length: ' + str(html_file_length) + '\n'
                    response_message += 'Date: '  + datetime.datetime.now().strftime("%a, %d %b %Y %H:%M") + ' KST\n\n'
                    response_message += 'http://localhost:' + str(serverPort) + request_headers[1]
        
        elif request_headers[2] == 'HTTP/1.1' and request_headers[0] == 'DELETE':
            os.remove(request_headers[1][1:])
            respomse_message = 'HTTP/1.1 200 OK\n'
            respomse_message += 'Content-Type: text/plain\n'
            response_message += 'Date: '  + datetime.datetime.now().strftime("%a, %d %b %Y %H:%M") + ' KST\n\n'
            response_message += 'I have your delete request, will take time to process\n\n'
            
        elif request_headers[2] == 'HTTP/1.1' and request_headers[0] in 'OPTIONS':
            respomse_message = 'HTTP/1.1 200 OK\n'
            respomse_message += 'Allow: GET, HEAD, POST, PUT, OPTIONS, DELETE\n'
            respomse_message += 'Content-Length: 0\n'
            response_message += 'Date: '  + datetime.datetime.now().strftime("%a, %d %b %Y %H:%M") + ' KST\n\n'
    except:
        pass

    connectionSocket.send(response_message.encode())
