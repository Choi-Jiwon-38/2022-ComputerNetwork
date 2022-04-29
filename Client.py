import socket

IP = "127.0.0.1"
PORT = 3091

ADDRESS = (IP, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as CLIENT:
    CLIENT.connect(ADDRESS)
    while True:
        MESSAGE = input().encode()
        CLIENT.send(MESSAGE)
        DATA = CLIENT.recv(1024)
        print(DATA.decode())