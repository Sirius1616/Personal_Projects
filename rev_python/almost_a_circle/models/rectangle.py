#!/usr/bin/python3

from models.base import Base

"""Module containing the base class"""
class Rectangle(Base):
    """The rectangle class that shall inherit from the base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the class Rectangle that inherits from the Base init method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """The setter for the width property of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """The setter for the height property of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """The setter for x parameter of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        """The setter for x parameter of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        return self.__height * self.__width

    def display(self):
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            print(" "*self.__x + "#"*self.__width)
            

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """A function that updates the value of each attributes"""
        if args and args != None:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'height':
                    self.__height = value

                elif key == 'id':
                    self.id = value

                elif key == 'width':
                    self.__width = value

                elif key == 'x':
                    self.__x = value

                elif key == 'y':
                    self.__y = value

    def to_dictionary(self):
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
