import unittest

from Source.task8.task8 import task8
from Tests.utility.input_output_utility import create_input_txt, read_output


class Task8Tests(unittest.TestCase):
    def test_case1(self):
        create_input_txt(['(())[]'])
        task8()
        res = read_output()
        self.assertEqual(0, res)

    def test_case2(self):
        create_input_txt(['[(])'])
        task8()
        res = read_output()
        self.assertEqual(2, res)

    def test_case3(self):
        create_input_txt(['((]]]'])
        task8()
        res = read_output()
        self.assertEqual(-1, res)

    def test_case4(self):
        create_input_txt(['((([[[)])])]'])
        task8()
        res = read_output()
        self.assertEqual(4, res)


if __name__ == '__main__':
    unittest.main()
