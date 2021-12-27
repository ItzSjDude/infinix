#!/usr/bin/env python3
#
# Copyright (C) 2020 by ItzSjDude@Github, < https://github.com/ItzSjDude/PikachuUserbot >.
#
# This file is part of < https://github.com/ItzSjDude/PikachuUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# 
# Please see < https://github.com/ItzSjDude/PikachuUserbot/blob/master/LICENSE >
#
# All rights reserved 

import os, sys;from logging import basicConfig, getLogger, INFO, ERROR, DEBUG;from distutils.util import strtobool as sb
_debug = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

if _debug:
  _level = DEBUG
else:
  _level = INFO 

basicConfig(format="◆━%(name)s━◆ ◉━%(levelname)s━◉  ⎝✧%(message)s✧⎠",level=_level,)
getLogger("telethon.statecache").setLevel(ERROR)
getLogger("telethon.network.mtprotosender").setLevel(ERROR)
getLogger("telethon.statecache").setLevel(ERROR)
getLogger("telethon.client.users").setLevel(ERROR)
getLogger("telethon.client.downloads").setLevel(ERROR)
getLogger("telethon.client.telegrambaseclient").setLevel(ERROR)
getLogger("telethon.network.mtprotosender").setLevel(ERROR)
