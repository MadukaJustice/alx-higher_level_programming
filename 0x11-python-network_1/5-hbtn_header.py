#!/usr/bin/python3
"""
    Sends a request to the URL and displays the value of the
    variable 'X-Request-Id' in the response header
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
