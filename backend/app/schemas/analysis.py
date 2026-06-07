from .common import BaseEvent


class AIAnalysisEvent(BaseEvent):

    incident_id: str

    summary: str

    root_cause: str

    recovery_suggestion: str

    confidence: float