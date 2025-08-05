import asyncio
import typing
from uuid import uuid4
from datetime import datetime

from server.models import User

class ClientSession:
    def __init__(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        self.id = uuid4()
        self.reader = reader
        self.writer = writer
        self.address = writer.get_extra_info("peername")
        self._profile: typing.Optional[User] = None
        self._authorized = False
        self.last_active = datetime.now()

    def set_auth(self, arg: bool):
        self._authorized = arg

    async def recieve(self):
        data = await self.reader.read(-1)
        self.last_active = datetime.now()
        return data.decode()

    async def send(self, response: str):
        self.writer.write(response.encode())
        await self.writer.drain()

    async def close(self):
        self.writer.close()
        await self.writer.wait_closed()

    def set_profile(self, profile):
        self._profile = profile