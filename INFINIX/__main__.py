#!/usr/bin/python3
from . import StartInfinix 
import sys
import asyncio as o

if __name__ == "__main__": 
    if sys.version_info < (3, 10):
        a = o.get_event_loop()
    else:
        try:
            a = o.get_running_loop()
        except RuntimeError:
            a = o.new_event_loop()

    o.set_event_loop(a)
    a.run_until_complete(StartInfinix())
   
