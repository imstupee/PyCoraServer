
from app.custom.QMainWindow import QMainWindow_
from app.layouts.layout_MainWindow import Ui_MainWindow
from qasync import asyncSlot
import asyncio

class ServerMainWindow(QMainWindow_):
    window_name = "ServerMainWindow"
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)