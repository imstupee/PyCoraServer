from app.windows.manager import WindowManager
from shared.log_dispatcher import LogDispatcher
from app.interfaces import IAppContext

class AppContext(IAppContext):
    def __init__(self, config, server_api, log_dispatcher):
        self.server_api = server_api
        self.window_manager = WindowManager()
        self.config = config
        self.log_dispatcher = log_dispatcher