import asyncio


async def sum(a, b):
    # return a + b
    ans = a + b
    await asyncio.sleep(0)
    print(ans)

async def sub(a, b):
    ans = a - b
    await asyncio.sleep(0)
    print(ans)

async def div(a, b):
    ans = a / b
    await asyncio.sleep(0)
    print(ans)

async def mul(a, b):
    ans = a * b# return a * b
    await asyncio.sleep(0)
    print(ans)
a = 21
b = 45
ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(sum(a, b)), ioloop.create_task(sub(a, b)), ioloop.create_task(div(a, b)), ioloop.create_task(mul(a, b))]
ioloop.run_until_complete(asyncio.wait((tasks)))
ioloop.close()