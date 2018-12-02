import asyncio
import json
from connections.connections import connect_to_rabbitmq
from datetime import datetime
from settings import RABBITMQ_QUEUE_SENSOR
import random
from tests.test_data.sensors import sensors_id


def gen_data():
    data = {
        'id': sensors_id[random.randint(0, len(sensors_id) - 1)],
        'time': str(datetime.utcnow()),
        'data': random.randint(0, 1)
    }

    return data


async def init_connect():
    transport, protocol = await connect_to_rabbitmq()

    channel = await protocol.channel()

    await channel.queue_declare(queue_name=RABBITMQ_QUEUE_SENSOR)

    return transport, protocol, channel


async def send_message(channel):
    print('send_message')
    await channel.basic_publish(
        payload=json.dumps(gen_data()),
        exchange_name='',
        routing_key=RABBITMQ_QUEUE_SENSOR
    )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    transport, protocol, channel = loop.run_until_complete(init_connect())

    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.gather(*[send_message(channel) for i in range(50)]))
    finally:
        loop.run_until_complete(protocol.close())
        transport.close()
        loop.close()
