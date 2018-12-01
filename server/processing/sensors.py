from aiohttp import web
import logging
import json


# TODO: поиск не только по айди, но и по адресу, используя, например sphinx или Elasticsearch
# через like будет долго
async def sensor_get(request):
    try:
        id = request.rel_url.query['id']

        cache_key = f'sensor_{id}'

        value_from_cache = await request.app.redis_connection.get(cache_key)

        if value_from_cache is None:
            value = await request.app.psql_connection.fetchrow('''SELECT * FROM sensor WHERE id=$1''',
                                                                id)
            value = dict(value)

            await request.app.redis_connection.set(cache_key, json.dumps(value))
        else:
            return web.Response(text=value_from_cache)

        return web.json_response(value)
    except Exception as e:
        text_exception = f'sensor_get error: {e}'
        print(text_exception)
        logging.exception(text_exception)
        return web.HTTPBadRequest(text=text_exception)


async def sensor_create(request):
    # через классы
    try:
        data = await request.post()
        await request.app.psql_connection.execute('''
        INSERT INTO sensor(id, address) VALUES($1, $2)
    ''', data['id'], data['address'])

        # обработка того, что датчик с таким id уже существует

        return web.Response(text='Ok')
    except Exception as e:
        text_exception = f'sensor_get error: {e}'
        print(text_exception)
        logging.exception(text_exception)
        return web.HTTPBadRequest(text=text_exception)


async def sensor_update(request):
    try:
        id = request.rel_url.query['id']

        data = await request.post()

        await request.app.psql_connection.execute('''
                UPDATE sensor SET id=$1, address=$2 where id=$3
            ''', data['id'], data['address'], id)

        return web.Response(text='Ok')
    except Exception as e:
        text_exception = f'sensor_update error: {e}'
        print(text_exception)
        logging.exception(text_exception)
        return web.HTTPBadRequest(text=text_exception)


# TODO: научить удалять не только по id
async def sensor_delete(request):
    try:
        id = request.rel_url.query['id']

        await request.app.psql_connection.execute('''
                        DELETE FROM sensor where id=$1
                    ''', id)

        return web.Response(text='Ok')
    except Exception as e:
        text_exception = f'sensor_delete error: {e}'
        print(text_exception)
        logging.exception(text_exception)
        return web.HTTPBadRequest(text=text_exception)
