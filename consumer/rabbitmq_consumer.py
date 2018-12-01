import asyncio
from consumer.rabbitmq_connection import connect_to_rabbitmq
from settings import RABBITMQ_QUEUE_SENSOR
import time

async def do_work(envelope, body):
    print(body)

async def callback(channel, body, envelope, properties):
    asyncio.get_event_loop().create_task(do_work(envelope, body))

async def start_consumer():
    transport, protocol = await connect_to_rabbitmq()

    channel = await protocol.channel()

    await channel.queue_declare(queue_name=RABBITMQ_QUEUE_SENSOR)

    await channel.basic_consume(callback, queue_name=RABBITMQ_QUEUE_SENSOR, no_ack=True)

    print ('sensor consumer started')

    # проверить правильность асинхронности

    # отправить данные по урлу клиента

    # записать значения в базы


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_consumer())
    loop.run_forever()
    loop.close()
