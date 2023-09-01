#!/usr/bin/python3
"""Sends a request to a URL and displays body of the response"""
if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
