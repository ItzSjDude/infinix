#____ Client Ids _____
Id1="#cGJvdDE"
Id2="#cGJvdDI"
Id3="#cGJvdDM"
Id4="#cGJvdDQ"
Id5="#cHRnYm90"
#_____________________

from telethon import TelegramClient
from telethon.sessions import StringSession
from ..database import pdb
def InfxClient(session, gBot=None):
    if gBot:
        return TelegramClient(
            "TgBot",
            pdb.Api_id,
            pdb.Api_hash).start(
            bot_token=session)
    else:
        return TelegramClient(
            StringSession(session),
            pdb.Api_id,
            pdb.Api_hash,
            connection_retries=None,
            auto_reconnect=True,
            lang_code='en')

def gpcid(_id_):
    if _id_==Id1:
       return InfxClient(pdb.Alpha)
    if _id_==Id2:
       return InfxClient(pdb.Beta)
    if _id_==Id3:
       return InfxClient(pdb.Gaama)
    if _id_==Id4:
       return InfxClient(pdb.Delta)
    if _id_==Id5: 
       return InfxClient(pdb.Omega, gBot=True)

__all__ = ['gpcid']
