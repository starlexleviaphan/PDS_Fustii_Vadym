import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("", 55555))
socket.listen(10)
print("server is running")
conn, addr = socket.accept()
print("connected:", addr) # Обмін повідомленнями можливий лише по черзі

while True:

    data = conn.recv(1024)
    print(str(bytes(data)))

    if str(bytes(data)) == "b'test'": # first key phrase
        ansv = "it`s test ansver"
    elif str(bytes(data)) == "b'byte me'": # second key phrase
        ansv = "Ha ha ha, you wish :)"
    else: ansv = str(input())
    conn.send(bytes(str(ansv), encoding="UTF-8"))
    socket.listen(10)
    a.append(str(data))

conn.close()
