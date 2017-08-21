#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
from contextlib import contextmanager
import sys
import io
import unittest
from datetime import datetime
from console import HBNBCommand
import console
import json

CMD = HBNBCommand()

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr

    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class TestHBNBCommandDocs(unittest.TestCase):
    """Class for testing Console docs"""

    @classmethod
    def setUpClass(cls):
        print('\n.................................')
        print('..... Testing Documentation .....')
        print('.......  For the Console  .......')
        print('.................................')

    def test_doc_file(self):
        """file documentation present"""
        expected = '\nCommand interpreter for Holberton AirBnB project\n'
        actual = console.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """class documentation present"""
        expected = 'Command inerpreter class'
        actual = CMD.__doc__
        self.assertEqual(expected, actual)

class TestConsole(unittest.TestCase):
    """ Class for testing Console """
    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('........ Testing Console ........')
        print('.................................')

    def test_create(self):
        """ create """
        with captured_output() as (out, err):
            CMD.do_create('')
        output = out.getvalue().strip()
        self.assertEqual("** class name missing **", output)

        with captured_output() as (out, err):
            CMD.do_create("State name=\"California\"")
        state_id = out.getvalue().strip()
        with captured_output() as (out, err):
            CMD.do_show("State {}".format(state_id))
        output = out.getvalue().strip()
        self.assertIn(state_id, output)
        
        CMD.do_destroy("State {}".format(state_id))

    def test_destroy(self):
        """ destroy """
        with captured_output() as (out, err):
            CMD.do_create("State name=\"California\"")
        state_id = out.getvalue()
        CMD.do_destroy("State {}".format(state_id))
        with captured_output() as (out, err):
            CMD.do_show("State {}".format(state_id))
        self.assertEqual("** no instance found **\n", out.getvalue())
        

if __name__ == '__main__':
    unittest.main
