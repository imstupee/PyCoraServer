from typing import List
import os
import pickle

from server.models import User

USER_FILE = "data/users.pickle"

class UserRepository:
    def __init__(self):
        self.users: List[User] = []

    def _load(self, base_dir: str):
        if os.path.exists(os.path.join(base_dir, USER_FILE)):
            print("User file, OK!")