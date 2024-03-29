#!/usr/bin/python3
"""
Fetches data from specified url using urllib
"""
from urllib.request import Request, urlopen
import sys
if __name__ == "__main__":
    req = Request(sys.argv[1])
    with urlopen(req) as response:
        res = response.headers.get('X-Request-Id')
        print(res)
