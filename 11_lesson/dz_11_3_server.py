import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("", 55555))
socket.listen(10)
print("server is running")
conn, addr = socket.accept()
print("connected:", addr) # Обмін повідомленнями можливий лише по черзі

while True:

    data = conn.recv(1024)
    # print(str(bytes(data)))
    a = bytes(data).decode("utf-8")
    print(a)
    ansv = len(a.split())

    conn.send(bytes(str(ansv), encoding="UTF-8"))
    socket.listen(10)

conn.close()
