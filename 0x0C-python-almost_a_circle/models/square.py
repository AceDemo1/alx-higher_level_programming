#!/usr/bin/python3

from model.Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, v):
        self.width = v
        self.height = v

    def __str__(self):
    """overwrite str"""
        return f'[Square] ({self.id}) {self.x}{self.y} - {self.size}'

