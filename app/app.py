from .context import AppContext
from config import ConfigLoader

from server import CoraServer

from app.windows import ServerMainWindow

from shared.log_dispatcher import LogDispatcher

from PySide6.QtWidgets import QApplication

import qasync
import asyncio

class CoraServerApplication:
    def __init__(self, config: ConfigLoader = None):
        self.app = QApplication()
        self.log_dispatcher = LogDispatcher()
        self.server = CoraServer(config, self.log_dispatcher)
        self.app_context: AppContext = AppContext(config, self.server.get_proxy(), self.log_dispatcher)

        self.loop = qasync.QEventLoop(self.app)
        asyncio.set_event_loop(self.loop)

    async def run(self):
        window = ServerMainWindow()
        window.set_context(self.app_context)
        self.app_context.window_manager.open(window)

        with self.loop:
            self.loop.run_forever()