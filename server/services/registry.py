from server.services.users.manager import UserManager

class ServiceRegistry:
    def __init__(self, config, dispatcher):
        self.user_manager = UserManager(config, dispatcher)

    def start_services(self):
        self.user_manager.load_service()