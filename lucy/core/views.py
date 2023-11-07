from rest_framework.views import APIView
from rest_framework.response import Response

from .services import telegram
from .models import TelegramChannel


class TelegramStartView(APIView):
    def get(self, request, format=None):
        # TODO: improve filter based on is_active
        telegram_token = TelegramChannel.objects.filter(is_active=True).first().token

        telegram_bot = telegram.TelegramChannel(token=telegram_token)
        telegram_bot = telegram_bot.start()
        telegram_bot.run_polling()

        return Response({"message": "TelegramStart API"})
