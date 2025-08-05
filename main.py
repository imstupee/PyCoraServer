from app import CoraServerApplication
from config import ConfigLoader
import asyncio

if __name__ == '__main__':
    config = ConfigLoader()
    config.load()
    app = CoraServerApplication(config)
    asyncio.run(app.run())