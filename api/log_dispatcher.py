from core.signal import Signal

import asyncio
import inspect
from datetime import datetime

class LogDispatcher:
    def __init__(self):
        self.queue = asyncio.Queue()
        self.log_track = []
        self.is_running = True
        self.dispatch = Signal()

    async def handle(self):
        while self.is_running:
            self.dispatch.emit(await self.queue.get())
            await asyncio.sleep(0.5)

    async def info(self, message):
        module_name = (inspect.getmodule(inspect.getouterframes(inspect.currentframe())[0][1]).__name__).split('.')[-1]
        _message = f"({datetime.now().strftime('%H:%M:%S')}) <{module_name}> [INFO]" + " " + message
        await self.queue.put(_message)
    