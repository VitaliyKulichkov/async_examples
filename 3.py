import asyncio
import aiohttp
import datetime
import time
import platform
import aiofiles


async def file_write(data):
    filename = f'name{time.time()}.jpeg'
    async with aiofiles.open(filename, 'wb') as f:
        await f.write(data)
async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        await file_write(data)

async def main():
    url = 'https://loremflickr.com/320/240'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time.time()
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main())
    print(time.time() - t0)