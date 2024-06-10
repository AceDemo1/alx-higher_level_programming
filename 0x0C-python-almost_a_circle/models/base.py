#!/usr/bin/python3
"""create a Base class"""
import json
import os
import csv


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
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns instance with all attr set"""
        if cls.__name__ == 'Rectangle':
            i = cls(1, 1)
        elif cls.__name__ == 'Square':
            i = cls(1)
        i.update(**dictionary)
        return i

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        i = f'{cls.__name__}.json'
        if not os.path.isfile(i):
            return []
        with open(i, 'r') as f:
            j = f.read()
            k = cls.from_json_string(j)
            return [cls.create(**li) for li in k]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        i = f'{cls.__name__}.csv'
        with open(i, 'w', newline='') as f:
            w = csv.writer(f)
            if cls.__name__ == 'Rectangle':
                w.writerow(['id', 'width', 'height', 'x', 'y'])
                for i in list_objs:
                    w.writerow([i.id, i.width, i.height, i.x, i.y])
            elif cls.__name__ == 'Square':
                w.writerow(['id', 'size', 'x', 'y'])
                for i in list_objs:
                    w.writerow([i.id, i.size, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserialize in CSV"""
        i = f'{cls.__name__}.csv'
        if not os.path.isfile(i):
            return []
        with open(i, 'r', newline='') as f:
            r = csv.reader(f)
            h = next(r)
            ins = []
            for row in r:
                if cls.__name__ == 'Rectangle':
                    id, width, height, x, y = map(int, row)
                    ins_ = cls(1, 1)
                    ins_.update(id=id, width=width, height=height, x=x, y=y)
                elif cls.__name__ == 'Square':
                    id, size, x, y = map(int, row)
                    ins_ = cls(1)
                    ins_.update(id=id, size=size, x=x, y=y)
                ins.append(ins_)
            return ins
