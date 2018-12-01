from server.app import app
from aiohttp import web


# TODO: кеширование
async def sensor_get(request):
    try:
        return web.Response(text='Ok')
    except Exception as e:
        return web.HTTPServerError(text=f'error: {e}')


async def sensor_create(request):
    try:
        return web.Response(text='Ok')
    except Exception as e:
        return web.HTTPServerError(text=f'error: {e}')


async def sensor_update(request):
    try:
        return web.Response(text='Ok')
    except Exception as e:
        return web.HTTPServerError(text=f'error: {e}')


async def sensor_delete(request):
    try:
        return web.Response(text='Ok')
    except Exception as e:
        return web.HTTPServerError(text=f'error: {e}')
