#!/usr/bin/python3
"""
    Initialize Module
"""
import json


def load_from_json_file(filename):
    """
        Creates an object from JSON file
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
