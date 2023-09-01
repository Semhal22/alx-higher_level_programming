#!/usr/bin/python3
"""Fetches a url and displays value of a variable in the response header"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    print(request_id)
