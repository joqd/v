from telethon import TelegramClient

from app.config import settings
from app.handlers import ping, start
from app.proxy import get_telethon_proxy


def create_client() -> TelegramClient:
    return TelegramClient(
        'bot',
        settings.api_id,
        settings.api_hash,
        proxy=get_telethon_proxy(),
    )


def register_handlers(client: TelegramClient) -> None:
    ping.register(client)
    start.register(client)
