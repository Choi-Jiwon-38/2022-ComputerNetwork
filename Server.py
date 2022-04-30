import socket
import requests

HOST = "127.0.0.1" # 127.0.0.1 == localhost == 내 컴퓨터
PORT = 3091

ADDRESS = (HOST, PORT)

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
            exit()
        
        FUNC, URL = DATA.decode().split()
        JSON = {"outer": {"inner": "value"}}


        print("client >> ", DATA.decode())


        if FUNC == "GET":
            RESPONSE = requests.get(URL)
        
        elif FUNC == "HEAD":
            RESPONSE = requests.head(URL)
        
        elif FUNC == "POST":
            RESPONSE = requests.post(URL, data = JSON)

        elif FUNC == "PUT":
            RESPONSE = requests.put(URL, data = JSON)

        else:
            RESPONSE = "usage: GET/HEAD/POST/PUT (ADDRESS)"


        if RESPONSE.status_code == 200:
            MESSAGE = "200 OK"
        elif RESPONSE.status_code == 400:
            MESSAGE = "404 Bad Request"
        else:
            MESSAGE = str(RESPONSE.status_code) # 아래에서 encode를 하기 위해 str로 형변환

        CONNECTION.send(MESSAGE.encode())

        