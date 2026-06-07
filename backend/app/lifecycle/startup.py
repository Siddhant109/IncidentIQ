from app.db import MongoManager
from app.kafka.manager import start_kafka


async def initialize_platform():

    await MongoManager.connect()

    await start_kafka()