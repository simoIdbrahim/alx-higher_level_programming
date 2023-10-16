#!/usr/bin/python3
''' Defines a rectangle class '''
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' constructor function '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' multiply the width and the height '''
        return self.__width * self.__height

    def display(self):
        ''' loop from char string # '''
        print(
            '\n' * self.y +
            (' ' * self.x + '#' * self.width + '\n') * self.height, end=''
        )

    def __str__(self):
        ''' return the string info about the classs '''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id,
                   self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        ''' Update the attribute '''
        if args and len(args) != 0:
            ind = 0
            for arg in args:
                if arg is None:
                    return False
                if ind == 0:
                    self.id = arg
                elif ind == 1:
                    self.width = arg
                elif ind == 2:
                    self.height = arg
                elif ind == 3:
                    self.x = arg
                elif ind == 4:
                    self.y = arg
                ind += 1
        else:
            for key, val in kwargs.items():
                if key == 'id':
                    self.id = val
                elif key == 'width':
                    self.width = val
                elif key == 'height':
                    self.height = val
                elif key == 'x':
                    self.x = val
                elif key == 'y':
                    self.y = val

    def to_dictionary(self):
        ''' return the attribute of the Rectangle '''
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
        }
