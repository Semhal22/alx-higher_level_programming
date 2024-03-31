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
    url = f"https://api.github.com/users/{username}"
    res = requests.get(url, headers=headers)
    user = res.json()
    print(user.get('id'))
