from server.models import ClientSession

class SessionManager:
    sessions = {}
    def __init__(self):
        pass

    def register(self, reader, writer):
        session = ClientSession(reader, writer)
        self.sessions[session.id] = session
        return (session, session.id)

    def remove(self, id):
        pass