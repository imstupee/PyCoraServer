from app import CoraServerApplication
from config import CoraConfig
import asyncio

if __name__ == '__main__':
    config = CoraConfig()
    app = CoraServerApplication()
    asyncio.run(app.run())