#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    new_entry = {key: value}
    a_dictionary.update(new_entry)

    return a_dictionary
