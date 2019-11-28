import unittest
import os
from Source.task1.task1 import task1
from Tests.utility.input_output_utility import create_input_txt, read_output


class Task1Tests(unittest.TestCase):
    def tearDown(self):
        os.remove('input.txt')
        os.remove('output.txt')

    def test_case1(self):
        create_input_txt(['5', '73 31 96 24 46'])
        task1()
        res = read_output()
        self.assertEqual(380, res)

    def test_case2(self):
        create_input_txt(['10', '1 2 3 4 5 6 7 8 9 10'])
        task1()
        res = read_output()
        self.assertEqual(100, res)

    def test_case3(self):
        create_input_txt(['10', '10 9 8 7 6 5 4 3 2 1'])
        task1()
        res = read_output()
        self.assertEqual(55, res)

    def test_case4(self):
        create_input_txt(['20', '10 9 8 7 6 5 4 3 2 1 10 9 10 9 8 7 6 5 4 3'])
        task1()
        res = read_output()
        self.assertEqual(172, res)


if __name__ == '__main__':
    unittest.main()
