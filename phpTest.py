#!/usr/bin/env python3
from __future__ import print_function
import os
import asyncio
import datetime
from multiprocessing import Pool
import urllib.request
import urllib.parse

# import await as await


# def f(x):
#     os.system("php test.php")
#     return x*x

@asyncio.coroutine
def display_date(loop):
    end_time = loop.time() + 1.0
    while True:
        pastebin_vars = {
                        "api_option": "paste",
                        "api_dev_key": "57fe1369d02477a235057557cbeabaa1",
                        "api_paste_code": "testing pastebin right now",
                        "api_paste_private": "0",
                        "api_paste_name": "testing.html",
                        "api_paste_expire_date": "10M",
                        "api_paste_format": "html5",
                        "api_paste_name": "title"
                        }
        # "api_paste_code": "<head>Testing</head>",
        response = urllib.request.urlopen('http://pastebin.com/api/api_post.php', urllib.parse.urlencode(pastebin_vars).encode(
            "utf-8"))
        url = response.read()
        print(url)
        # with urllib.request.urlopen("http://pastebin.com/api/api_post.php") as url:
        #     s = url.read()
        # I'm guessing this would output the html source code?

        # response = urllib.urlopen('http://pastebin.com/api/api_post.php', urllib.urlencode(pastebin_vars))
        # url = response.read()
        # print(url)
    #     os.system("php test.php")
    #     print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        for bar in asyncio.sleep(1):
            yield bar
    # yield from asyncio.sleep(1)

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