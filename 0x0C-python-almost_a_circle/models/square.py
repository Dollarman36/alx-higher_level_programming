#!/usr/bin/python3

""" square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ __init__ function """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Square __str__ function """
        msg = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return msg.format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        setattr(self, "width", value)
        setattr(self, "height", value)

    def update(self, *args, **kwargs):
        """ Square update function """
        if args != ():
            to_upd = {
                0: 'id',
                1: 'size',
                2: 'x',
                3: 'y'
            }
            for i, arg in enumerate(args):
                setattr(self, to_upd[i], arg)
        else:
            for k in kwargs:
                setattr(self, k, kwargs[k])

    def to_dictionary(self):
        """ Square to_dictionary function """
        rep = {
            'id': 0,
            'size': 0,
            'x': 0,
            'y': 0
        }
        for k in rep:
            rep[k] = getattr(self, k)

        return rep
