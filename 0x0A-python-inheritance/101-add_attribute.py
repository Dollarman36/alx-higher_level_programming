#!/usr/bin/python3

""" add_attribute module """


def add_attribute(obj, att_name, att_value):
    """ add_attribute function """

    if obj.__class__.__module__ == 'builtins':
        raise TypeError("can't add new attribute")
    elif hasattr(obj, "__slots__") and att_name not in obj.__slots__:
        raise TypeError("can't add new attribute")

    setattr(obj, att_name, att_value)
