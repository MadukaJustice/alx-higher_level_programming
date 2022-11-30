#!/usr/bin/python3

def uppercase(str):
    for c in str:
        checker = ord(c)
        if checker >= 97 and checker <= 122:
            c = chr(checker - 32)
        print('{}'.format(c), end='')
    print('')
