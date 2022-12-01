#!/usr/bin/python3

from sys import argv


def add_cli_args():
    argc = len(argv)
    i = 1
    sum = 0
    while i < argc:
        sum += int(argv[i])
        i += 1
    print(f"{sum}")


if __name__ == "__main__":
    add_cli_args()
