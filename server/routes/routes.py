from aiohttp import web

async def ping(request):
    text = 'ping'
    return web.Response(text=text)