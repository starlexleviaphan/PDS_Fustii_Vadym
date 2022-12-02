import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("localhost", 55555))
while True:

    socket.send(bytes(str(input()), encoding="UTF-8"))
    data = socket.recv(1024)
    print(data)
socket.close()
