import unittest

from Source.task7.task7 import task7
from Tests.utility.input_output_utility import create_input_txt, read_grid_int


class Task7Tests(unittest.TestCase):
    def test_case1(self):
        create_input_txt(['4 5 2', '0 2 2 2 2', '0 2 2 2 2', '1 1 2 2 2', '1 1 0 0 0'])
        task7()
        res = read_grid_int()
        self.assertEqual([[0, 0, 2, 2],
                          [1, 1, 5, 4]], res)

    def test_case2(self):
        create_input_txt(['10 10 8',
                          '6 6 6 6 6 6 6 5 0 7',
                          '6 6 6 6 6 6 6 5 0 7',
                          '6 6 6 6 6 6 6 5 2 7',
                          '6 6 6 6 6 6 6 5 3 7',
                          '0 0 0 1 2 3 5 5 3 7',
                          '0 0 0 1 2 3 5 5 3 7',
                          '0 0 0 1 2 2 5 5 2 2',
                          '0 0 0 1 4 0 5 5 0 0',
                          '8 8 8 8 1 0 5 5 0 0',
                          '8 8 8 8 0 0 0 0 0 0',
                          ])
        task7()
        res = read_grid_int()
        self.assertEqual([[3, 1, 5, 6],
                          [4, 3, 10, 8],
                          [5, 4, 9, 7],
                          [4, 2, 5, 3],
                          [6, 1, 8, 10],
                          [0, 6, 7, 10],
                          [9, 4, 10, 10],
                          [0, 0, 4, 2],
                          ], res)


if __name__ == '__main__':
    unittest.main()
