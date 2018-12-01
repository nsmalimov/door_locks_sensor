import asyncio_redis
import asyncpg
from aiohttp import web
from server.routes import routes
import asyncio
from settings import PSQL_USERNAME, PSQL_PASSWORD, PSQL_PORT, PSQL_URL, PSQL_DATABASE, PORT, REDIS_URL, REDIS_PORT

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
    app.psql_connection = await asyncpg.connect(user=PSQL_USERNAME,
                                 password=PSQL_PASSWORD,
                                 database=PSQL_DATABASE,
                                 port=PSQL_PORT,
                                 host=PSQL_URL)

    app.redis_connection = await asyncio_redis.Connection.create(host=REDIS_URL, port=REDIS_PORT)


def setup_connections(app):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_connections(app))


if __name__ == '__main__':
    setup_connections(app)

    setup_routes(app)

    web.run_app(app, host='127.0.0.1', port=PORT)
