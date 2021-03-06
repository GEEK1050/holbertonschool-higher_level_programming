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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """__init__: constructor"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """area: return area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter: return the perimeter of the rectangle"""
        if not self.__width or not self.__height:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        __str__: string representation of the instance
        """
        rect = ""
        if not self.__width or not self.__height:
            return rect
        for i in range(self.__height):
            for j in range(self.__width):
                rect += '#'
            rect += '\n'

        rect = rect[:-1]

        return rect

    def __repr__(self):
        """
        __repr__: string representation of the instance
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
        ___del__: destructor
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger_or_equal: return the biggest rectangle"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() < rect_2.area():
            return rect_2

        else:
            return rect_1
