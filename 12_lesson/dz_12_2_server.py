import socket
import asyncio

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("", 55555))
socket.listen(10)
print("server is running")
conn, addr = socket.accept()
print("connected:", addr) # Обмін повідомленнями можливий лише по черзі
async def sum(a, b):
    n = []
    n.append("addition = {}".format(a + b))
    await asyncio.sleep(0)
    n.append("substraction = ".format(a - b))
    await asyncio.sleep(0)
    n.append("division = ".format(a / b))
    await asyncio.sleep(0)
    n.append("multiplication = ".format(a * b))
    await asyncio.sleep(0)
    return n



while True:

    data = conn.recv(1024).decode("utf-8")
    print(data)
    ans = [int(a) for a in data.split()]
    coroutine = arif(ans[0], ans[1])
    ans = coroutine.send()
    conn.send(bytes(str(ans), encoding="UTF-8"))
    socket.listen(10)


conn.close()