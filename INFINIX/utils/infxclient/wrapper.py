from var import Var
from ...core import pget
from ...clients import bot, bot2, bot3, bot4, tgbot
    
async def auto_var(_pika_, value=None):
  __id__=await get_pika_id(_pika_)
  a=None 
  if bot:
    i1 = bot.uid
  else:
    i1 = 1111
  if bot2:
    i2 = bot2.uid
  else:
    i2 = 1011
  if bot3:
    i3 = bot3.uid
  else:
    i3 = 1010
  if bot4 is not None:
    i4 = bot4.uid
  else:
    i4 = 1001

  if __id__==i1:
     a="alpha"
  if __id__==i2:
     a="beta"
  if __id__==i3:
     a="gaama" 
  if __id__==i4:
     a="delta"

  if value is not None: 
      return pget(a, value)
  else: 
      return a
async def pika_msg(_pika, text, _pika_=None, parse_mode=None, link_preview=None):
  parse_mode = parse_mode or "md"; link_preview = link_preview or False
  try: 
     _reply = await _pika.get_reply_message()
  except: 
     pass 
     _reply = False 
  if _pika_ is None: 
      return await _pika.edit(text, parse_mode=parse_mode, link_preview=link_preview) 
  else:
      if _reply: 
          return await _reply.reply(text, parse_mode=parse_mode,link_preview=link_preview)
      if not _reply: 
          return await _pika.reply(text, parse_mode=parse_mode,link_preview=link_preview)
#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/> 
async def is_pikatg(_pika_=None):
  _pika = await _pika_.client.get_me()
  if _pika.id== tgbot.uid:
      return True

#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/>
async def get_pika_id(_pika):
  _pika_= await _pika.client.get_me() 
  return _pika_.id 

#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/>
async def get_pika_tg(_pika_): 
  tg_id = await get_pika_id(_pika_)
  cache=[]
  if bot:
     cache.append(bot.uid)
  if bot2:
     cache.append(bot2.uid)
  if bot3:
     cache.append(bot3.uid)
  if bot4:
     cache.append(bot4.uid)

  if _pika_.sender_id in cache and tg_id != tgbot.uid:
      return None 
  if not _pika_.sender_id in cache and tg_id != tgbot.uid: 
      return True 

  if tg_id == tgbot.uid: 
      return True 

__all__=['pika_msg', 'is_pikatg', 'get_pika_tg', 'get_pika_id', 'auto_var']