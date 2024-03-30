#!/usr/bin/python3
"""
Send POST request with parameter
"""
import requests
import sys
if __name__ == "__main__":
    try:
        q = sys.argv[1]
    except IndexError:
        q = ""
    res = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        obj = res.json()
        if not obj:
            print("No result")
        else:
            print(f"[{obj['id']}] {obj['name']}")
    except ValueError:
        print("Not a valid JSON")
