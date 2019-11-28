import os
import unittest

from Source.task2.task2 import task2
from Tests.utility.input_output_utility import read_output, create_input_txt


class Task2Tests(unittest.TestCase):
    def tearDown(self):
        os.remove('input.txt')
        os.remove('output.txt')

    def test_case1(self):
        create_input_txt(['1 3'])
        task2()
        res = read_output()
        self.assertEqual(1, res)

    def test_case2(self):
        create_input_txt(['2 7'])
        task2()
        res = read_output()
        self.assertEqual(21, res)

    def test_case3(self):
        create_input_txt(['3 10'])
        task2()
        res = read_output()
        self.assertEqual(274, res)

    def test_case4(self):
        create_input_txt(['10 300'])
        task2()
        res = read_output()
        self.assertEqual(882971537534051991955001088904131417322100611304096337608932781399847726784040386810546040,
                         res)


if __name__ == '__main__':
    unittest.main()
