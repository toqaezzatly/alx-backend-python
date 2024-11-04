#!/usr/bin/env python3
"""Test access nested map"""
import unittest
import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):

    def test_access_nested_map1(self):
        nested_map = {"a": 1}
        path = ('a', )
        excepted = 1

        self.assertEqual(access_nested_map(nested_map, path),excepted)

    def test_access_nested_map2(self):
        nested_map = {"a": {"b": 2}}
        path = ('a', )
        excepted = {"b": 2}

        self.assertEqual(access_nested_map(nested_map, path),excepted)



if __name__ == "__main__":
    unittest.main()