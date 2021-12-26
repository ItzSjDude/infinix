from . import infinix
import asyncio as _asyncio  

if __name__ == "__main__": 
    _asyncio.get_event_loop().run_until_complete(infinix())
