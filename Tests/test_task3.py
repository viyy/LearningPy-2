import os
import unittest

from Source.task3.task3 import task3
from Tests.utility.input_output_utility import create_input_txt, read_output_raw


class Task3Tests(unittest.TestCase):
    def tearDown(self):
        os.remove('input.txt')
        os.remove('output.txt')

    def test_case1(self):
        create_input_txt(['1 3'])
        task3()
        res = read_output_raw()
        self.assertEqual('100 100', res)

    def test_case2(self):
        create_input_txt(['2 3'])
        task3()
        res = read_output_raw()
        self.assertEqual('200 101', res)

    def test_case3(self):
        create_input_txt(['3 4'])
        task3()
        res = read_output_raw()
        self.assertEqual('3000 1002', res)

    def test_case4(self):
        create_input_txt(['23 6'])
        task3()
        res = read_output_raw()
        self.assertEqual('995000 100499',
                         res)


if __name__ == '__main__':
    unittest.main()
