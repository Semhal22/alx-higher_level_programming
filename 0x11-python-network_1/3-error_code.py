#!/usr/bin/python3
"""
Fetches data from specified url using urllib
Manages exceptions
"""
from urllib.request import Request, urlopen
import urllib
import sys
if __name__ == "__main__":
    req = Request(sys.argv[1])
    try:
        with urlopen(req) as response:
            res = response.read()
            print(res.decode())
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
