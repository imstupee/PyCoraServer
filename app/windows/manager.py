from PySide6.QtWidgets import QMainWindow

class WindowManager:
    def __init__(self):
        self.windows = {}

    def open(self, window: QMainWindow):
        if window.window_name not in [*self.windows]:
            self.windows[window.window_name] = window
            window.show()