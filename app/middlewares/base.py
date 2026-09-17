from collections.abc import Awaitable, Callable

from telethon.events import NewMessage

Handler = Callable[[NewMessage.Event], Awaitable[None]]
Middleware = Callable[[NewMessage.Event], Awaitable[None]]


def with_middlewares(*middlewares: Middleware):
    def decorator(handler: Handler) -> Handler:
        async def wrapper(event: NewMessage.Event) -> None:
            for middleware in middlewares:
                await middleware(event)
            await handler(event)

        return wrapper

    return decorator
