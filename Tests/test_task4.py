import unittest

from Source.task4.task4 import task4
from Tests.utility.input_output_utility import create_input_txt, read_output


class Task4Tests(unittest.TestCase):
    def test_case1(self):
        create_input_txt(['3', '6 6 3 6 6 9 8 7 5 4', '13 5 9 2 9 8 12 8 12 2', '3 2 2 1 2 3 6 3 6 1'])
        task4()
        res = read_output()
        self.assertEqual(2, res)

    def test_case2(self):
        create_input_txt(['3', '0 0 0 2 2 4 4 2 2 0', '1 6 1 5 1 7 2 7 2 5', '4 5 3 4 5 4 5 6 3 6'])
        task4()
        res = read_output()
        self.assertEqual(2, res)

    def test_case3(self):
        create_input_txt(['3', '-2 2 2 0 0 -2 -2 0 0 2', '4 1 3 0 5 -2 7 0 5 2', '2 -4 0 -4 2 -2 4 -4 2 -6'])
        task4()
        res = read_output()
        self.assertEqual(2, res)

    def test_case4(self):
        create_input_txt(['1', '-2 1 -2 1 -1 3 5 0 4 -2'])
        task4()
        res = read_output()
        self.assertEqual(1, res)


if __name__ == '__main__':
    unittest.main()
