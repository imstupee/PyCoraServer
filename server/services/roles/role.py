from server.services.roles.permissions import PermissionClass

class Role:
    id: str
    name: str
    permissions: list[PermissionClass]

    def __init__(self):
        pass

    def assign_permission(self):
        pass


    def get_name(self):
        return self.name

