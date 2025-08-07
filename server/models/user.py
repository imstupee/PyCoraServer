class User:
    username: str
    password: str
    _active: bool

    def __init__(self, _username: str, _password: str):
        self.username = _username
        self.password = _password
    
    def to_dict(self):
        return {
            "username": self.username,
            "h_password": self.password,
            "active": self._active
        }

    @classmethod
    def to_obj(cls, data: dict):
        cls.username = data.get("username")
        cls.password = data.get("h_password")
        cls._active = data.get("active")
        return cls