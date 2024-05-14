#!/usr/bin/python3
"""Student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dict"""
        if attrs is not None:
            k = {}
            for i in attrs:
                if i in self.__dict__:
                    k[i] = self.__dict__[i]
            return k
        return self.__dict__
