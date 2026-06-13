import asyncio

from .auth import AuthSimulator
from .payment import PaymentSimulator
from .analytics import AnalyticsSimulator
from .notification import NotificationSimulator
from .gateway import GatewaySimulator


class SimulatorManager:

    @staticmethod
    async def start():

        simulators = [
            AuthSimulator(),
            PaymentSimulator(),
            AnalyticsSimulator(),
            NotificationSimulator(),
            GatewaySimulator(),
        ]

        for simulator in simulators:

            asyncio.create_task(
                simulator.run()
            )