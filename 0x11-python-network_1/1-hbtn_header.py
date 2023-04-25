#!/usr/bin/python3
"""
    Sends a request to the URL and displays the value of the
    'X-Request-Id' variable found in the header of the response.
"""
from sys import argv
import urllib.request


if __name__ == "__main__":
    url = argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.getheader('X-Request-Id'))
