import unittest
import numpy

from logic.solver import *


class TestSolver(unittest.TestCase):
    @staticmethod
    def get_regular_sudoku():
        return numpy.array([
            [0, 6, 0, 3, 0, 5, 0, 8, 0],
            [8, 0, 0, 0, 0, 0, 0, 0, 9],
            [4, 5, 0, 0, 0, 0, 0, 6, 7],
            [0, 0, 0, 2, 0, 4, 0, 0, 0],
            [2, 7, 0, 9, 0, 8, 0, 4, 3],
            [0, 0, 0, 7, 0, 1, 0, 0, 0],
            [9, 2, 0, 0, 0, 0, 0, 3, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 4],
            [0, 4, 0, 1, 0, 7, 0, 2, 0]
        ])

    @staticmethod
    def get_hard_sudoku():
        return numpy.array([
            [4, 0, 0,    0, 0, 0,   3, 6, 5],
            [2, 0, 9,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 5, 8,   0, 0, 0],

            [7, 0, 0,    0, 6, 0,   8, 1, 0],
            [0, 0, 0,    0, 3, 0,   0, 0, 0],
            [0, 9, 1,    0, 2, 0,   0, 0, 3],

            [0, 0, 0,    3, 4, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   5, 0, 9],
            [3, 8, 7,    0, 0, 0,   0, 0, 4],
        ])

    def assertNumpyEqual(self, first: numpy.array, second: numpy):
        self.assertTrue((first == second).all())
