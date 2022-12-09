import asyncio, socket


#  async functions
async def sum(a, b):
    global s
    s = int(a) + int(b)
    await asyncio.sleep(0)
    print("summ = ", s)
    return s


async def sub(a, b):
    global ss
    ss = int(a) - int(b)
    await asyncio.sleep(0)
    print("substract = ", ss)
    return ss


async def div(a, b):
    global d
    d = int(a) / int(b)
    await asyncio.sleep(0)
    print("division = ", d)
    return d



async def mul(a, b):
    global m
    m = int(a) * int(b) # return a * b
    await asyncio.sleep(0)
    print("multiplication = ", m)
    return m
# async def main():
#     f1 = loop.create_task(sum(int(ans[0]), int(ans[1])))
#     f2 = loop.create_task(div(int(ans[0]), int(ans[1])))
#     f3 = loop.create_task(mul(int(ans[0]), int(ans[1])))
#     f4 = loop.create_task(sub(int(ans[0]), int(ans[1])))
#     await asyncio.wait([f1, f2, f3, f4])



async def handle_client(client):
    loop = asyncio.get_event_loop()
    request = None
    while request != 'quit':
        request = (await loop.sock_recv(client, 255)).decode('utf8')
        ans = request.split(' ')  # Строка розділяється по пробілу
        result = "addition = {}".format(await sum(ans[0], ans[1]))
        await loop.sock_sendall(client, result.encode('utf8'))
        result = "substraction = {}".format(await sub(ans[0], ans[1]))
        await loop.sock_sendall(client, result.encode('utf8'))
        result = "division = {}".format(await div(ans[0], ans[1]))
        await loop.sock_sendall(client, result.encode('utf8'))
        result= "multiplication = {}".format(await mul(ans[0], ans[1]))
        await loop.sock_sendall(client, result.encode('utf8'))
    client.close()

async def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 15555))
    server.listen(8)
    server.setblocking(False)

    loop = asyncio.get_event_loop()

    while True:
        client, _ = await loop.sock_accept(server)
        loop.create_task(handle_client(client))

asyncio.run(run_server())



# tasks = [
        # loop.create_task(sum(int(ans[0]), int(ans[1]))),
        # loop.create_task(sub(int(ans[0]), int(ans[1]))),
        # loop.create_task(div(int(ans[0]), int(ans[1]))),
        # loop.create_task(mul(int(ans[0]), int(ans[1])))
        # ]


#
# async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
#     data = None
#
#     while True:
#         data = await reader.read(1024)  # Отримання даних від клієнта у вигляді строки "число число"
#         msg = data.decode()
#         global list_of_numbers
#         ans = msg.split(' ')  # Строка розділяється по пробілу
#         ioloop = asyncio.get_event_loop()
#         tasks = [
#             ioloop.create_task(sum(int(ans[0]), int(ans[1]))),
#             ioloop.create_task(sub(int(ans[0]), int(ans[1]))),
#             ioloop.create_task(div(int(ans[0]), int(ans[1]))),
#             ioloop.create_task(mul(int(ans[0]), int(ans[1])))
#         ]
#         wait_tasks = asyncio.wait(tasks)
#         ioloop.run_until_complete(wait_tasks)
#         # result = f'A+B={s}; A-B={ss}; A*B={m}, A/B={d}'  # Результат операцій над числами
#         # print(result)
#         # writer.write(bytes(str(result), encoding='UTF-8'))  # Відправка даних клієнту
#         # await writer.drain()
#
#     writer.close()
#
#
# async def run_server():
#     server = await asyncio.start_server(handle_client, 'localhost', 15555)
#     async with server:
#         await server.serve_forever()
#
# # asyncio.run(run_server())
# if __name__ == '__main__':
#     loop = asyncio.new_event_loop()
#     loop.run_until_complete(run_server())

# while True:
#
#     data = conn.recv(1024).decode("utf-8")
#     print(data)
#     ans = [int(a) for a in data.split()]
#
#     ioloop = asyncio.get_event_loop()
#     tasks = [ioloop.create_task(div(ans[0], ans[1])), ioloop.create_task(sub(ans[0], ans[1])), ioloop.create_task(sum(ans[0], ans[1])),
#              ioloop.create_task(mul(ans[0], ans[1]))]
#     wait_tasks = asyncio.wait(tasks)
#     ioloop.run_until_complete(wait_tasks)
#     ioloop.close()
#
#     # socket.listen(10)
#
#
# conn.close()