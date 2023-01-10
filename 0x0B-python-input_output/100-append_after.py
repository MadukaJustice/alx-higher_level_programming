#!/usr/bin/python3
"""
    Initialize Module
"""


def append_after(filename="", search_string="", new_string=""):
    """
        Inserts a line of text to a file after each line containing
        a specific string
    """

    with open(filename, mode="r+", encoding="utf-8") as f:
        new_lines = ""
        for line in f:
            new_lines += line
            if search_string in line:
                new_lines += new_string
        f.seek(0)
        f.write(new_lines)
