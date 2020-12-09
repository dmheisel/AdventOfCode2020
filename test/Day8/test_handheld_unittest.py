import unittest
from Day8.handheld_runner import *

test_boot_code = [('nop', 0), ('acc', 1), ('jmp', 4), ('acc', 3),
                  ('jmp', -3), ('acc', -99), ('acc', 1), ('jmp', -4), ('acc', 6)]


class ParserTests(unittest.TestCase):
    def test_parse(self):
        test_path = 'test/Day8/test_input.txt'
        output = parse_code(test_path)
        self.assertListEqual(output, test_boot_code)


class HandheldTests(unittest.TestCase):
    def setUp(self) -> None:
        self.handheld = Handheld(test_boot_code)

    def tearDown(self):
        del self.handheld

    def test_handheld_init(self):
        self.assertEqual(self.handheld.boot_code, test_boot_code)
        self.assertEqual(self.handheld.accumulator, 0)
        self.assertEqual(self.handheld.pointer, 0)
        self.assertListEqual(self.handheld.processed, list())

    def test_handheld_check_pointer(self):
        self.assertEqual(self.handheld.check_pointer(), True)
        self.handheld.pointer = 3
        self.handheld.processed.append(3)
        self.assertEqual(self.handheld.check_pointer(), False)

    def test_jump(self):
        test_jump = ('jmp', 4)
        self.handheld.process_step(*test_jump)
        self.assertEqual(self.handheld.pointer, 4)

    def test_acc(self):
        test_acc = ('acc', 2)
        self.handheld.process_step(*test_acc)
        self.assertEqual(self.handheld.pointer, 1)
        self.assertEqual(self.handheld.accumulator, 2)

    def test_nop(self):
        test_nop = ('nop', 5)
        self.handheld.process_step(*test_nop)
        self.assertEqual(self.handheld.pointer, 1)
        self.assertEqual(self.handheld.accumulator, 0)


if __name__ == "__main__":
    unittest.main()
