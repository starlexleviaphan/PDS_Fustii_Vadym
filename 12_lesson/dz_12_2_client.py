import asyncio

HOST = 'localhost'
PORT = 15555


async def run_client():
    reader, writer = await asyncio.open_connection(HOST, PORT)
    a = input('Number A:') # Введення чисел
    b = input('Number B:')
    r = f'{a} {b}' # Переведення пари чисел у строку
    writer.write(bytes(str(r), encoding='UTF-8')) # Відправка даних на сервер
    await writer.drain()

    while True:
        data = await reader.read(1024)

        if not data:
            raise Exception('socket closed')

        print(f'{data.decode()}') # Друкування відповіді

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(run_client())