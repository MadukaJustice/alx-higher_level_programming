#!/usr/bin/python3
"""
    Sends a request to the URL and displays the body of the response
      * If the HTTP status code is greater than or equal to 400,
        print: Error code: followed by the value of the HTTP status code
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]

    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
