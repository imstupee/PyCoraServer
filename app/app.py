from .context import AppContext
from config import CoraConfig

from app.windows import ServerMainWindow

from PySide6.QtWidgets import QApplication

import qasync
import asyncio

class CoraServerApplication:
    def __init__(self, config: CoraConfig = None):
        self.app = QApplication()
        self.app_context: AppContext = AppContext()

        self.loop = qasync.QEventLoop(self.app)
        asyncio.set_event_loop(self.loop)

    async def run(self):
        window = ServerMainWindow()
        self.app_context.window_manager.open(window)

        with self.loop:
            self.loop.run_forever()