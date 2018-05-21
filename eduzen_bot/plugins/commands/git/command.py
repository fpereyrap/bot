"""
pull - update_repo
"""
import subprocess

import structlog
from telegram.ext.dispatcher import run_async
from auth.restricted import restricted

logger = structlog.get_logger(filename=__name__)


@run_async
@restricted
def update_repo(bot, update, args):
    logger.warn("Trying to update bot code")

    result = subprocess.run(
        ["git", "pull", "origin", "master"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    msg = "No paso naranja!"

    if result.returncode == 0:
        logger.warn("Code updated!")
        msg = result.stdout.decode('utf-8')
    elif result.returncode == 1:
        msg = result.stderr.decode('utf-8')

    update.message.reply_text(msg)
