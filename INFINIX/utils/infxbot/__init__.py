from infxbot.core import gpcid, pdb
import os

#__________Clients___________
tgbot=bot4=bot3=bot2=bot=None

if pdb.Alpha:
    bot=gpcid("#cGJvdDE")
if pdb.Beta:
    bot2=gpcid("#cGJvdDI")
if pdb.Gaama:
    bot3=gpcid("#cGJvdDM")
if pdb.Delta:
    bot4=gpcid("#cGJvdDQ")
if pdb.Omega:
    tgbot=gpcid("#cHRnYm90")
#_____________________________
__all__ = ["tgbot", "bot4","bot3","bot2","bot"]