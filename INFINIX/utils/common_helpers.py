from ..infxcl import *
from ..database import pdb

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


__all__=['add_active_clients','inf_session']
