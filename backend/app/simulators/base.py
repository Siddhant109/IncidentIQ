import asyncio
import random

from app.kafka.producer import (
    KafkaProducerManager
)

from app.kafka.topics import KafkaTopics


class BaseSimulator:

    service_name = "unknown"

    async def emit_log(self):

        latency = random.randint(
            50,
            3000
        )

        status = random.choice(
            [
                "healthy",
                "healthy",
                "healthy",
                "error"
            ]
        )

        event = {
            "service": self.service_name,
            "status": status,
            "latency_ms": latency,
            "error_rate": round(
                random.random(),
                2
            ),
            "message": f"{self.service_name} event"
        }

        await KafkaProducerManager.publish(
            KafkaTopics.SERVICE_LOGS,
            event
        )

    async def emit_metric(self):

        metric = {
            "service": self.service_name,
            "cpu_usage": round(
                random.uniform(10, 90),
                2
            ),
            "memory_usage": round(
                random.uniform(20, 80),
                2
            ),
            "requests_per_minute":
            random.randint(50, 500),
            "latency_ms":
            random.randint(50, 3000),
        }

        await KafkaProducerManager.publish(
            KafkaTopics.SERVICE_METRICS,
            metric
        )

    async def run(self):

        while True:

            await self.emit_log()

            await self.emit_metric()

            await asyncio.sleep(2)