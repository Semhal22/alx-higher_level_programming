#!/usr/bin/python3
"""Fetches a url and displays value of a variable in the response header"""
if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        value = response.getheader('X-Request-Id')
        print(value)
