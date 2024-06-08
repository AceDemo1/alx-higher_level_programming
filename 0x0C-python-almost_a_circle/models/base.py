#!/usr/bin/python3
"""create a Base class"""
import json


class Base:
    """define a class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON rep"""
        if not list_dictionaries:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write JSON str to a file"""
        i = f'{cls.__name__}.json'
        with open(i, 'w') as f:
            if not list_objs:
                f.write('[]')
            else:
                j = [i.to_dictionary() for i in list_objs]
                f.write(cls.to_json_string(j))

    @staticmethod
    def from_json_string(json_string):
        """returns list of JSON rep"""
        if not json_string:
            return '[]'
        else:
            return [json.loads(json_string)]

    @staticmethod
    def create(cls, **dictionary):
        """returns instance with all attr set"""
        if cls.__name__ == 'Rectangle':
            i = cls(1, 1)
        elif cls.__name__ == 'Square':
            i = cls(1)
        return i.update(**dictionary)
