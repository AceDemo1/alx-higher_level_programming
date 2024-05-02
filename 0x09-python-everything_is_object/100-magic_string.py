#!/usr/bin/python3
def magic_string():
    count = [0]
    return lambda: ", ".join(["BestSchool"] * (count[0] := count[0] + 1))

