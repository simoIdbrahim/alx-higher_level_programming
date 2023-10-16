#!/usr/bin/python3
"""Defines a base model class."""
import json


class Base:
    '''the class OOP content'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor function'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' json file dict '''
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        ''' rejson file as dict '''
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' save json file object to file '''
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        else:
            with open('{}.json'.format(cls.__name__), 'w') as file:
                file.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        ''' create a new class from the  '''
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            the_new = Rectangle(1, 1)
        elif cls is Square:
            the_new = Square(1)
        else:
            the_new = None
        the_new.update(**dictionary)
        return the_new

    @classmethod
    def load_from_file(cls):
        ''' load stirng from file'''
        import os
        file = '{}.json'.format(cls.__name__)
        if not os.path.isfile(file):
            return []
        else:
            with open(file, 'r') as json_file:
                return (cls.create(**data) for data in cls.
                        from_json_string(json_file.read()))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Write the CSV serialization of a list of objects to a file """
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                w = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    w.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Return a list of classes instantiated from a CSV file """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
