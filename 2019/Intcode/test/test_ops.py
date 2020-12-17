import unittest
from Computer import *


class OpCodeTests(unittest.TestCase):
    def setUp(self):
        self.computer = Computer()
        self.computer.mod = lambda i, v:  (i, v)

    def tearDown(self):
        del self.computer

    def test_add_op(self):
        result = self.computer.run_op(1, 3, 4, 5)
        self.assertEqual(result, (5, 7), 'Add op code should add two args')

    def test_mlt_op(self):
        result = self.computer.run_op(2, 3, 4, 5)
        self.assertEqual(
            result, (5, 12), 'MLT op code should multiply two args')

    def test_inp_op(self):
        self.computer.I = list([5])
        result = self.computer.run_op(3, 2)
        self.assertEqual(self.computer.I, list())
        self.assertEqual(result, (2, 5))

    def test_out_op(self):
        self.computer.run_op(4, 5)
        self.assertEqual(self.computer.O, [5])


class ModeTests(unittest.TestCase):
    def setUp(self):
        self.computer = Computer()
        self.computer.mod = lambda i, v:  (i, v)

    def tearDown(self):
        del self.computer


class RunOpCodeTests(unittest.TestCase):
    def setUp(self):
        self.test_input = ['1,9,10,3,2,3,11,0,99,30,40,50']
        self.computer = Computer(self.test_input)

    def tearDown(self):
        del self.test_input
        del self.computer

    def test_parse_code(self):
        code = self.computer.parse_code()
        self.assertEqual(code, 1)
        next_code = self.computer.parse_code()
        self.assertEqual(next_code, 9)

    def test_parse_code_params(self):
        self.computer.update_pointer()
        op, params = self.computer.parse_code_params(1)
        self.assertEqual((op, params), (1, [30, 40, 3]))
