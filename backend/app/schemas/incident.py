from pydantic import BaseModel

from .common import BaseEvent


class IncidentEvent(BaseEvent):

    service: str

    severity: str

    description: str

    latency_ms: int | None = None

    status: str