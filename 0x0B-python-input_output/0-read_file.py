#!/usr/bin/python3
"""read file"""


def write_file(filename="", text=""):
	"""define func"""
	with open(filename, w) as f:
		print(f.read())
