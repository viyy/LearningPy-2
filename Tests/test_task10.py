import unittest

from Source.task10.task10 import task10
from Tests.utility.input_output_utility import create_input_txt, read_output_raw


class Task10Tests(unittest.TestCase):
    def test_case1(self):
        create_input_txt(['1+2-(3-5)/2'])
        f = open('input.txt', 'r')
        line = f.readline()
        f.close()
        task10(line)
        res = read_output_raw()
        self.assertEqual('4', res)

    def test_case2(self):
        create_input_txt(['0-10/2+5'])
        f = open('input.txt', 'r')
        line = f.readline()
        f.close()
        task10(line)
        res = read_output_raw()
        self.assertEqual('0', res)

    def test_case3(self):
        create_input_txt(['2+2*2'])
        f = open('input.txt', 'r')
        line = f.readline()
        f.close()
        task10(line)
        res = read_output_raw()
        self.assertEqual('6', res)

    def test_case4(self):
        create_input_txt(['2*(2+2)'])
        f = open('input.txt', 'r')
        line = f.readline()
        f.close()
        task10(line)
        res = read_output_raw()
        self.assertEqual('8', res)

    def test_case5(self):
        create_input_txt(['-2++3('])
        f = open('input.txt', 'r')
        line = f.readline()
        f.close()
        task10(line)
        res = read_output_raw()
        self.assertEqual('Ошибка!', res)

    def test_case6(self):
        create_input_txt(['((((2^2^2+2*2/4)+10)/9+3)-1)/5'])
        f = open('input.txt', 'r')
        line = f.readline()
        f.close()
        task10(line)
        res = read_output_raw()
        self.assertEqual('1', res)


if __name__ == '__main__':
    unittest.main()
