#!/usr/bin/python3
"""
unittest classes:
"""
import unittest

from models.base import Base


class TestBaseInitialization(unittest.TestCase):
    """Test for initialization of base class"""
    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_none_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        b1 = Base(15)
        self.assertEqual(12, Base(12).id)

    def test_public(self):
        b1 = Base(15)
        b1.id = 7
        self.assertEqual(7, b1.id)

    def test_string(self):
        b1 = Base("hello")
        self.assertEqual(b1.id, "hello")

    def test_bool(self):
        b1 = Base(True)
        self.assertEqual(b1.id, True)

    def test_list(self):
        b1 = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b1.id)

    def test_tuple_id(self):
        b1 = Base((1, 2))
        self.assertEqual((1, 2), b1.id)
