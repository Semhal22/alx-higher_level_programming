#!/usr/bin/python3
"""
Fetches data from specified url using requests
Manages exceptions
"""
import requests
import sys
if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    code = res.status_code

    if code >= 400:
        print(f"Error code: {code}")
    else:
        print(res.text)
