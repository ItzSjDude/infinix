import re
import sys
from telethon import *
from pathlib import Path
from traceback import format_exc
from time import gmtime, strftime
import asyncio
from asyncio import create_subprocess_shell as asyncsubshell, subprocess as asyncsub
from os import remove
from traceback import format_exc
from logging import getLogger
from ...core import *
from ...database import *
from ...infxcl import *
from pathlib import Path
import re, time, math, friendly
import sys
infxlog = getLogger("Plugin Error?")
CMD_LIST = {};InfAsst = {};CMD_HELP = {};Pika_Cmd = {};INT_PLUG = "";LOAD_PLUG = {};COUNT_MSG = 0;USERS = {};COUNT_PM = {};LASTMSG = {};const = {};ISAFK = False;LASTMSG = {};ISAFK = False
infclts=[]
acmd=bcmd=ccmd=dcmd="\."
ocmd="\!"
sacmd=sbcmd=sccmd=sdcmd="\!" 
Asudo=Bsudo=Csudo=Dsudo=int(1277919761)

cmd1=pget("alpha", "cmd")
cmd2=pget("beta", "cmd")
cmd3=pget("gaama", "cmd")
cmd4=pget("delta", "cmd")
cmd5=pget("omega", "cmd") 
scmd1=pget("alpha", "scmd")
scmd2=pget("beta", "scmd")
scmd3=pget("gaama", "scmd")
scmd4=pget("delta", "scmd")

if cmd1: acmd=f"\{cmd1}"
if cmd2: bcmd=f"\{cmd2}"
if cmd3: ccmd=f"\{cmd3}"
if cmd4: dcmd=f"\{cmd4}"
if cmd5: ocmd=f"\{cmd5}"
if scmd1: sacmd=f"\{scmd1}"
if scmd2: sbcmd=f"\{scmd2}"
if scmd3: sccmd=f"\{scmd3}"
if scmd4: sdcmd=f"\{scmd4}"

if pdb.Asudo is not None: Asudo=list(set(int(x) for x in (pdb.Asudo).split(" ")))
if pdb.Bsudo is not None: Bsudo=list(set(int(x) for x in (pdb.Bsudo).split(" ")))
if pdb.Csudo is not None: Csudo=list(set(int(x) for x in (pdb.Csudo).split(" ")))
if pdb.Dsudo is not None: Dsudo=list(set(int(x) for x in (pdb.Dsudo).split(" ")))

def _compile(hndlr,ptrn):
  a=None
  if ptrn.startswith("^/"):
     a= re.compile(hndlr + ptrn.replace("^/", "\\/"),)
  elif ptrn.startswith("\\#"):
     a= re.compile(ptrn)
  elif ptrn.startswith("^."):
     a=re.compile(hndlr + ptrn.replace("^.", ""))
  else:
    a=re.compile(hndlr + ptrn)
  return a

smx=[Asudo,Bsudo,Csudo,Dsudo]

def Infinix(**args):
    from inspect import stack
    cmx=[];dmx=[]
    args["func"] = lambda e: e.via_bot_id is None
    file_test = Path((stack()[1]).filename).stem.replace(".py", "")
    allow_sudo = args.get("allow_sudo", False)
    pattern = args.get("pattern", False)
    args.get('disable_edited', True)
    groups_only = args.get('groups_only', False)
    trigger_on_fwd = args.get('trigger_on_fwd', False)
    trigger_on_inline = args.get('trigger_on_inline', False)
    sudo = args.get("sudo", False)
    tbot = args.get("tbot", False)
    alx=None
    if "trigger_on_inline" in args: del args['trigger_on_inline']
    if "groups_only" in args: del args['groups_only']
    if "trigger_on_fwd" in args: del args['trigger_on_fwd']
    if tbot: args["incoming"] = True; del args["tbot"]  
    if sudo: alx=True; del args["sudo"] 
    else: args["outgoing"] = True
    if pattern: 
        del args["pattern"]
        if bot: c1=_compile(acmd, pattern); sc1=_compile(sacmd, pattern); cmx.append(c1); dmx.append(sc1);
        if bot2: c2=_compile(bcmd, pattern); sc2=_compile(sbcmd, pattern); cmx.append(c2); dmx.append(sc2);
        if bot3: c3=_compile(ccmd, pattern); sc3=_compile(sccmd, pattern); cmx.append(c3); dmx.append(sc3);
        if bot4: c4=_compile(dcmd, pattern); sc4=_compile(sdcmd, pattern); cmx.append(c4); dmx.append(sc4);
        if tbot: c5=_compile(ocmd, pattern); 
    def decorator(func):
        async def wrap(check):
            if pdb.Botlog_chat: send_to = pdb.Botlog_chat
            if not trigger_on_fwd and check.fwd_from: return
            if check.via_bot_id and not trigger_on_inline: return
            if groups_only and not check.is_group:
                await check.respond("`I don't think this is a group.`")
                return
            try:
                await func(check)
            except events.StopPropagation:
                raise events.StopPropagation
            except KeyboardInterrupt:
                pass
            except BaseException as e:
                infxlog.exception(e)
                from .wrapper import infxgvar
                date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                text = "**Sorry, I encountered a error!**\n"
                text += "If you wanna you can report it"
                text += "I won't log anything except the fact of error and date\n"
                ftext = "\nDisclaimer:\nThis file uploaded ONLY here, "
                ftext += "we logged only fact of error aand date, "
                ftext += "we respect your privacy, "
                ftext += "you may not report this error if you've "
                ftext += "any confidential data here, no one will see your data "
                ftext += "if you choose not to do so.\n\n"
                ftext += "--------BEGIN PIKABOT TRACEBACK LOG--------"
                ftext += "\nDate: " + date
                ftext += "\nGroup ID: " + str(check.chat_id)
                ftext += "\nSender ID: " + str(check.sender_id)
                ftext += "\nClient Name: " + str(await infxgvar(check)) 
                ftext += "\n\nEvent Trigger:\n"
                ftext += str(check.text)
                ftext += "\n\nTraceback info:\n"
                ftext += str(format_exc())
                ftext += "\n\nError text:\n"
                ftext += str(sys.exc_info()[1])
                ftext += "\n\n--------END USERBOT TRACEBACK LOG--------"
                command = "git log --pretty=format:\"%an: %s\" -5"
                ftext += "\n\n\nLast 5 commits:\n"
                process = await asyncio.create_subprocess_shell(command,stdout=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.PIPE)
                stdout, stderr = await process.communicate()
                result = str(stdout.decode().strip()) + str(stderr.decode().strip()) 
                ftext += result
                file = open("error.log", "w+")
                file.write(ftext)
                file.close()
                if pdb.Botlog_chat:
                    await check.client.send_file(
                        send_to,
                        "error.log",
                        caption=text,
                    )
                else:
                    await check.client.send_file(
                        check.chat_id,
                        "error.txt",
                        caption=text,
                    )
                remove("error.log")

        if sudo:
            c=zip(infclts,dmx,smx)
            for i,j,k in c:
                i.add_event_handler(wrap, events.NewMessage(**args, incoming=True, pattern=j, from_users=k)) 
            dmx.clear() 
            smx.clear()
        elif not tbot and not sudo:
            d=zip(infclts,cmx)
            for i,j in d:
                i.add_event_handler(wrap, events.NewMessage(**args, pattern=j))
            cmx.clear()
        elif tbot: tgbot.add_event_handler(wrap, events.NewMessage(**args, pattern=c5))
        else:
          return None 
        try:
            LOAD_PLUG[file_test].append(wrap)
        except Exception:
            LOAD_PLUG.update({file_test: [wrap]})
        return wrap
    return decorator


async def progress(current, total, event, start, type_of_ps, file_name=None):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "[{0}{1}]\nProgress: {2}%\n".format(
            ''.join(["█" for i in range(math.floor(percentage / 5))]),
            ''.join(["░" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2))
        tmp = progress_str + \
            "{0} of {1}\nETA: {2}".format(
                humanbytes(current),
                humanbytes(total),
                time_formatter(estimated_total_time)
            )
        if file_name:
            await event.edit("{}\nFile Name: `{}`\n{}".format(
                type_of_ps, file_name, tmp))
        else:
            await event.edit("{}\n{}".format(type_of_ps, tmp))


def humanbytes(size):
    """Input size in bytes,
    outputs in a human readable format"""
    # https://stackoverflow.com/a/49361727/4723940
    if not size:
        return ""
    # 2 ** 10 = 1024
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time
    
def time_formatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " day(s), ") if days else "") + \
        ((str(hours) + " hour(s), ") if hours else "") + \
        ((str(minutes) + " minute(s), ") if minutes else "") + \
        ((str(seconds) + " second(s), ") if seconds else "") + \
        ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    return tmp[:-2]

__all__=['Infinix', 'time_formatter', 'get_readable_time', 'humanbytes', 'progress','infclts']
