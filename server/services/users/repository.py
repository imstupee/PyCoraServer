from typing import List
import os
import pickle

from server.models import User
from shared.log_dispatcher import LogDispatcher

from server.services.users.exceptions import UserAlreadyExists, UserDoesNotExist

REPO_PATH = "data/users.pickle"

class UserRepository:
    def __init__(self, _dispatcher: LogDispatcher, _base_dir: str):
        self.users: List[User] = []
        self.dispatcher = _dispatcher
        self.user_file = os.path.join(_base_dir, REPO_PATH)

    def _load(self):
        if os.path.exists(self.user_file):
            self.dispatcher.info_nowait("Loaded Users file!")
            with open(self.user_file) as file:
                data = pickle.load(file)
                self.users = [User.to_obj(record) for record in data]
        else:
            self.dispatcher.info_nowait("User file not found. Creating empty!")
            self.__create_empty_file()

    def get_user_by_username(self, username: str):
        requested = None

        for user in self.users:
            if user.name == username:
                requested = user

        if requested is None:
            raise UserDoesNotExist(username)
        
        return requested

    def check_user_by_username(self, username: str):
        if username in [user.name for user in self.users]:
            return True
        return False
    
    def add(self, user: User):
        self.users.append(user)

    def remove(self, user: User):
        index = self.users.index(User)
        del self.users[index]

    def _save(self):
        pass

    async def __create_empty_file(self):
        with open(self.user_file, 'wb') as file:
            exp_list = [user.to_dict() for user in self.users]
            pickle.dump(exp_list, file)