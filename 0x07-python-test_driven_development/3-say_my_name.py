#!/usr/bin/python3

"""3-say_my_name module

This module has only one function that prints
My name is <first name> <last name>


Example:

>>> say_my_name = __import__('3-say_my_name').say_my_name
>>> say_my_name("John", "Smith")
My name is John Smith

"""


def say_my_name(first_name, last_name=""):
    """say_my_name(first_name, last_name="")

    This function receives two string inputs, if not a TypeError exception
    is raised.
    """
    message = "My name is {} {}"

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(message.format(first_name, last_name))
