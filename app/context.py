from app.windows.manager import WindowManager

class AppContext:
    def __init__(self, config, server_api):
        self.server_api = server_api
        self.window_manager = WindowManager()
        self.config = config