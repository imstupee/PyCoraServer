from server.services.users.repository import UserRepository
from server.models import User

from server.services.users.exceptions import UserCreateError, UserAlreadyExists

from config import ConfigLoader as Config

class UserManager:
    def __init__(self, config: Config, dispatcher):
        self._repo = UserRepository(dispatcher, config.BASE_DIR)

    def load_service(self):
        self._repo._load()

    def create_user(self, username: str, password: str):
        if self._repo.check_user_by_username(username):
            raise UserCreateError(_cause=UserAlreadyExists(username)) # Replace with an actual exception in the future
        
        new_user = User(username, password)

        # Add password validation
        # Add username validation
    
        self._repo.add(new_user)

    def remove_user(self, username: str):
        user = self._repo.get_user_by_username(username)

        if user is None:
            raise