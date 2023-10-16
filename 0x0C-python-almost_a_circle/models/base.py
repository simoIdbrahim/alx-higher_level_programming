#!/usr/bin/python3
'''Module for base class'''
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
