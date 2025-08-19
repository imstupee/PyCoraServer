from server.services.roles.permissions import PermissionClass
from server.services.roles.role import Role


class RoleManager:
    def __init__(self):
        existing_roles: list[Role] = []

    def create_role(self, role_name: str, permissions: list[PermissionClass]):
        pass

    def remove_role(self, role_name: str):
        pass