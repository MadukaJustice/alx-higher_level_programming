#!/usr/bin/python3
"""
    Use Github API to list last 10 commits given a repo and owner name
"""
from sys import argv
import requests

if __name__ == "__main__":
    owner = argv[1]
    repo = argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            repo, owner)

    req = requests.get(url)
    commits = req.json()

    for commit in commits[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
