from server.services.users.manager import UserManager

class ServiceRegistry:
    def __init__(self, config):
        self.user_manager = UserManager(config)