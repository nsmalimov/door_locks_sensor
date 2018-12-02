from connections.connections import connect_to_redis, connect_to_psql
from aiohttp import web
from server.routes import routes
import asyncio
from settings import PORT

app = web.Application()


# todo: autorestart при изменении кода

def setup_routes(app):
    app.router.add_route('*', '/', routes.ping)

    app.router.add_route('*', '/user', routes.user)
    app.router.add_route('*', '/sensor', routes.sensor)

    app.router.add_route('*', '/relation', routes.relation)

    app.router.add_route('*', '/notification_log', routes.notification_log)


async def init_connections(app):
    # todo: можно разделить и обрабатывать exceptions каждого
    app.psql_connection = await connect_to_psql()

    app.redis_connection = await connect_to_redis()


def setup_connections(app):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_connections(app))


if __name__ == '__main__':
    setup_connections(app)

    setup_routes(app)

    web.run_app(app, host='127.0.0.1', port=PORT)
