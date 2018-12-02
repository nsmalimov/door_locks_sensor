import aiohttp
import asyncio
import uuid


from processing_network.request_funcs import delete

url = 'http://localhost:8080'



data_post = {
    'id': str(uuid.uuid4())[0:16],
    'address': 'Москва'
}

data_put = {
    'id': str(uuid.uuid4())[0:16],
    'address': 'Санкт-Петербург'
}


headers = {
    'AUTH_TOKEN': 'some_token'
}


async def main():
    # async with aiohttp.ClientSession(headers=headers) as session:
    #     html = await post(session, url + '/sensor', data_post)
    #     print(html)

    # async with aiohttp.ClientSession(headers=headers) as session:
    #     html = await get(session, url + '/sensor?id=89c19078-db58-49')
    #     print(html)

    # async with aiohttp.ClientSession(headers=headers) as session:
    #     html = await put(session, url + '/sensor?id=89c19078-db58-49', data_put)
    #     print(html)

    async with aiohttp.ClientSession(headers=headers) as session:
        html = await delete(session, url + '/sensor?id=a6d27c72-c1ac-4a')
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
