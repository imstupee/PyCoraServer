from server.interfaces import IServer
from server.services import ServiceRegistry

class ServerProxy:
    def __init__(self, _server: IServer, _svc_reg: ServiceRegistry):
        self.server = _server
        self.svc_reg = _svc_reg

    async def start_server(self):
        await self.server._start()