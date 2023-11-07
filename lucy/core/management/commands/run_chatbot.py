from django.core.management.base import BaseCommand
from lucy.core.tasks import run_telegram_bot_listener


class Command(BaseCommand):
    help = "Run the Telegram bot listener using a Celery worker"

    def handle(self, *args, **options):
        run_telegram_bot_listener.apply_async()
