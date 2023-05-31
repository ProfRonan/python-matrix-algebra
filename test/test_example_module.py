"""Esse arquivo testa o arquivo example_module.py"""

import unittest  # for creating the test case
from example_module import soma, multiplicação


class TestExampleModule(unittest.TestCase):
    """Class for testing the example_module.py file"""

    def test_soma(self):
        """Tests if the addition function returns the correct value 5"""
        self.assertEqual(soma(2, 3), 5)

    def test_multiplicação(self):
        """Tests if the addition function returns the correct value 5"""
        self.assertEqual(multiplicação(2, 3), 6)
