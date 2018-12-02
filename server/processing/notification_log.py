from server.app import app
from aiohttp import web


# TODO: кеширование
async def filtred_log_get(request):
    try:
        # TODO: сделать фильтрацию
        # запросы в базу с 'where'
        return web.Response(text='Ok')
    except Exception as e:
        return web.HTTPServerError(text=f'error: {e}')
