#!/usr/bin/python3
"""
    Takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8)
"""
from sys import argv
import urllib.request


if __name__ == "__main__":
    try:
        url = argv[1]
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
