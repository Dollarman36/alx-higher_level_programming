#!/usr/bin/python3

""" test_rectangle module """

import unittest
import os
from models.rectangle import Rectangle
from models.base import Base


class TestClassRectangle(unittest.TestCase):
    """ Testing class Rectangle """

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ tearDown method """
        pass

    def test_init(self):
        """ Testing the initialization of class Rectangle """

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r1 = Rectangle(2, 10)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_values(self):
        """ Testing value errors """
        self.assertRaises(ValueError, Rectangle, -10, 2)

    def test_types(self):
        """ Testing type errors """
        self.assertRaises(TypeError, Rectangle, 10, "2")
