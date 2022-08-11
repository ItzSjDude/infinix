from ..core import *
from ..utils import *
from .login import *
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
    
async def StartInfinix(): 
    from ..database import pdb
    _const = {}; _logstr_ = "__{}__: connected 🔥"; _logstr2_ = "__{}__: started login assistent, do /start at {}'s pm".format(_const, pdb.Bf_uname); import glob; path = './plugins/*.py'; _path = './infxbot/Assistant/plugins/*.py'; files = glob.glob(path); _files = glob.glob(_path)
    msg = "✘Infinix Booting Process Started ✘\n\n"
    msg+="✗Checking Tgbot Connectivity✗\n"
    await asyncio.sleep(2)
    msg+="**Status**: Connected ✅\n\n"
   
    inf_session()
    if len(infson)==1:
        infson.append("alpha")
    for sname in infson:
        client=inf_session(sname)
        try:
            await client.start()
            client.me = await client.get_me()
            client.infx_cmd = {}; infclts.append(client);
            client.uid = tutils.get_peer_id(client.me)
            infxlog.info(_logstr_.format(sname))
        except Exception as e:
            infxlog.info(_logstr2_.format(sname))
            await infx_login(sname)
    infclts.remove(tgbot)
    _loginfx = await tgbot.send_message(pdb.Botlog_chat, msg)
          
    if (len(infclts))==1:
        msg+="Single UserMode Detected"+"\n"+"**Status**: Connected ✅\n\n"
        await infx_msg(_loginfx, msg)
    else: 
        msg+="Multi UserMode Detected"+"\n"+f"**Status**: {len(infclts)} Accounts Connected ✅\n\n"
        await infx_msg(_loginfx, msg)

    from ..loader import load_infx 
    
    try: 
        msg += "Loading Plugins" + "\n"
        load_infx("ubplugs")
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
