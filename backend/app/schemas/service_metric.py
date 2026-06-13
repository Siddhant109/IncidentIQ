from .common import BaseEvent


class ServiceMetric(BaseEvent):

    service: str

    cpu_usage: float

    memory_usage: float

    requests_per_minute: int

    latency_ms: int