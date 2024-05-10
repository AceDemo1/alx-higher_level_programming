#!/usr/bin/python3
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__heigth = height

    def area(self):

    def __str__(self):
        print("[Rectangle] self.__width/self.__height")

