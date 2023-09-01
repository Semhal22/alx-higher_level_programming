#!/usr/bin/python3
"""Fetches a url using the package requests"""
if __name__ == "__main__":
    import requests
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    body = response.content
    print('Body response:')
    print(f'\t- type: {type(body)}')
    print(f'\t- content: {body.decode("utf-8")}')
