from telethon import *
from importlib.util import *
import logging
import sys    
from sys import modules
import INFINIX
from INFINIX import bot, tgbot, ItzSjDude
from INFINIX.core import pdb, pget
import INFINIX.utils as _utilz
from pathlib import Path as _asstpath
from logging import getLogger
logpl = getLogger("Plugins:")
logpa = getLogger("Assistant:")

def pika_assistant(_infxsst=None):
    rx = "!"
    import plugins.__init__ as _Modules
    asstpath = _asstpath(f"./infinix/Assistant/plugins/{_infxsst}.py")
    asstname = "infinix.Assistant.plugins.{}".format(_infxsst)
    spec = spec_from_file_location(asstname, asstpath)
    asst = module_from_spec(spec)
                               #____infinix__Assistant__Plugins__Loader____
    userbot = infinix; asst.bot = bot; asst.tgbot = tgbot; asst.Var = Var; asst.rx = rx; asst.ItzSjDude = ItzSjDude; asst.pdb = pdb; asst.infxtgbot = infxtgbot; modules['Asst_modules'] = _Modules       
    infxast[_infxsst] = asst; modules["infinix"+_infxsst] = asst; tgbot.infxast[_infxsst] = asst; spec.loader.exec_module(asst); logpa.info("🔥Imported "+_infxsst)
           

def pika_plugins(_infxmod=None):
    from pathlib import Path 
    _rx=pget("alpha", "cmdhandler")
    if _rx: 
        rx = _rx
    else: 
        rx = "."
    path = Path(f"plugins/{_infxmod}.py")
    name = "plugins.{}".format(_infxmod)
    spec = spec_from_file_location(name, path)
    _infx = module_from_spec(spec)
                                   #____infinix__Plugins__Loader____
    userbot = infinix; _infx.bot = bot; _infx.Var = Var; _infx.rx = rx; _infx.ItzSjDude = ItzSjDude; _infx.pdb = pdb; _infx.Config = Var; _infx.borg = bot; _infx.logger = logging.getLogger(_infxmod)
    modules["userbot"] = infinix; modules["userbot.utils"] = _utilz; spec.loader.exec_module(_infx); bot.infxcmd[_infxmod] = _infx; modules["infinix"+_infxmod] = _infx; logpl.info("🔥Imported "+_infxmod)

def load_ext_module(shortname):
    if shortname.endswith("_"):
        from pathlib import Path
        path = Path(f"plugins/{shortname}.py")
        name = "plugins.{}".format(shortname)
        spec = spec_from_file_location(name, path)
        mod = module_from_spec(spec)
        spec.loader.exec_module(mod)


def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                if bot is not None:
                    bot.remove_event_handler(i)
                if bot2 is not None:
                    bot2.remove_event_handler(i)
                if bot3 is not None:
                    bot3.remove_event_handler(i)
                if bot4 is not None:
                    bot4.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"plugins.{shortname}"
            if bot is not None:
                for i in reversed(range(len(bot._event_builders))):
                    ev, cb = bot._event_builders[i],
                    if cb.__module__ == name:
                        del bot._event_builders[i]
            if bot2 is not None:
                for i in reversed(range(len(bot2._event_builders))):
                    ev, cx = bot2._event_builders[i],
                    if cx.__module__ == name:
                        del bot2._event_builders[i]
            if bot3 is not None:
                for i in reversed(range(len(bot3._event_builders))):
                    ev, cy = bot3._event_builders[i],
                    if cy.__module__ == name:
                        del bot3._event_builders[i]
            if bot4 is not None:
                for i in reversed(range(len(bot4._event_builders))):
                    ev, cz = bot4._event_builders[i],
                    if cz.__module__ == name:
                        del bot4._event_builders[i]
    except BaseException:
        raise ValueError
