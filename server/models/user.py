class User:
    username: str
    password: str
    _active: bool

class UserProfile:
    
    def to_dict(self):
        pass

    @classmethod
    def to_obj(cls, data):
        pass