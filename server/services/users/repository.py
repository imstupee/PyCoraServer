from typing import List
import os
import pickle

from server.models import User
from api.log_dispatcher import LogDispatcher

REPO_PATH = "data/users.pickle"

class UserRepository:
    def __init__(self, _dispatcher: LogDispatcher, _base_dir: str):
        self.users: List[User] = []
        self.dispatcher = _dispatcher
        self.user_file = os.path.join(_base_dir, REPO_PATH)

    async def _load(self):
        if os.path.exists(self.user_file):
            await self.dispatcher.info("User file, OK!")
            with open(self.user_file) as file:
                data = pickle.load(file)
                self.users = [User.to_obj(record) for record in data]
        else:
            self.dispatcher.info("User file not found. Creating empty!")
            self.__create_empty_file()

    def get_user_by_username(self):
        pass

    def check_user_by_username(self, username: str):
        if username in [user.name for user in self.users]:
            return True
        return False
    
    def add(self, user: User):
        self.users.append(user)

    async def _save(self):
        pass

    async def __create_empty_file(self):
        with open(self.user_file, 'wb') as file:
            exp_list = [user.to_dict() for user in self.users]
            pickle.dump(exp_list, file)