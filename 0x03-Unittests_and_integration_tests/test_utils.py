#!/usr/bin/env python3
"""Test access nested map"""
import unittest
import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """testing multiple method with single"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """the function to be tested """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
