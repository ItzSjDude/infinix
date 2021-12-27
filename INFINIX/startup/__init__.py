from ..core import *
from ..login import infx_login
from ..infxcl import *
from .logger import *
from sys import *
import asyncio, os
from telethon import *
from pathlib import Path
from logging import getLogger
from telethon.tl.types import *
import telethon.utils as tutils
from telethon.errors.rpcerrorlist import *
import time
infxlog = getLogger("Startup")

#________Clients_________
#________________________

async def StartInfinix(): 
    from ...database import pdb
    if not bot:
        infxlog.info(
           "**mainclient**: started login assistent, do /start at {}'s pm".format(pdb.Bf_uname))
        await infx_login("alpha")
    else:
        _const = {}; _logstr_ = "__{}__: connected 🔥"; _logstr2_ = "__{}__: started login assistent, do /start at {}'s pm".format(_const, pdb.Bf_uname); import glob; path = './plugins/*.py'; _path = './infxbot/Assistant/plugins/*.py'; files = glob.glob(path); _files = glob.glob(_path)
        await tgbot.start(); tgbot.me = await tgbot.get_me(); tgbot.infxAsst = {}; tgbot.uid = tutils.get_peer_id(tgbot.me); infxlog.info(_logstr_.format("tgbot")); msg = _logstr_.format("_tgbot_") + '\n\n'; _loginfx = await tgbot.send_message(pdb.Botlog_chat, msg)

        if pdb.Alpha:
            try:
                await bot.start(); bot.me = await bot.get_me(); bot.infx_cmd = {}; bot.uid = tutils.get_peer_id(bot.me); infxlog.info(_logstr_.format("mainclient")); msg += _logstr_.format("mainclient") + "\n\n"; await infx_msg(_loginfx, msg)
            except Exception as e:
                infxlog.info(str(e)); infxlog.info(_logstr2_.format("mainclient")); msg += _logstr2_.format("mainclient") + "\n\n"; await infx_msg(_loginfx, msg); await infx_login("alpha")

        if pdb.Beta:
            try:
                await bot2.start(); infxlog.info(_logstr_.format("multiclient1")); bot2.me = await bot2.get_me(); bot2.uid = tutils.get_peer_id(bot2.me); msg += _logstr_.format("multiclient1") + "\n\n"; await infx_msg(_loginfx, msg)
            except:
                infxlog.info(_logstr2_.format("multiclient1")); msg += _logstr2_.format("multiclient1") + "\n\n"; await infx_msg(_loginfx, msg); await infx_login("beta")

        if pdb.Gaama:
            try:
                await bot3.start(); infxlog.info(_logstr2_.format("multiclient2")); bot3.me = await bot3.get_me(); bot3.uid = tutils.get_peer_id(bot3.me); msg += _logstr_.format("multiclient2") + "\n\n"; await infx_msg(_loginfx, msg)
            except:
                infxlog.info(_logstr2_.format("multiclient2")); msg += _logstr2_.format("multiclient2") + "\n\n"; await infx_msg(_loginfx, msg); await infx_login("gaama")

        if pdb.Delta:
            try:
                await bot4.start(); infxlog.info(_logstr_.format("multiclient3")); bot4.me = await bot4.get_me(); bot4.uid = tutils.get_peer_id(bot4.me); msg += logstr_.format("multiclient3") + "\n\n"; await infx_msg(_loginfx, msg)
            except:
                infxlog.info(_logstr2_.format("multiclient3")); msg += _logstr2_.format("multiclient3") + "\n\n"; await infx_msg(_loginfx, msg); await infx_login("delta")

        def __load_plugs__():
            from ...loader import infx_plugins, infx_assistant
            if tgbot: 
                for name in files:
                    with open(name) as f:
                        path1 = Path(f.name); shortname = path1.stem
                        infx_plugins(shortname.replace(".py", ""))
            if pdb.Asstt: 
                for name in _files:
                    with open(name) as f:
                        _asstpath = Path(f.name); shortname = _asstpath.stem
                        infx_assistant(shortname.replace(".py", ""))

        try: 
            __load_plugs__()
        except Exception as e:
            infxlog.exception(e)
            msg += str(e) + "\n\n"; await infx_msg(_loginfx, msg)

        msg += "sucessfully loaded plugins\n\n" + "**infxbot started sucessfully**"; await infx_msg(_loginfx, msg)
       

    if len(argv) not in (1, 3, 4):
        if bot:
            await gpcid("#cGJvdDE").disconnect()
        if bot2:
            await gpcid("#cGJvdDI").disconnect()
        if bot3:
            await gpcid("#cGJvdDM").disconnect()
        if bot4:
            await gpcid("#cGJvdDQ").disconnect()
    else:
        if bot:
            await bot.run_until_disconnected()
        if bot2:
            await bot2.run_until_disconnected()
        if bot3:
            await bot3.run_until_disconnected()
        if bot4:
            await bot4.run_until_disconnected()

__all__=["StartInfinix"]
