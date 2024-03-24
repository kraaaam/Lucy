import logging

import asyncio
import telegram

from telegram import Update
from telegram.ext import (
    filters,
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
)

from .base import BaseChannel
from ..services import telegram as telegram_service


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


class TelegramChannel(BaseChannel):
    def __init__(self, token: str):
        self.token = token
        self.application = ApplicationBuilder().token(self.token).build()
        # return application

    def send_message(self, message: str):
        raise NotImplementedError

    async def _start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Hello {user}. I'm a bot, please talk to me!",
        )

        # telegram_service.create_telegram_subscriber(
        #     chat_id=update.effective_chat.id,
        #     username=update.effective_user.username,
        #     first_name=update.effective_user.first_name,
        # )

    async def _echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text=update.message.text
        )

    def start(self):
        start_handler = CommandHandler("start", self._start)
        echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), self._echo)

        self.application.add_handler(start_handler)
        self.application.add_handler(echo_handler)
        self.application.run_polling()
