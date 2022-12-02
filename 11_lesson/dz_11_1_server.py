import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("", 55555))
socket.listen(10)
print("server is running")
conn, addr = socket.accept()
print("connected:", addr) # Обмін повідомленнями можливий лише по черзі
while True:

    data = conn.recv(1024)
    print(str(data))
    conn.send(bytes(str(input()), encoding="UTF-8"))
    socket.listen(10)
conn.close()