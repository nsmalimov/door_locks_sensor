from aiohttp import web
import logging
import json


# TODO: кеширование
# поиск не только по айди, но и по имени, используя, например sphinx или Elasticsearch
async def user_get(request):
    try:
        id = request.rel_url.query['id']

        cache_key = f'user_{id}'

        value_from_cache = await request.app.redis_connection.get(cache_key)

        if value_from_cache is None:
            values = await request.app.psql_connection.fetchrow('''SELECT * FROM user_table WHERE id=$1''',
                                                                int(id))
            values = dict(values)

            await request.app.redis_connection.set(cache_key, json.dumps(values))
        else:
            values = value_from_cache

        return web.json_response(values)
    except Exception as e:
        text_exception = f'user_get error: {e}'
        print(text_exception)
        logging.exception(text_exception)
        return web.HTTPServerError(text=text_exception)


async def user_create(request):
    data = await request.post()

    # через классы
    try:
        await request.app.psql_connection.execute('''
        INSERT INTO user_table(name, url) VALUES($1, $2)
    ''', data['name'], data['url'])

        # обработка того, что юзер уже существует

        return web.Response(text='Ok')
    except Exception as e:
        text_exception = f'user_get error: {e}'
        print(text_exception)
        logging.exception(text_exception)
        return web.HTTPServerError(text=text_exception)


async def user_update(request):
    try:
        return web.Response(text='Ok')
    except Exception as e:
        text_exception = f'user_update error: {e}'
        print(text_exception)
        logging.exception(text_exception)
        return web.HTTPServerError(text=text_exception)


async def user_delete(request):
    try:
        id = request.rel_url.query['id']

        return web.Response(text='Ok')
    except Exception as e:
        text_exception = f'user_delete error: {e}'
        print(text_exception)
        logging.exception(text_exception)
        return web.HTTPServerError(text=text_exception)
