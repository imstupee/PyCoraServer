from PySide6.QtWidgets import QMainWindow, QListWidgetItem
from app.layouts.layout_MainWindow import Ui_MainWindow
from qasync import asyncSlot
import asyncio

class ServerMainWindow(QMainWindow):
    window_name = "ServerMainWindow"
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)