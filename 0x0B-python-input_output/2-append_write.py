#!/usr/bin/python3
"""
    Initialize Module
"""


def append_write(filename="", text=""):
    """
        Appends a string to a text file (UTF8) and returns num of
        characters written
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
