#!/usr/bin/python3
"""List 10 recent commits given the user and repository name"""
if __name__ == "__main__":
    import requests
    import sys
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    response = requests.get(url)
    data = response.json()
    for i in range(10):
        commit = data[i]['commit']
        sha = data[i]['sha']
        author = commit['author']['name']
        print('[{}] {}'.format(sha, author))
