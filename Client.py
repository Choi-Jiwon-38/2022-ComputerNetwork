import socket

IP = "127.0.0.1"
PORT = 3091

ADDRESS = (IP, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as CLIENT: # 클라이언트 소켓을 만든 뒤, CLIENT로 지칭
    CLIENT.connect(ADDRESS)

    MESSAGE = input("<< ").encode() # 클라이언트가 서버에 전송할 메시지 입력 (input)
    CLIENT.send(MESSAGE) # 메시지 전송 (클라이언트 -> 서버)

    DATA = CLIENT.recv(1024) # 데이터 수신 (클라이언트 <- 서버)
    print(">>", DATA.decode()) # decode 마친 후 출력

    CLIENT.close() # 소켓 닫기