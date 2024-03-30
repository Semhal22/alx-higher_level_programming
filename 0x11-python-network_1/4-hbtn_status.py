#!/usr/bin/python3
"""
Fetches data from specified url using requests
"""
import requests
if __name__ == "__main__":
    res = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"	- type: {type(res.text)}")
    print(f"	- content: {res.text}")
