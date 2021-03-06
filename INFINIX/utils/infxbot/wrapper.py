from ...infxcl import *
from importlib.util import *
import os
from functools import wraps
TGBOT_USERS = set(
    int(x) for x in os.environ.get(
        "BOT_USERS",
        "779890498").split())
# ©Infinix


def infxtgbot(infx=None, silent=None):
    def decorator(func):
        @wraps(func)
        async def wrapper(event):
            _selfinfx = await tgbot.get_me()
            if "AdmOnly" in infx:
                _infx = await tgbot.get_permissions(int(event.chat_id), event.sender_id)
                if _infx.is_admin:
                    await func(event)
                if event.sender_id == bot.uid:
                    pass
                if not _infx.is_admin:
                    if silent is None:
                        await event.reply("You need to be admin to use this command")

            if "AmIAdm" in infx:

                _infx = await tgbot.get_permissions(int(event.chat_id), _selfinfx.id)
                if _infx.is_admin:
                    await func(event)
                else:
                    if silent is None:
                        await event.reply("I am not Admin Nibba😷")

            if "OwnSudo" in infx:
                tgbotusers = list(TGBOT_USERS)
                if event.sender_id == bot.uid or event.sender_id in tgbotusers:
                    await func(event)
                else:
                    if silent is None:
                        await event.reply("**Error**: You are not a Sudo User, Owner.")

            if "Owner" in infx:
                if event.sender_id == bot.uid:
                    await func(event)
                else:
                    if silent is None:
                        await event.reply("Only Owners can execute this Cmd")

            if "BotSudo" in infx:
                if event.sender_id in list(TGBOT_USERS):
                    await func(event)

        return wrapper

    return decorator
