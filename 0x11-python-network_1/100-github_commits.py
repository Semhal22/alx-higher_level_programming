#!/usr/bin/python3
"""
List 10 commits of given repository and user using the GitHub API
"""
import requests
import sys
if __name__ == "__main__":
    repo, owner = sys.argv[1], sys.argv[2]
    headers = {'Accept': 'application/vnd.github+json'}
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    res = requests.get(url, headers=headers)
    res = res.json()

    for i in range(10):
        obj = res[i]
        tx = f"{obj.get('sha')}: {obj.get('commit').get('author').get('name')}"
        print(tx)
