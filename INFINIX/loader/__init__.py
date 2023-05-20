from telethon import *
from importlib.util import *
import logging,sys,glob   
from sys import modules
from ..infxcl import *
from ..utils import *
import INFINIX

from INFINIX.core import *
import INFINIX.utils as _utilz
from pathlib import Path
from logging import getLogger
logpl = getLogger("Plugins:")
logpa = getLogger("Assistant:")
bfiles=glob.glob("./plugins/*.py")
afiles=glob.glob("./assistant/plugins/*.py")

def load_infx(_infxmod=None):
    from pathlib import Path
    from ..database import pdb,pget,pset
    import plugins.__init__ as _Modules

    rx = "!"; alf=False 
    if _infxmod=="ubplugs":
       files=bfiles
       alf=True 
    if _infxmod=="astplugs":
       files=afiles

    for name in files:
       
        with open(name) as f:
            path1 = Path(f.name); shortname = path1.stem; flik=glk=nx=None
            blik=shortname.replace(".py", "")
            if alf:
                flik=f"plugins/{blik}.py"
                nx=f"plugins.{blik}"
                glk=True
            else: 
                flik=f"assistant/plugins/{blik}.py"
                nx=f"assistant.plugins.{blik}"
            spec = spec_from_file_location(nx,Path(flik))
            _infx = module_from_spec(spec)
            asst = module_from_spec(spec)
           
            if glk: 
                userbot = INFINIX; _infx.bot = bot; _infx.rx = rx; _infx.Infinix = Infinix; _infx.pdb = pdb; _infx.borg = client; _infx.logger = logging.getLogger(blik)
                modules["userbot"] = INFINIX; modules["userbot.utils"] = _utilz; spec.loader.exec_module(_infx); client.infx_cmd[blik] = _infx; modules["infinix"+blik] = _infx; logpl.info(f"🔥Imported {blik}")
            else: 
                userbot = INFINIX; asst.bot = client; asst.tgbot = tgbot; asst.rx = rx; asst.Infinix = Infinix; asst.pdb = pdb; asst.infxtgbot = infxtgbot; modules['Asst_modules'] = _Modules       
                infxast[_infxsst] = asst; modules["infinix"+_infxsst] = asst; tgbot.infxast[_infxsst] = asst; spec.loader.exec_module(asst); logpa.info("🔥Imported "+_infxsst)


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
