#!/usr/bin/python3
"""
Fetches specific response header from URL passed
"""
import requests
import sys
if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    value = res.headers.get('X-Request-Id')
    print(value)
