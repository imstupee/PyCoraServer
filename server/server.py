from core.interfaces import IServer

class CoraServer(IServer):
    def __init__(self):
        pass

    def _start(self):
        pass

    def _stop(self):
        pass

    def __wait_for_client(self):
        pass

    def __handle_unauthorized(self, client):
        pass

    def __handle_client(self, client):
        pass