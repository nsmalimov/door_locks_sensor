import json


# такие же функции, но через psql

async def get_user_by_sensor_id_from_cache(sensor_id, redis_connection):
    user_id = await redis_connection.get(f'relation_sensor_{sensor_id}')

    return await get_user_from_cache(user_id, redis_connection)

async def get_user_from_cache(user_id, redis_connection):
    return json.loads(await redis_connection.get(f'user_{user_id}'))

async def get_sensor_from_cache(sensor_id, redis_connection):
    return json.loads(await redis_connection.get(f'sensor_{sensor_id}'))