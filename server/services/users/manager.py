from .repository import UserRepository

from config import ConfigLoader as Config

class UserManager:
    def __init__(self, config: Config):
        self._repo = UserRepository()