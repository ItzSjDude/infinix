import re
import sys
from telethon import *
from pathlib import Path
from traceback import format_exc
from time import gmtime, strftime
from asyncio import create_subprocess_shell as asyncsubshell, subprocess as asyncsub
from os import remove
from traceback import format_exc
from ...core import * 
from ...database import *
from ...infxcl import *
from pathlib import Path
import re, time, math, friendly
import sys

defcmd= "\."
cmd1=pget("alpha", "cmdhandler")
cmd2=pget("beta", "cmdhandler")
cmd3=pget("gaama", "cmdhandler")
cmd4=pget("delta", "cmdhandler")
scmd1 = pget("alpha", "sudocmd")
scmd2 = pget("beta", "sudocmd")
scmd3 = pget("gaama", "sudocmd")
scmd4 = pget("delta", "sudocmd")

if cmd1:
   acmd = f"\{cmd1}"
else: 
   acmd = defcmd
if cmd2:
   bcmd = f"\{cmd2}"
else: 
   bcmd = defcmd
if cmd3:
   gcmd = f"\{cmd3}"
else: 
   gcmd = defcmd
if cmd4:
   dcmd = f"\{cmd4}"
else: 
   cmd = defcmd
 
defscmd = "\!" 

if scmd1: 
   sacmd = f"\{scmd1}"
else: 
   sacmd = defscmd
if scmd2:
   sbcmd = f"\{cmd2}"
else: 
   sbcmd = defscmd
if scmd3:
   sgcmd = f"\{scmd3}"
else:
   sgcmd = defscmd
if scmd4:
   sdcmd = f"\{scmd4}"
else:
   sdcmd = defscmd 


__st__= int(1277919761)
if pdb.Asudo is not None:
   Asudo=list(set(int(x) for x in (pdb.Asudo).split(" ")))
else: 
   Asudo=__st__
if pdb.Bsudo is not None: 
   Bsudo=list(set(int(x) for x in (pdb.Bsudo).split(" ")))
else: 
   Bsudo=__st__
if pdb.Gsudo is not None:
   Gsudo = list(set(int(x) for x in (pdb.Gsudo).split(" ")))
else: 
   Gsudo=__st__
if pdb.Dsudo is not None:
   Dsudo = list(set(int(x) for x in (pdb.Dsudo).split(" ")))
else: 
   Dsudo=__st__

def ItzSjDude(**args):
    from inspect import stack
    from infinix import pget
    _plug = "\!"
    args["func"] = lambda e: e.via_bot_id is None
    stk = stack()
    previous_stack_frame = stk[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    pattern = args.get("pattern", None)
    args.get('disable_edited', True)
    allow_sudo = args.get("allow_sudo", False)
    args.get('disable_edited', True)
    groups_only = args.get('groups_only', False)
    trigger_on_fwd = args.get('trigger_on_fwd', False)
    trigger_on_inline = args.get('trigger_on_inline', False)
    disable_errors = args.get("disable_errors", False)
    infx = args.get("infx", False)
    sudo = args.get("sudo", False)
    lol=True
    if infx: 
        args["incoming"] = True
        del args["infx"]  
    if sudo:
        del args["sudo"]
    else: 
        args["outgoing"] = True
    if pattern is not None:
        if infx:
            if pattern.startswith("^/"):
                infxtg = pattern.replace("^/", "\\/")
                args["pattern"] = re.compile(pikatg)
            elif pattern.startswith("\\#"):
                args["pattern"] = re.compile(pattern)
            else:
                args["pattern"] = re.compile(_plug + pattern)
                infxtg = _plug + pattern
            try:
                InfAsst[file_test].append(infxtg)
            except BaseException:
                InfAsst.update({file_test: [infxtg]})
        else: 
            dpt=gpt=bpt=apt= None;dspt=gspt=bspt=aspt= None 
            if pattern.startswith("\\#"):
                del args["pattern"]
                dpt=gpt=bpt=apt=re.compile(pattern) 
            if pattern.startswith("^."):
                del args["pattern"]
                infcmd = pattern.replace("^.", "")
                if bot: 
                    apt = re.compile(acmd + infcmd)
                    aspt = re.compile(sacmd + infcmd)
                if bot2:
                    bpt = re.compile(bcmd + infcmd) 
                    bspt = re.compile(sbcmd + infcmd)
                if bot3:
                    gpt = re.compile(gcmd + infcmd) 
                    gspt = re.compile(sgcmd + infcmd)
                if bot4:
                    dpt = re.compile(dcmd + infcmd) 
                    dspt = re.compile(sdcmd + infcmd) 
            else:
                del args["pattern"]
                if bot: 
                    apt = re.compile(acmd + pattern)
                    aspt = re.compile(sacmd + pattern)
                if bot2:
                    bpt = re.compile(bcmd + pattern) 
                    bspt = re.compile(sbcmd + pattern)
                if bot3:
                    gpt = re.compile(gcmd + pattern) 
                    gspt = re.compile(sgcmd + pattern)
                if bot4:
                    dpt = re.compile(dcmd + pattern) 
                    dspt = re.compile(sdcmd + pattern) 
    if "trigger_on_inline" in args:
        del args['trigger_on_inline']
    if "groups_only" in args:
        del args['groups_only']
    if "disable_errors" in args:
        del args['disable_errors']
    if "trigger_on_fwd" in args:
        del args['trigger_on_fwd']
    def decorator(func):
        async def wrapper(check):
            if pdb.Botlog_chat:
                send_to = pdb.Botlog_chat
            if not trigger_on_fwd and check.fwd_from:
                return
            if check.via_bot_id and not trigger_on_inline:
                return
            if disable_errors:
                return
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
                if not disable_errors:
                    from .wrappers import auto_var
                    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

                    text = "**Sorry, I encountered a error!**\n"
                    link = "[https://t.me/PikachuUserbotSupport](Pikabot Support Chat)"
                    text += "If you wanna you can report it"
                    text += f"- just forward this message to {link}.\n"
                    text += "I won't log anything except the fact of error and date\n"

                    ftext = "\nDisclaimer:\nThis file uploaded ONLY here, "
                    ftext += "we logged only fact of error and date, "
                    ftext += "we respect your privacy, "
                    ftext += "you may not report this error if you've "
                    ftext += "any confidential data here, no one will see your data "
                    ftext += "if you choose not to do so.\n\n"
                    ftext += "--------BEGIN PIKABOT TRACEBACK LOG--------"
                    ftext += "\nDate: " + date
                    ftext += "\nGroup ID: " + str(check.chat_id)
                    ftext += "\nSender ID: " + str(check.sender_id)
                    ftext += "\nClient Name: " + str(await auto_var(check)) 
                    ftext += "\n\nEvent Trigger:\n"
                    ftext += str(check.text)
                    ftext += "\n\nTraceback info:\n"
                    ftext += str(format_exc())
                    ftext += "\n\nError text:\n"
                    ftext += str(sys.exc_info()[1])
                    ftext += "\n\n--------END USERBOT TRACEBACK LOG--------"
                    command = "git log --pretty=format:\"%an: %s\" -5"
                    ftext += "\n\n\nLast 5 commits:\n"
                    result = str(friendly.explain_traceback())
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
                            "error.log",
                            caption=text,
                        )
                    remove("error.log")
        if bot:
            if not infx and not sudo:
                bot.add_event_handler(wrapper, events.NewMessage(**args, pattern=apt))
            if sudo:
                bot.add_event_handler(wrapper, events.NewMessage(**args, incoming=True, pattern=aspt, from_users=Asudo))
        if bot2:
            if not infx and not sudo:
                bot2.add_event_handler(wrapper, events.NewMessage(**args, pattern=bpt))
            if sudo:
                bot2.add_event_handler(wrapper, events.NewMessage(**args, incoming=True, pattern=bspt, from_users=Bsudo,))
        if bot3:
            if not infx and not sudo:
                bot3.add_event_handler(wrapper, events.NewMessage(**args, pattern=gpt))
            if sudo:
                bot3.add_event_handler(wrapper, events.NewMessage(**args, incoming=True, pattern=gspt, from_users=Gsudo))
        if bot4:
            if not infx and not sudo:
                bot4.add_event_handler(wrapper, events.NewMessage(**args, pattern=dpt))
            if sudo:
                bot4.add_event_handler(wrapper, events.NewMessage(**args, incoming=True, pattern=dspt, from_users=Dsudo))
        if tgbot:
            if infx:
                tgbot.add_event_handler(wrapper, events.NewMessage(**args))
        try:
            LOAD_PLUG[file_test].append(wrapper)
        except Exception:
            LOAD_PLUG.update({file_test: [wrapper]})
        return wrapper
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


class Loader():
    def __init__(self, func=None, **args):
        self.Var = Var
        if bot:
          bot.add_event_handler(func, events.NewMessage(**args))
        if bot2:
          bot2.add_event_handler(func, events.NewMessage(**args))
        if bot3:
          bot3.add_event_handler(func, events.NewMessage(**args))
        if bot4:
          bot4.add_event_handler(func, events.NewMessage(**args))
        
__all__=['ItzSjDude', 'time_formatter', 'get_readable_time', 'humanbytes', 'progress']
