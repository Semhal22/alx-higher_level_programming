#!/usr/bin/python3
"""Take Github credentials and return user id"""
if __name__ == "__main__":
    import requests
    import sys
    username = sys.argv[1]
    pwd = sys.argv[2]
    response = \
        requests.get('https://api.github.com/user', auth=(username, pwd))
    data = response.json()
    print(data.get('id'))
