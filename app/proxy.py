from urllib.parse import urlparse

from app.config import settings

SCHEME_MAP = {'socks5': 2, 'socks4': 1, 'http': 3}


def get_telethon_proxy() -> tuple | None:
    if not settings.proxy:
        return None
    parsed = urlparse(settings.proxy)
    return (
        SCHEME_MAP.get(parsed.scheme, 2),
        parsed.hostname,
        parsed.port,
        True,
        parsed.username,
        parsed.password,
    )
