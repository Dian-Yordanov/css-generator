#!/usr/bin/env python3
from __future__ import print_function
import os
import asyncio
import datetime
from multiprocessing import Pool

# import await as await


# def f(x):
#     os.system("php test.php")
#     return x*x

@asyncio.coroutine
def display_date(loop):
    end_time = loop.time() + 5.0
    while True:
        os.system("php test.php")
        # print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        yield from asyncio.sleep(1)

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(display_date(loop))
    loop.close()

    # callback = ""
    # pool = Pool(processes=1)  # Start a worker processes.
    # result = pool.apply_async(f, [10], callback)  # Evaluate "f(10)" asynchronously calling callback when finished.

if __name__ == '__main__':
    main()






# Blocking call which returns when the display_date() coroutine is done


# asyncio.async
# def display_date(loop):
#     end_time = loop.time() + 5.0
#     while True:
#         print(datetime.datetime.now())
#         if (loop.time() + 1.0) >= end_time:
#             break
#         await asyncio.sleep(1)
#
#
# loop = asyncio.get_event_loop()
# # Blocking call which returns when the display_date() coroutine is done
# loop.run_until_complete(display_date(loop))
# loop.close()