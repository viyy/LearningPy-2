import unittest

from Source.task6.task6 import task6
from Tests.utility.input_output_utility import create_input_txt, read_output_raw


class Task6Tests(unittest.TestCase):
    def test_case1(self):
        create_input_txt(['{[()[]{}()]}'])
        task6()
        res = read_output_raw()
        self.assertEqual('0', res)

    def test_case2(self):
        create_input_txt(['(())[[]]{{]}', '(()))', '{{{{{{{}}}}}}()[]'])
        task6()
        res = read_output_raw()
        self.assertEqual('111', res)

    def test_case3(self):
        create_input_txt(['(((', ')))', '{}[]()'])
        task6()
        res = read_output_raw()
        self.assertEqual('110', res)

    def test_case4(self):
        create_input_txt(['[[]][][]][[]][[]][[]]['])
        task6()
        res = read_output_raw()
        self.assertEqual('1', res)


if __name__ == '__main__':
    unittest.main()
