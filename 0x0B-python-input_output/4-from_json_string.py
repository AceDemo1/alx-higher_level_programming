#!/usr/bin/python3
"""return obj from JSON string"""
import json


def from_json_string(my_obj):
    return json.load(my_obj)
