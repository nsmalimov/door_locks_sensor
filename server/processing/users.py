from aiohttp import web
import logging
import json


# TODO: поиск не только по айди, но и по имени, используя, например sphinx или Elasticsearch
# через like будет долго
async def user_get(request):
    try:
        id = request.rel_url.query['id']

        cache_key = f'user_{id}'

        value_from_cache = await request.app.redis_connection.get(cache_key)

        if value_from_cache is None:
            value = await request.app.psql_connection.fetchrow('''SELECT * FROM user_table WHERE id=$1''',
                                                                int(id))
            value = dict(value)

            await request.app.redis_connection.set(cache_key, json.dumps(value))
        else:
            return web.Response(text=value_from_cache)

        return web.json_response(value)
    except Exception as e:
        text_exception = f'user_get error: {e}'
        print(text_exception)
        logging.exception(text_exception)
        return web.HTTPBadRequest(text=text_exception)


async def user_create(request):
    # через классы
    try:
        data = await request.post()
        await request.app.psql_connection.execute('''
        INSERT INTO user_table(name, url) VALUES($1, $2)
    ''', data['name'], data['url'])

        # обработка того, что юзер уже существует

        return web.Response(text='Ok')
    except Exception as e:
        text_exception = f'user_get error: {e}'
        print(text_exception)
        logging.exception(text_exception)
        return web.HTTPBadRequest(text=text_exception)


async def user_update(request):
    try:
        id = int(request.rel_url.query['id'])

        data = await request.post()

        await request.app.psql_connection.execute('''
                UPDATE user_table SET name=$1, url=$2 where id=$3
            ''', data['name'], data['url'], id)

        return web.Response(text='Ok')
    except Exception as e:
        text_exception = f'user_update error: {e}'
        print(text_exception)
        logging.exception(text_exception)
        return web.HTTPBadRequest(text=text_exception)


# TODO: научить удалять не только по id
async def user_delete(request):
    try:
        id = int(request.rel_url.query['id'])

        await request.app.psql_connection.execute('''
                        DELETE FROM user_table where id=$1
                    ''', id)

        return web.Response(text='Ok')
    except Exception as e:
        text_exception = f'user_delete error: {e}'
        print(text_exception)
        logging.exception(text_exception)
        return web.HTTPBadRequest(text=text_exception)
