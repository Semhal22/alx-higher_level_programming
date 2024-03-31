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
        i = 0
        while (i < 10 and i < len(res)):
            obj = res[i]
            author = obj.get('commit').get('author').get('name')
            print(f"{obj.get('sha')}: {author}")
            i += 1
