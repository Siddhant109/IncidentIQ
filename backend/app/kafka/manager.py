from app.kafka.producer import (
    KafkaProducerManager
)


async def start_kafka():

    await KafkaProducerManager.start()


async def stop_kafka():

    await KafkaProducerManager.stop()