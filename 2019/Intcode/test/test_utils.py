import unittest
from utils import utils


class UtilsTest(unittest.TestCase):
    def test_parser(self):
        path = 'test/simple_test.txt'
        result = utils.parse_input(path)
        self.assertEqual(result, [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])

