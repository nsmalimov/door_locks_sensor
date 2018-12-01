import aiohttp
import asyncio

url = 'http://localhost:8080'


async def get(session, url):
    async with session.get(url) as response:
        return await response.text()


async def post(session, url, data):
    async with session.post(url, data=data) as response:
        return await response.text()


async def put(session, url):
    async with session.put(url) as response:
        return await response.text()


async def delete(session, url):
    async with session.delete(url) as response:
        return await response.text()


data_post = {
    'name': 'Андрей',
    'url': 'some url 2'
}

headers = {
    'AUTH_TOKEN': 'some_token'
}


async def main():
    # async with aiohttp.ClientSession(headers=headers) as session:
    #     html = await post(session, url + '/user', data_post)
    #     print(html)

    async with aiohttp.ClientSession(headers=headers) as session:
        html = await get(session, url + '/user?id=1')
        print(html)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
