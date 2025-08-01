from abc import ABC
from abc import abstractmethod

class IServer(ABC):
    
    @abstractmethod
    def _start():
        pass
    
    @abstractmethod
    def _stop():
        pass