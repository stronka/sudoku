import unittest
import numpy

from logic import solve_row, solve_box


class TestSolver(unittest.TestCase):
    def test_solveRow_EightMissing_Fill(self):
        row = [7, 0, 9, 6, 2, 3, 1, 5, 4]
        solved = [7, 8, 9, 6, 2, 3, 1, 5, 4]
        self.assertEqual(solved, solve_row(row))

    def test_solveRow_OneMissing_Fill(self):
        row = [2, 0, 6, 8, 5, 4, 9, 7, 3]
        solved = [2, 1, 6, 8, 5, 4, 9, 7, 3]
        self.assertEqual(solved, solve_row(row))

    def test_solveRow_TwoNumbersMissing_Fill(self):
        row = [2, 0, 6, 8, 5, 0, 9, 7, 3]
        solved = [2, 1, 6, 8, 5, 4, 9, 7, 3]
        self.assertEqual(solved, solve_row(row))

    def test_solveBox_FiveMissing_Fill(self):
        box = numpy.array([
            [1, 2, 3],
            [4, 0, 6],
            [7, 8, 9]
        ])
        solved_box = numpy.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        self.assertNumpyEqual(solved_box, solve_box(box))

    def test_solveBox_OneMissing_Fill(self):
        box = numpy.array([
            [5, 2, 3],
            [4, 0, 6],
            [7, 8, 9]
        ])
        solved_box = numpy.array([
            [5, 2, 3],
            [4, 1, 6],
            [7, 8, 9]
        ])
        self.assertNumpyEqual(solved_box, solve_box(box))

    def assertNumpyEqual(self, first: numpy.array, second: numpy):
        self.assertTrue((first == second).all())
