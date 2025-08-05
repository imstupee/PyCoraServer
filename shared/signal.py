class Signal:
    def __init__(self):
        self.connected = []

    def connect(self, callback):
        self.connected.append(callback)

    def emit(self, *args, **kwargs):
        for callback in self.connected:
            callback(*args, **kwargs)