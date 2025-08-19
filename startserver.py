from server import CoraServer
from config.config import ConfigLoader as Config

import asyncio

config = Config()
config.load()
server = CoraServer(config)

if __name__ == "__main__":
    asyncio.run(server._start())