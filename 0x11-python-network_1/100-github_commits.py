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
    if (res.status_code == 200):
        res = res.json()
        for i in range(10):
            obj = res[i]
            author = obj.get('commit').get('author').get('name')
            tx = f"{obj.get('sha')}: {author}"
            print(tx)
