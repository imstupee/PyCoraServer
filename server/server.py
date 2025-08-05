from server.interfaces import IServer
from config import ConfigLoader
from api import ServerAPI
from server.services import ServiceRegistry
from shared.utils import get_local_address
from server.models import ClientSession

import asyncio
import socket

class CoraServer(IServer):
    def __init__(self, config: ConfigLoader = None):
        self.svc_reg: ServiceRegistry = ServiceRegistry()
        self.config: ConfigLoader = config

        self.host = self.config.host if self.config.host != "local" else get_local_address()
        self.con_port = self.config.con_port
        self.bcast_port = self.config.bcast_port

        self.bcast_task = None

        self._running = False

    async def _start(self):
        self._running = True
        self.bcast_task = asyncio.create_task(self.__start_broadcast())
        self.async_server = await asyncio.start_server(self.__wait_for_connection, self.host, self.con_port)
        try:
            async with self.async_server:
                await self.async_server.serve_forever()
        except asyncio.CancelledError: # When server stops there is a cancel error
            pass

    async def _stop(self):
        self._running = False
        self.async_server.close()
        await self.async_server.wait_closed()

    async def __wait_for_connection(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        session = ClientSession(reader, writer)

        # session = client_manager.register(reader, writer)
        # if await aut_service.wait_for_auth(session)
        #   self.__handle_session(session)

        self.__handle_unauthorized(session)

    async def __handle_unauthorized(self, session: ClientSession):
        try:
            while self._running:
                try:
                    data = await asyncio.wait_for(session.recieve(), timeout=5.0)

                    if data:
                        pass # Send incoming request to RPC Handler
                        if session._authorized:
                            asyncio.create_task(self.__handle_session(session))
                            break
                    
                    else:
                        await session.close()
                        break

                except asyncio.TimeoutError:
                    await session.close()
                    break

                except Exception as exc:
                    await session.send(f"error?code={exc.code}&message={exc.message}")
                    await session.close()
            
            await session.close()

        except ConnectionError as con_err:
            pass

    async def __handle_session(self, session: ClientSession):
        while self._running:
            try:
                data = await session.recieve()
                if data:

                    pass # Send incoming request to RPC Handler

            except ConnectionError:
                await session.close()
            
            except Exception as exc:
                await session.send(f"error?code={exc.code}&message={exc.message}")
        
        await session.close() if session else None


    async def __start_broadcast(self):
        loop = asyncio.get_running_loop()
        bcast_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bcast_sock.bind((self.host, self.bcast_port))
        bcast_sock.setblocking(False)

        while self._running:
            inc_data, con_addr = await loop.sock_recvfrom(bcast_sock, 4096)
            if inc_data == b"discover":
                await loop.sock_sendto(bcast_sock, b"discover", con_addr)
        
        bcast_sock.close()

    def get_api(self):
        return ServerAPI(self, self.svc_reg)