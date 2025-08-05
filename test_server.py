from server.server import CoraServer
from config import ConfigLoader
import asyncio

config = ConfigLoader()
config.load()
server = CoraServer(config)


async def main():
    asyncio.create_task(server._start())
    while True:
        pass

asyncio.run(main())