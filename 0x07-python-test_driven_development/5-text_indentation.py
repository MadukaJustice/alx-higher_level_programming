#!/usr/bin/python3
"""
    Define test_indentation function
"""


def text_indentation(text):
    """
        Prints text, two new lines after these characters "?", ":", "."
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    br = False
    for i in text:
        if br is False:
            if i == ' ':
                continue
            else:
                br = True
        if br is True:
            if i == '?' or i == '.' or i == ':':
                print(i)
                print()
                br = False
            else:
                print(i, end="")
