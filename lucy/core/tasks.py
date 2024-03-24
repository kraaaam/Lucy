from celery import shared_task
from django.conf import settings


from .channels import telegram
from .models import TelegramChannel as TelegramChannelModel


@shared_task
def run_telegram_bot_listener():

    telegram_token = TelegramChannelModel.objects.filter(is_active=True).first().token
    telegram_bot = telegram.TelegramChannel(token=telegram_token)
    telegram_bot = telegram_bot.start()
