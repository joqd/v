import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    api_id: int = int(os.getenv('API_ID', '0'))
    api_hash: str = os.getenv('API_HASH', '')
    phone: str = os.getenv('PHONE', '')
    database_url: str = os.getenv('DATABASE_URL', 'sqlite+aiosqlite:///db.sqlite3')
    proxy: str | None = os.getenv('PROXY')


settings = Settings()
