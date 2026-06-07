import json

from aiokafka import AIOKafkaProducer

from app.config import settings


class KafkaProducerManager:

    producer = None

    @classmethod
    async def start(cls):

        cls.producer = AIOKafkaProducer(
            bootstrap_servers=
            settings.KAFKA_BOOTSTRAP_SERVERS
        )

        await cls.producer.start()

    @classmethod
    async def stop(cls):

        if cls.producer:
            await cls.producer.stop()

    @classmethod
    async def publish(
        cls,
        topic: str,
        payload: dict
    ):

        await cls.producer.send_and_wait(
            topic,
            json.dumps(payload).encode()
        )