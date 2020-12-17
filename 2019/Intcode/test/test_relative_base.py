import unittest
from Computer import *

class RelativeBaseTests(unittest.TestCase):
    def setUp(self):
        self.computer = Computer()

    def tearDown(self):
        del self.computer