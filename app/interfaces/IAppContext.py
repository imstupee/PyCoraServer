from abc import ABC
from abc import abstractmethod

from server.proxy import ServerProxy
from app.windows.manager import WindowManager
from config import ConfigLoader as Config
from shared.log_dispatcher import LogDispatcher

class IAppContext(ABC):
    proxy: ServerProxy
    window_manager: WindowManager
    config: Config
    log_dispatcher: LogDispatcher