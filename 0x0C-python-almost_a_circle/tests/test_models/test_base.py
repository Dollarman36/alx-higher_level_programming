#!/usr/bin/python3

""" test_base module """

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ testing class Base """

    def setUp(self):
        """ setUp function """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ tearDown function """
        pass

    def test_init(self):
        """ testing initialization of class Base """

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)
