#!/usr/bin/python3
import hidden_4


def discovr():
    names = dir(hidden_4)
    for name in names:
        if name[:2] != '__':
            print("{:s}".format(name))


if __name__ == "__main__":
    discovr()
