#!/usr/bin/python3
from sys import exc_info, stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (IndexError, TypeError, ValueError, ZeroDivisionError):
        print("Exception: {}".format(exc_info()[1]), file=stderr)
        return None
