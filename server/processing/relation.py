from aiohttp import web
import logging


async def set_relation(request):
    # через классы
    try:
        data = await request.post()
        await request.app.psql_connection.execute('''
        INSERT INTO sensor_user(sensor_id, user_id) VALUES($1, $2)
    ''', data['sensor_id'], int(data['user_id']))

        return web.Response(text='Ok')
    except Exception as e:
        text_exception = f'set_relation error: {e}'
        print(text_exception)
        logging.exception(text_exception)
        return web.HTTPBadRequest(text=text_exception)
