from telethon import TelegramClient, events

from app.middlewares.base import with_middlewares
from app.middlewares.user_middleware import ensure_user


def register(client: TelegramClient) -> None:
    @client.on(events.NewMessage(pattern='/start'))
    @with_middlewares(ensure_user)
    async def handler(event: events.NewMessage.Event) -> None:
        await event.respond('خوش اومدی 👋')
