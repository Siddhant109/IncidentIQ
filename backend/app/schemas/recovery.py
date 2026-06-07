from .common import BaseEvent


class RecoveryEvent(BaseEvent):

    service: str

    action: str

    status: str