async def get(session, url):
    async with session.get(url) as response:
        return await response.text()


async def post(session, url, data):
    async with session.post(url, data=data) as response:
        return await response.text()


async def put(session, url, data):
    async with session.put(url, data=data) as response:
        return await response.text()


async def delete(session, url):
    async with session.delete(url) as response:
        return await response.text()
