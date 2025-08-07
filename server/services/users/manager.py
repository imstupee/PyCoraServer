from server.services.users.repository import UserRepository

from config import ConfigLoader as Config

from server.models import User

class UserManager:
    def __init__(self, config: Config, dispatcher):
        self._repo = UserRepository(dispatcher)
        self._repo._load(config.BASE_DIR)

    def create_user(self, username: str, password: str):
        if self._repo.check_user_by_username(username):
            raise Exception # Replace with an actual exception in the future
        
        new_user = User(username, password)