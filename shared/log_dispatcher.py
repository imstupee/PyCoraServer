from shared.signal import Signal

import asyncio
import inspect
from datetime import datetime


class LogDispatcher:
    queue = asyncio.Queue()
    log_track = []
    is_running = True
    dispatch = Signal()
    def __init__(self):
        pass

    async def handle(self):
        while self.is_running:
            self.dispatch.emit(await self.queue.get())
            await asyncio.sleep(0.5)

    async def info(self, message: str):
        module_name = (inspect.getmodule(inspect.getouterframes(inspect.currentframe())[0][1]).__name__).split('.')[-1]
        _message = f"({datetime.now().strftime('%H:%M:%S')}) <{module_name}> [INFO]" + " " + message
        await self.queue.put(_message)

    def info_nowait(self, message: str):
        #module_name = (inspect.getmodule(inspect.getouterframes(inspect.currentframe())[0][1]).__name__).split('.')[-1]
        _message = f"({datetime.now().strftime('%H:%M:%S')}) <Server> [INFO]" + " " + message
        self.queue.put_nowait(_message)