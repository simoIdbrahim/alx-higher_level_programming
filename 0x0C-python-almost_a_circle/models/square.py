#!/usr/bin/python3
''' Defines a Square class '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Square class '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' constructor function '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' return the string info about the classs '''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        ''' the size of the Square '''
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        ''' update the attribute using the unpaking (*args/**kwargs) '''
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        return
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        return
                    else:
                        self.id = val
                elif key == "size":
                    self.size = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def to_dictionary(self):
        ''' return the attribute of the Square '''
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y,
        }
