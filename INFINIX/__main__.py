#!/usr/bin/python3
from . import StartInfinix
import asyncio as _asyncio  

if __name__ == "__main__": 
    
    _loop = _asyncio.new_event_loop
    _asyncio.set_event_loop(loop)
    _asyncio.get_event_loop().run_until_complete(StartInfinix())
