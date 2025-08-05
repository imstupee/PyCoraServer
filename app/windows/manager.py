from app.custom.QMainWindow import QMainWindow_

class WindowManager:
    def __init__(self):
        self.windows = {}

    def open(self, window: QMainWindow_):
        if window.window_name not in [*self.windows]:
            self.windows[window.window_name] = window
            window.show()