#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
i = __import__("5-save_to_json_file").save_to_json_file
j = __import__("6-load_from_json_file").load_from_json_file
k = __import__("sys").argv
try:
    li = j("add_item.json")
except FileNotFoundError:
    li = []
li.extend(k[1:])
i(li, "add_item.json")
