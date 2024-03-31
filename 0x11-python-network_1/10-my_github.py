#!/usr/bin/python3
"""
Use GitHub API with github credentials to display id
"""
import requests
import sys
if __name__ == "__main__":
    username, passwrd = sys.argv[1], sys.argv[2]
    headers = {'Authorization': f'Bearer {passwrd}',
               'Accept': 'application/vnd.github+json'}
    res = requests.get(f"https://api.github.com/{username}", headers=headers)
    user = res.json()
    if (hasattr(user, 'id')):
        print("user['id']")
    else:
        print("None")
