import asyncpg

import aioamqp
import asyncio_redis

from settings import RABBITMQ_PASSWORD, RABBITMQ_URL, RABBITMQ_PORT, RABBITMQ_USER, \
    PSQL_USERNAME, PSQL_PASSWORD, PSQL_PORT, PSQL_URL, PSQL_DATABASE, REDIS_URL, REDIS_PORT


async def connect_to_rabbitmq():
    transport, protocol = await aioamqp.connect(
        port=RABBITMQ_PORT,
        host=RABBITMQ_URL,
        password=RABBITMQ_PASSWORD,
        login=RABBITMQ_USER
    )

    channel = await protocol.channel()

    return transport, protocol, channel


async def connect_to_psql():
    return await asyncio_redis.Connection.create(host=REDIS_URL, port=REDIS_PORT)


async def connect_to_redis():
    return await asyncpg.connect(user=PSQL_USERNAME,
                                 password=PSQL_PASSWORD,
                                 database=PSQL_DATABASE,
                                 port=PSQL_PORT,
                                 host=PSQL_URL)
