import aiohttp
import asyncio

from processing_network.request_funcs import delete

url = 'http://localhost:8080'



data_post = {
    'name': 'Андрей',
    'url': 'some url 2'
}

data_put = {
    'name': 'Андрей 444',
    'url': 'some url 111'
}


headers = {
    'AUTH_TOKEN': 'some_token'
}


async def main():
    # async with aiohttp.ClientSession(headers=headers) as session:
    #     html = await post(session, url + '/user', data_post)
    #     print(html)

    # async with aiohttp.ClientSession(headers=headers) as session:
    #     html = await get(session, url + '/user?id=1')
    #     print(html)

    # async with aiohttp.ClientSession(headers=headers) as session:
    #     html = await put(session, url + '/user?id=1', data_put)
    #     print(html)

    async with aiohttp.ClientSession(headers=headers) as session:
        html = await delete(session, url + '/user?id=1')
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
