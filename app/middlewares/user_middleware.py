from sqlmodel import select
from telethon.events import NewMessage

from app.db import async_session
from app.models.user import User


async def ensure_user(event: NewMessage.Event) -> None:
    sender = await event.get_sender()
    if sender is None or getattr(sender, 'bot', False):
        return

    async with async_session() as session:
        result = await session.exec(select(User).where(User.telegram_id == sender.id))
        if result.first() is not None:
            return

        session.add(
            User(
                telegram_id=sender.id,
                username=sender.username,
                first_name=sender.first_name,
                last_name=sender.last_name,
            )
        )
        await session.commit()
