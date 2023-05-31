"""Esse arquivo testa o arquivo main.py"""

import importlib  # for importing the main.py file
import io  # for capturing the output
import sys  # for restoring the stdout and removing the main module from the cache
import unittest  # for creating the test case
from unittest.mock import patch  # for mocking the input


class TestMain(unittest.TestCase):
    """Class for testing the main.py file"""

    def setUp(self):
        """Sets up the test environment by removing the main module from the cache"""
        super().setUp()
        sys.modules.pop("main", None)

    @patch("builtins.input", return_value="Alice")
    def test_prints_hello_name(self, _mock_input):
        """Tests if the main.py file prints the correct output"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Oi Alice!")

    @patch("builtins.input", return_value="Bernardo")
    def test_prints_hello_other_name(self, _mock_input):
        """Tests if the main.py file prints the correct output"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Oi Bernardo!")
