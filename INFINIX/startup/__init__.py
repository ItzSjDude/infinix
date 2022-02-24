from ..core import *
from ..utils import infx_msg,infclts
from .login import infx_login
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
infson=[]
def add_active_clts():
    if bot: infclts.append(bot)
    if bot2: infclts.append(bot2)
    if bot3: infclts.append(bot3)
    if bot4: infclts.append(bot4)

def inf_session(name=None):
    from ..database import pdb
    if name: 
        if name=="omega": return tgbot
        if name=="alpha": return bot
        if name=="beta": return bot2
        if name=="gama": return bot3
        if name=="delta": return bot4
    else: 
        if pdb.Omega: infson.append("omega")
        if pdb.Alpha: infson.append("alpha") 
        if pdb.Beta: infson.append("beta") 
        if pdb.Gaama: infson.append("gaama") 
        if pdb.Delta: infson.append("delta") 
        
async def StartInfinix(): 
    from ..database import pdb
    _const = {}; _logstr_ = "__{}__: connected 🔥"; _logstr2_ = "__{}__: started login assistent, do /start at {}'s pm".format(_const, pdb.Bf_uname); import glob; path = './plugins/*.py'; _path = './infxbot/Assistant/plugins/*.py'; files = glob.glob(path); _files = glob.glob(_path)
    msg = "✘Infinix Booting Process Started ✘\n\n"
    msg+="✗Checking Tgbot Connectivity✗\n"
    await asyncio.sleep(2)
    msg+="**Status**: Connected ✅\n\n"
   
    inf_session()
    for sname in infson:
        client=inf_session(sname)
        try:
            await client.start()
            client.me = await client.get_me()
            client.infx_cmd = {}
            client.uid = tutils.get_peer_id(client.me)
            infxlog.info(_logstr_.format(sname))
        except Exception as e:
            infxlog.info(_logstr2_.format(sname))
            await infx_login(sname)
    _loginfx = await tgbot.send_message(pdb.Botlog_chat, msg)
            
    add_active_clts()
    if (len(infclts))==1:
        msg+="Single UserMode Detected"+"\n"+"**Status**: Connected ✅\n\n"
        await infx_msg(_loginfx, msg)
    else: 
        msg+="Multi UserMode Detected"+"\n"+f"**Status**: {len(infclts)} Accounts Connected ✅\n\n"
        await infx_msg(_loginfx, msg)

    def __load_plugs__():
        from ..loader import infx_plugins, infx_assistant
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
        msg += "Loading Plugins" + "\n"
        __load_plugs__()
        msg += "**Status**: Successfully Loaded\n\n"
        await infx_msg(_loginfx, msg)
    except Exception as e:
        infxlog.exception(e)
        msg += "Error While Loading\n\n"+ str(e) + "\n\n"; await infx_msg(_loginfx, msg)

    msg += "**✘Infinix Boot Process Finished✘**"+"\n\n"; await infx_msg(_loginfx, msg)
    msg += "__-Developed By ItzSjDude With ♥️__"; await infx_msg(_loginfx, msg)
       
    for aifc in infclts:  
        if len(argv) not in (1, 3, 4): await aifc.disconnect()  
        else: await aifc.run_until_disconnected()

__all__=["StartInfinix"]
