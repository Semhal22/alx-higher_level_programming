#!/usr/bin/python3
"""Sends a POST request to a url with a letter as a parameter"""
if __name__ == "__main__":
    import requests
    import sys
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    response = requests.post(url, data={'q': q})
    try:
        data = response.json()
        if data:
            value_id = data['id']
            name = data['name']
            print("[{}] {}".format(value_id, name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
