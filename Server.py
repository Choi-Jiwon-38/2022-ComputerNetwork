from ast import Try
import socket
import requests


HOST = "127.0.0.1" # localhost == 내 컴퓨터
PORT = 3091

ADDRESS = (HOST, PORT)

print(ADDRESS)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as SERVER:
    
    SERVER.bind(ADDRESS)
    SERVER.listen()
    print("Server is started ...")
    
    CONNECTION, ADDRESS = SERVER.accept()
    print("Connected client = {} : {}".format(ADDRESS[0], ADDRESS[1]))
    
    while True:
        DATA = CONNECTION.recv(1024)
        
        if DATA.decode() == "q":
            print("Quit connection")
            break
        
        FUNC, URL = DATA.decode().split()
        JSON = {"outer": {"inner": "value"}}


        print("client >> ", DATA.decode())

        # Python3의 각 명령어 수행 뒤, 파일 입출력을 사용하기 위해 변수 설정
        fileName = FUNC + "_" + URL.replace("http://", "") + ".txt" 

        if FUNC == "GET":
            RESPONSE = requests.get(URL)
        
            try:
                f = open(fileName, 'w')
                print('success - w')
            except:
                f = open(fileName, 'x')
                print('success - x')
            f.write(str(RESPONSE))
            f.close()

        elif FUNC == "HEAD":
            RESPONSE = requests.head(URL)
        
            try:
                f = open(fileName, 'w')
                print('success - w')
            except:
                f = open(fileName, 'x')
                print('success - x')
            f.write(str(RESPONSE))
            f.close()

        elif FUNC == "POST":
            RESPONSE = requests.post(URL, data = JSON)

            try:
                f = open(fileName, 'w')
                print('success - w')
            except:
                f = open(fileName, 'x')
                print('success - x')
            f.write(str(RESPONSE))
            f.close()

        elif FUNC == "PUT":
            RESPONSE = requests.put(URL, data = JSON)

            try:
                f = open(fileName, 'w')
                print('success - w')
            except:
                f = open(fileName, 'x')
                print('success - x')
            f.write(str(RESPONSE))
            f.close()

        else:
            RESPONSE = "usage: GET/HEAD/POST/PUT (ADDRESS)"

        if RESPONSE.status_code == 200:
            MESSAGE = "200 OK"
        elif RESPONSE.status_code == 400:
            MESSAGE = "404 Bad Request"
        else:
            MESSAGE = str(RESPONSE.status_code) # 아래에서 encode를 하기 위해 str로 형변환

        CONNECTION.send(MESSAGE.encode())

        