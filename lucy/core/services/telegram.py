import logging

import asyncio
import telegram

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

from .base import BaseChannel


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
            text=f"Hello {user.first_name}. I'm a bot, please talk to me!",
        )

    def start(self):
        start_handler = CommandHandler("start", self._start)
        self.application.add_handler(start_handler)
        self.application.run_polling()
