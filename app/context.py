from .windows.manager import WindowManager

class AppContext:
    def __init__(self):
        self.server_api = None
        self.window_manager = WindowManager()