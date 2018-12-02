import json


async def get_user_by_sensor_id_from_cache(sensor_id, redis_connection):
    user_id = await redis_connection.get(f'relation_sensor_{sensor_id}')

    return await get_user_from_cache(user_id, redis_connection)


async def get_user_from_cache(user_id, redis_connection):
    return json.loads(await redis_connection.get(f'user_{user_id}'))


async def get_sensor_from_cache(sensor_id, redis_connection):
    return json.loads(await redis_connection.get(f'sensor_{sensor_id}'))


async def save_sensor_data_log(sensor_id, sensor_data_data, sensor_data_time, psql_connection):
    await psql_connection.execute('''
            INSERT INTO sensor_data_log(sensor_id, sensor_data_data, sensor_data_time) VALUES($1, $2, $3)
        ''', sensor_id, sensor_data_data, sensor_data_time)


async def save_notification_data_log(notification_type, locked, stable, sensor_id,
                                     user_id, notification_time, psql_connection):
    await psql_connection.execute('''
            INSERT INTO notification_log(notification_type, locked, stable, sensor_id, 
            user_id, notification_time) VALUES($1, $2, $3, $4, $5, $6, $7, $8)
        ''', notification_type, locked, stable, sensor_id, user_id, notification_time)
