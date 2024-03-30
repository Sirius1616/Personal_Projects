#!/usr/bin/python3

from models.rectangle import Rectangle

"""A module been a sequel of the rectangle module"""


class Square(Rectangle):
    """A square that inherits all the attributes form the rectangl3e class 
    Args:
        size(int): the size of the square wich would be the same with the height and the width of the rectangle
        all other arguments hold their previous description"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} -{}".format(self.id, self.x, self.y, self.width)


    def update(self, *args, **kwargs):
        """A public method that updates the square object when there is such input attribute"""
        attribute = ['id', 'size', 'x', 'y']
        if args and args != None:
            for i, arg in enumerate(args):
                if i < len(attribute):
                    setattr(self, attribute[i], arg)

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)


    def to_dictionary(self):
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
