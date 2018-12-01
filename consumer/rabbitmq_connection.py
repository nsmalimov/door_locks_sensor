import aioamqp
from settings import RABBITMQ_PASSWORD, RABBITMQ_URL, RABBITMQ_PORT, RABBITMQ_USER


async def connect_to_rabbitmq():
    transport, protocol = await aioamqp.connect(
        port=RABBITMQ_PORT,
        host=RABBITMQ_URL,
        password=RABBITMQ_PASSWORD,
        login=RABBITMQ_USER
    )

    return transport, protocol
