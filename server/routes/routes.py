from aiohttp import web
from server.processing.users import user_get, user_create, user_update, user_delete
from server.processing.sensors import sensor_get, sensor_create, sensor_update, sensor_delete
from server.processing.notification_log import filtred_log_get
from server.processing.relation import set_relation
from settings import TOKEN


async def ping(request):
    text = 'ping'
    return web.Response(text=text)


async def user(request):
    if request.headers.get('AUTH_TOKEN') != TOKEN:
        return web.HTTPForbidden()

    if request.method == 'GET':
        return await user_get(request)
    elif request.method == 'POST':
        return await user_create(request)
    elif request.method == 'PUT':
        return await user_update(request)
    elif request.method == 'DELETE':
        return await user_delete(request)

    # TODO: PATCH


async def sensor(request):
    if request.headers.get('AUTH_TOKEN') != TOKEN:
        return web.HTTPForbidden()

    if request.method == 'GET':
        return await sensor_get(request)
    elif request.method == 'POST':
        return await sensor_create(request)
    elif request.method == 'PUT':
        return await sensor_update(request)
    elif request.method == 'DELETE':
        return await sensor_delete(request)

    # TODO: PATCH


async def relation(request):
    if request.headers.get('AUTH_TOKEN') != TOKEN:
        return web.HTTPForbidden()

    if request.method == 'POST':
        return await set_relation(request)

    # TODO: остальные методы Rest

    return await set_relation(request)


async def notification_log(request):
    if request.headers.get('AUTH_TOKEN') != TOKEN:
        return web.HTTPForbidden()

    return await filtred_log_get(request)
