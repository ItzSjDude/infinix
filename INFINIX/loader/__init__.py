from telethon import *
from importlib.util import *
import logging
import sys    
from sys import modules
from ..infxcl import *
from ..utils import *
import INFINIX

from INFINIX.core import *
import INFINIX.utils as _utilz
from pathlib import Path as _asstpath
from logging import getLogger
logpl = getLogger("Plugins:")
logpa = getLogger("Assistant:")

def infx_assistant(_infxsst=None):
    rx = "!"
    import plugins.__init__ as _Modules
    asstpath = _asstpath(f"./infinix/Assistant/plugins/{_infxsst}.py")
    asstname = "infinix.Assistant.plugins.{}".format(_infxsst)
    spec = spec_from_file_location(asstname, asstpath)
    asst = module_from_spec(spec)
                               #____infinix__Assistant__Plugins__Loader____
    userbot = infinix; asst.bot = bot; asst.tgbot = tgbot; asst.rx = rx; asst.Infinix = Infinix; asst.pdb = pdb; asst.infxtgbot = infxtgbot; modules['Asst_modules'] = _Modules       
    infxast[_infxsst] = asst; modules["infinix"+_infxsst] = asst; tgbot.infxast[_infxsst] = asst; spec.loader.exec_module(asst); logpa.info("🔥Imported "+_infxsst)
           

def infx_plugins(_infxmod=None):
    from pathlib import Path
    from ..database import pdb,pget,pset
    for client in infclts:
        
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
      userbot = INFINIX; _infx.bot = client; _infx.rx = rx; _infx.Infinix = Infinix; _infx.pdb = pdb; _infx.borg = client; _infx.logger = logging.getLogger(_infxmod)
      modules["userbot"] = INFINIX; modules["userbot.utils"] = _utilz; spec.loader.exec_module(_infx); client.infx_cmd[_infxmod] = _infx; modules["infinix"+_infxmod] = _infx; logpl.info("🔥Imported "+_infxmod)

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
                for j in infclts: 
                    j.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"plugins.{shortname}"
            for j in infclts: 
                for i in reversed(range(len(j._event_builders))):
                    ev, cb = j._event_builders[i],
                    if cb.__module__ == name:
                        del j._event_builders[i]
    except BaseException:
        raise ValueError
