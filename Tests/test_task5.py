import unittest

from Source.task5.task5 import task5
from Tests.utility.input_output_utility import create_input_txt, read_output


class Task5Tests(unittest.TestCase):
    def test_case1(self):
        create_input_txt(['3 1'])
        task5()
        res = read_output()
        self.assertEqual(9, res)

    def test_case2(self):
        create_input_txt(['4 2'])
        task5()
        res = read_output()
        self.assertEqual(20, res)

    def test_case3(self):
        create_input_txt(['5 3'])
        task5()
        res = read_output()
        self.assertEqual(48, res)

    def test_case4(self):
        create_input_txt(['8 5'])
        task5()
        res = read_output()
        self.assertEqual(7320, res)

    def test_case5(self):
        create_input_txt(['8 6'])
        task5()
        res = read_output()
        self.assertEqual(728, res)


if __name__ == '__main__':
    unittest.main()
