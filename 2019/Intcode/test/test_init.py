import unittest
from Computer import *


class InitTests(unittest.TestCase):
    def setUp(self):
        self.computer = Computer()

    def tearDown(self):
        del self.computer

    def test_init_input(self):
        self.assertTrue(hasattr(self.computer, 'code_in'))
        self.assertEqual(self.computer.code_in, None)

    def test_init_int_code(self):
        self.assertTrue(hasattr(self.computer, 'int_code'))
        self.assertEqual(self.computer.int_code, None)

    def test_init_pointer(self):
        self.assertTrue(hasattr(self.computer, 'pointer'))
        self.assertEqual(self.computer.pointer, 0)

    def test_init_IO(self):
        self.assertTrue(hasattr(self.computer, "I"))
        self.assertTrue(hasattr(self.computer, "O"))
        self.assertEqual((self.computer.I, self.computer.O), (list(), list()))

    def test_init_ops(self):
        self.assertTrue(hasattr(self.computer, "ops"))
        self.assertEqual(list(self.computer.ops.keys()),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 99])

    def test_rel_base(self):
        self.assertTrue(hasattr(self.computer, 'relative_base'))
        self.assertEqual(self.computer.relative_base, 0)
