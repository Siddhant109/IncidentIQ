from .common import BaseEvent


class ServiceEvent(BaseEvent):

    service: str

    status: str

    latency_ms: int

    error_rate: float

    message: str