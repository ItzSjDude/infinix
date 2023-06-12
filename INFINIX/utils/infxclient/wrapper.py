from ...database import pget,pset,pdel,pdb
from ...infxcl import *
    
async def infxgvar(_infx_, value=None):
  __id__=await get_infx_id(_infx_)
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
async def infx_msg(_infx, text, _infx_=None, parse_mode=None, link_preview=None):
  try:
      parse_mode = parse_mode or "md"; link_preview = link_preview or False
      try: 
         _reply = await _infx.get_reply_message()
      except: 
         pass 
         _reply = False 
      if _infx_ is None:
          return await _infx.edit(text, parse_mode=parse_mode, link_preview=link_preview) 
      else:
          if _reply: 
              return await _reply.reply(text, parse_mode=parse_mode,link_preview=link_preview)
          if not _reply: 
              return await _infx.reply(text, parse_mode=parse_mode,link_preview=link_preview)
  except:
      pass
#©Infinix </Kang/Copy with Credits else u will be called ultra gey/> 
async def is_infxtg(_infx_=None):
  _infx = await _infx_.client.get_me()
  if _infx.id== tgbot.uid:
      return True

#©Infinix </Kang/Copy with Credits else u will be called ultra gey/>
async def get_infx_id(_infx):
  _infx_= await _infx.client.get_me() 
  return _infx_.id 

#©Infinix </Kang/Copy with Credits else u will be called ultra gey/>
async def get_infx_tg(_infx_): 
  tg_id = await get_infx_id(_infx_)
  cache=[]
  if bot:
     cache.append(bot.uid)
  if bot2:
     cache.append(bot2.uid)
  if bot3:
     cache.append(bot3.uid)
  if bot4:
     cache.append(bot4.uid)

  if _infx_.sender_id in cache and tg_id != tgbot.uid:
      return None 
  if not _infx_.sender_id in cache and tg_id != tgbot.uid: 
      return True 

  if tg_id == tgbot.uid: 
      return True 

async def infchvar(self,var,msgid):
  svar=await infxgvar(self,var)
  if not svar:
    entit = (await self.client.get_entity("@InfinixResources")).id 
    return await self.client.get_messages(entity=entit,ids=int(msgid))
  elif svar:
     entit = pdb.Botlog_chat
     return await self.client.get_messages(entity=entit,ids=int(svar))
  else: 
    return 

__all__=['infx_msg', 'is_infxtg', 'get_infx_tg', 'get_infx_id', 'infxgvar','infchvar']
