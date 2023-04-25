#!/usr/bin/python3
"""
    Takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    u_name = argv[1]
    u_pwd = argv[2]
    url = 'https://api.github.com/user'

    req = requests.get(url, auth=HTTPBasicAuth(u_name, u_pwd))
    print(req.json().get('id'))
