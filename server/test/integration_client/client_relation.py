import aiohttp
import asyncio

from server.test.integration_client.request_funcs import post

url = 'http://localhost:8080'

data_post = {
    'sensor_id': '05b72d64-7232-4b',
    'user_id': '3'
}

headers = {
    'AUTH_TOKEN': 'some_token'
}


async def main():
    async with aiohttp.ClientSession(headers=headers) as session:
        html = await post(session, url + '/relation', data=data_post)
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
