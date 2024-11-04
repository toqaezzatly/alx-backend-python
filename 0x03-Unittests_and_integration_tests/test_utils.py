#!/usr/bin/env python3
"""Test access nested map and get_json"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function."""
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the expected result."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that access_nested_map raises KeyError as expected."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """Test get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that utils.get_json returns the expected result."""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response  # Corrected assignment

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test the memoize decorator."""
    
    def test_memoize(self):
        """Test that the memoize decorator works as expected."""
        
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def _a_property(self):  # Separate method for memoization
                return self.a_method()

            @property
            def a_property(self):
                return self._a_property  # Return the memoized property
        
        test_instance = TestClass()  # Instantiate TestClass

        # Patch a_method
        with patch.object(test_instance, 'a_method', return_value=42) as mock_method:
            result1 = test_instance.a_property  # Access as property
            result2 = test_instance.a_property  # Access as property again

            self.assertEqual(result1, result2)
            mock_method.assert_called_once()  # Ensure a_method is called once


if __name__ == "__main__":
    unittest.main()
