from telethon import TelegramClient
import asyncio
import os
import sys
from ..database import pdb, pset
from ..infxcl import *
from telethon import TelegramClient, events, custom
from telethon.sessions import StringSession
from telethon.errors.rpcerrorlist import *
from logging import getLogger
infxlog=infxlog=getLogger("Infinix Login")


# ----------------------------------Constants--------------------------------
_phone_ = "**Login Assistent** For {}\n\nEnter your Phone no. On which u want @PikachuUserbot 😛\nIf Indian No. **+91xxxxxxxxxx** else use **Country Code**"
_2vfa_ = "**Login Assistent** For {}\n\nSeems like u have **2-Step verification** On your Account. Enter Your Password"
_verif_ = "**Login Assistent** For {}\n\nPlease enter the verification code that you receive from Telegram\n**if your code is** 06969 **then enter** 0 6 9 6 9."
_code_ = "**Login Assistent** For {}\n\n**Invalid Code Received**. Please /start"
_logged_ = "Login Assistent** For {}\n\n {}:LOGGED IN\n\nwait for 1Min n then Do `.infx`"
# ----------------------------------Constants--------------------------------
 
def get_cl_name(_PiKa_):
    if _PiKa_ == "alpha":
        return "Mainclient"
    if _PiKa_ == "beta":
        return "Multiclient1"
    if _PiKa_ == "gaama":
        return "Multiclient2"
    if _PiKa_ == "delta":
        return "Multiclient3"

async def infx_login(_PiKa_):
    tgclient= tg_client = tgbot_client = tgbot
    _cn_=get_cl_name(_PiKa_)
    async with tgbot_client:
        me = await tgbot_client.get_me()
        infxlog.info(me.first_name)
        
        @tgclient.on(events.NewMessage())
        async def handler(tglogin):
            if not tglogin.is_private:
                return
            async with tg_client.conversation(tglogin.chat_id) as pikulogin:
                await pikulogin.send_message(_phone_.format(_cn_))
                infxget = pikulogin.wait_event(events.NewMessage(
                    chats=tglogin.chat_id
                ))
                infxres = await infxget
                phone = infxres.message.message.strip()
                infx_client = TelegramClient(
                    StringSession(),
                    api_id=pdb.Api_id,
                    api_hash=pdb.Api_hash
                )

                await infx_client.connect()
                senx=await infx_client.send_code_request(phone)
                infxlog.info(senx)
                await pikulogin.send_message(_verif_.format(_cn_))
                infxlog.info(
                    "{}: Please enter the verification code, by giving space. If your code is 6969 then Enter 6 9 6 9".format(_cn_))
                response = pikulogin.wait_event(events.NewMessage(
                    chats=tglogin.chat_id
                ))
                response = await response
                r_code = response.message.message.strip()
                _2vfa_code_ = None
                r_code = "".join(r_code.split(" "))
                try:
                    await infx_client.sign_in(phone, code=r_code, password=_2vfa_code_)
                    s_string = infx_client.session.save()
                    infx_me = await infx_client.get_me()
                    await pikulogin.send_message(_logged_.format(_cn_, infx_me.first_name))
                    infxlog.info(
                        f"Successfully Logged in as {infx_me.first_name}")
                    pset(f"{_PiKa_}", "session", s_string)
                except PhoneCodeInvalidError:
                    await pikulogin.send_message(_code_.format(_cn_,))
                    return
                except SessionPasswordNeededError:
                    infxlog.info(
                        "{}: 2-Step verification Protected Account, Enter Your Password".format(_cn_))
                    await pikulogin.send_message(_2vfa_.format(_cn_))
                    response = pikulogin.wait_event(events.NewMessage(
                        chats=tglogin.chat_id
                    ))
                    response = await response
                    _2vfa_code_ = response.message.message.strip()
                    await infx_client.sign_in(password=_2vfa_code_)
                    infx_me = await infx_client.get_me()
                    infxlog.info(
                        f"Successfully Logged in as {infx_me.first_name}")
                    s_string = infx_client.session.save()
                    await pikulogin.send_message(_logged_.format(_cn_, infx_me.first_name))
                    pset(f"{_PiKa_}", "session", s_string)
                    
        await tgclient.run_until_disconnected()

__all__ = ['infx_login']
