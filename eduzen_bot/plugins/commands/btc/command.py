"""
btc - btc
"""
import structlog
from telegram import ChatAction
from telegram.ext.dispatcher import run_async

from api import get_btc

logger = structlog.get_logger()


@run_async
def btc(update, context, *args, **kwargs):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    logger.info(f"Btc... by {update.message.from_user.name}")

    text = get_btc()

    context.bot.send_message(chat_id=update.message.chat_id, text=text)
