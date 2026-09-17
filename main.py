import asyncio

from app.bot import create_client, register_handlers
from app.config import settings
from app.db import init_db


async def main() -> None:
    await init_db()
    client = create_client()
    register_handlers(client)
    await client.start(phone=settings.phone)
    await client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())
