#!/usr/bin/python3
"""
0-rectangle
    Classes:
        * Rectangle
"""


class Rectangle:
    """
    Rectangle:
        methodes:
            * __init__
    """
    def __init__(self, width=0, height=0):
        """__init__: constructor"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width: retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width: set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """height: retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height: set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
