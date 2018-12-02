import asyncio

import aiohttp

from settings import MINUTES_STABLE_FALSE
from connections.connections import connect_to_psql, connect_to_redis
from processing_network.request_funcs import post
from domain.data_processing import get_sensor_from_cache, get_user_by_sensor_id_from_cache
from datetime import datetime, timedelta


async def send_to_user_stable_false(sensor_ids, redis_connection):
    for sensor_id in sensor_ids:
        sensor_from_cache = await get_sensor_from_cache(sensor_id, redis_connection)

        user_from_cache = await get_user_by_sensor_id_from_cache(sensor_id, redis_connection)

        data = {
            'type': 'connection_status',
            'sable': False,
            'address': sensor_from_cache['address']
        }

        user_url = user_from_cache['url']

        # todo: релизация отправки пачкой (bulk)
        async with aiohttp.ClientSession() as session:
            _ = await post(session, user_url, data)


async def get_data_with_stable_false():
    psql_connection = await connect_to_psql()
    redis_connection = await connect_to_redis()

    current_time = datetime.utcnow()

    current_time_minus_hour = current_time - timedelta(minutes=MINUTES_STABLE_FALSE)

    sensor_ids = await psql_connection.fetch('''SELECT * FROM notification_log WHERE 
    notification_time < $1''', current_time_minus_hour)

    await send_to_user_stable_false(sensor_ids, redis_connection)

    await redis_connection.close()
    redis_connection.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_data_with_stable_false())
