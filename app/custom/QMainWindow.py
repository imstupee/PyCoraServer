from PySide6.QtWidgets import QMainWindow

from app.interfaces import IAppContext

class QMainWindow_(QMainWindow):
    window_name: str
    context: IAppContext

    def set_context(self, context_: IAppContext):
        self.context = context_