import asyncio
import aiohttp
from connections.connections import connect_to_rabbitmq, connect_to_redis
from settings import RABBITMQ_QUEUE_SENSOR
import json
from processing_network.request_funcs import post
from domain.data_getter import get_sensor_from_cache, get_user_by_sensor_id_from_cache

def send_data_to_user(sensor_address, sensor_data, time, user_url):
    data = {
        'type': 'status_change',
        'locked': bool(sensor_data),
        'address': sensor_address,
        'time': time
    }

    # вроде бы эта библиотека умеет держать соединение и не обрывает его, ну по крайней мере умела
    # todo: проверить
    async with aiohttp.ClientSession() as session:
        _ = await post(session, user_url, data)
        # todo: обработка корректности отправки, переотправка в случае проблем


# todo: добавить close на коннекты при уничтожении объекта класса

class SensorConsumer():
    def __init__(self):
        self.rabbit_transport, self.rabbit_protocol, self.rabbit_channel = await connect_to_rabbitmq()

        self.redis_connection = await connect_to_redis()

    async def do_work(self, envelope, body):
        data = json.loads(body)
        sensor_id = data['id']

        sensor_from_cache = await get_sensor_from_cache(sensor_id, self.redis_connection)
        # TODO
        # если пустой идти в базу и актуализировать данные в кеше (потёрлись)

        user = await get_user_by_sensor_id_from_cache(sensor_id, self.redis_connection)

        send_data_to_user(sensor_from_cache['address'], data['data'], data['time'], user['url'])

    async def callback(self, channel, body, envelope, properties):
        asyncio.get_event_loop().create_task(self.do_work(envelope, body))


async def start_consumer():
    sc = SensorConsumer()

    await sc.rabbit_channel.queue_declare(queue_name=RABBITMQ_QUEUE_SENSOR)

    await sc.rabbit_channel.basic_consume(sc.callback, queue_name=RABBITMQ_QUEUE_SENSOR, no_ack=True)

    print('sensor consumer started')


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_consumer())
    loop.run_forever()
    loop.close()
