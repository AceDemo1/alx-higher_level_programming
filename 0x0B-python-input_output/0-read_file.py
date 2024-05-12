#!/usr/bin/python3
"""read file"""


def write_file(filename=""):
	"""define func"""

	with open(filename, "r") as f:
		print(f.read())
