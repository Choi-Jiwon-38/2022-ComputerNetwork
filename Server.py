import socket

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
        CONNECTION.send(DATA)
        print("client >> ", DATA.decode())