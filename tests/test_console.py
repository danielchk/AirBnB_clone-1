#!/usr/bin/python3
""" 
test console.py
"""

import models
import sys
import unittest
from io import StringIO
from console import HBNBCommand
from unittest.mock import create_autospec

class test_console(unittest.TestCase):
    """
    test for the console
    """"

    def test_quit(self):
        """
        test quit
        """
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF(self):
        """
        test EOF
        """
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def test_all(self):
        """
        test all
        """
        console = self.create()
        console.onecmd("all")
        self.assertTrue(isinstace(self.capt_out.getvalue(), str))

    def test_create(self):
        '''
            test create
        '''
        console = self.create()
        console.onecmd("create User")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))
