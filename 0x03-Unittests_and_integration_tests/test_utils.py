#!usr/bin/env python3
"""Familiarize yourself with the utils.access_nested_map function and
understand its purpose. Play with it in the Python console to make sure
you understand.In this task you will write the first unit test for
utils.access_nested_map.
Create a TestAccessNestedMap class that inherits from unittest.TestCase.
Implement the TestAccessNestedMap.test_access_nested_map method to test
that the method returns what it is supposed to.
Decorate the method with @parameterized.expand to test the function for
following inputs:
nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
For each of these inputs, test with assertEqual that the function
returns the expected result.
"""
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""

    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """test_access_nested_map method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Dict,
        path: Tuple[str],
        expected: Exception,
    ) -> None:
        """test_access_nested_map_exception method"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)
