#!/usr/bin/python3
"""
Send POST request with email to the URL passed
"""
import urllib
from urllib.request import Request, urlopen
import sys
if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    req = Request(sys.argv[1], data)
    with urlopen(req) as response:
        print(response.read().decode())
