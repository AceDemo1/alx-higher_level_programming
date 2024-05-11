#!/usr/bin/python3
"""MyInt is a rebel"""


class MyInt(int):
    def __ne__(self, i):
        """inverts ne"""
        return super().__eq__(i)

    def __eq__(self, i):
        """invert eq"""
        return super().__ne__(i)
