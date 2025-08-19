from server.models import ClientSession

class Command:
    def meta(name: str, _type: str, permissions: list[str]):
        def decorator(cls: DefaultCommand):
            cls.name = name
            cls._type = _type
            cls.permissions = permissions
            return cls
        return decorator


class DefaultCommand:
    name: str
    permissions: list[str]
    _type: str

    def __init__(self):
        pass

    def validate_params(self, params: dict):
        pass

    def validate_permissions(self, session: ClientSession):
        pass

    def execute(self, session: ClientSession, params: dict):
        pass

@Command.meta("auth", None, ["*"])
class AuthenticationCommand(DefaultCommand):
    def __init__(self):
        super().__init__()