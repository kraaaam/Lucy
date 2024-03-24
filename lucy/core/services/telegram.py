from asgiref.sync import sync_to_async

from ..models import TelegramSubscriber


@sync_to_async
def create_telegram_subscriber(*, chat_id: str, username: str, first_name: str):
    return TelegramSubscriber.objects.get_or_create(
        chat_id=chat_id, defaults={"username": username, "first_name": first_name}
    )
