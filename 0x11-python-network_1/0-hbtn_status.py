#!/usr/bin/python3
"""
Fetches data from specified url using urllib
"""
from urllib.request import Request, urlopen
if __name__ == "__main__":
    req = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(req) as response:
        res = response.read()

    print("Body response:")
    print(f"    - type: {type(res)}")
    print(f"    - content: {res}")
    print(f"    - utf8 content: {res.decode()}")
