#!/usr/bin/env python3
"""this module creates a test unit for accessing a nested map"""
from parameterized import parameterized
from typing import Dict, Tuple, Union
from unittest import TestCase
from unittest.mock import patch, Mock
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(TestCase):
    """this unit tests for a nested map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple[str],
                               expected: Union[Dict, int],) -> None:
        """Tests the output of a nested map."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
