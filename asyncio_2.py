import asyncio
import time

print(time.ctime())
async def main():
    print('tim')
    print(time.ctime())
    await foo('text')
    print(time.ctime())

async def foo(text):
    print(text)
    await asyncio.sleep(1)


asyncio.run(main())