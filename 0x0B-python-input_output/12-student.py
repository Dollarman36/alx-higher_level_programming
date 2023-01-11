#!/usr/bin/python3

""" student module """


class Student:
    """ Student class """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        s_dict = self.__dict__
        if type(attrs) is list and all([type(i) is str for i in attrs]):
            new_dict = {}
            for name in attrs:
                if name in s_dict:
                    new_dict[name] = s_dict[name]
            return new_dict

        return self.__dict__
