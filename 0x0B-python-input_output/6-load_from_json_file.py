#!/usr/bin/python3
"""load from json file"""
import json


def load_from_json_file(filename):
    """define func"""
    with open(filename, "r") as f:
        return json.loads(f.read())
