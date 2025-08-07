from app.windows.manager import WindowManager
from api.log_dispatcher import LogDispatcher

class AppContext:
    def __init__(self, config, server_api, log_dispatcher):
        self.server_api = server_api
        self.window_manager = WindowManager()
        self.config = config
        self.log_dispatcher = log_dispatcher