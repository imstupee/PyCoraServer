class UserManagerException(Exception):
    def __init__(self):
        super().__init__()

class UserCreateError(UserManagerException):
    def __init__(self, _cause: Exception):
        super().__init__(_cause)
    
    def __str__(self):
        return f"Cannot create User due to: \n\t {self.cause}"
    
class UserRemoveError(UserManagerException):
    def __init__(self, _cause: Exception):
        super().__init__(_cause)

    def __str__(self):
        return f"Cannot remove User due to: \n\t {self.cause}"

class UserAlreadyExists(UserManagerException):
    def __init__(self, _username: str):
        super().__init__()
        self.username = _username

    def __str__(self):
        return f"{self.username} already exists!"
    
class UserDoesNotExist(UserManagerException):
    def __init__(self, _username: str):
        super().__init__()
        self.username = _username

    def __str__(self):
        return f"{self.username} does not exist!"
    
class InvalidPassword(UserManagerException):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Password does not follow the requirements."

class InvalidUsername(UserManagerException):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "Username does not follow the requirements."