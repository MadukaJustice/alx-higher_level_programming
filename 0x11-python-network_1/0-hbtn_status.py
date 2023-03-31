#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """


import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        res = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print("\t- content: {}".format(res))
        print("\t- utf8 content: {}".format(res.decode('utf-8')))
