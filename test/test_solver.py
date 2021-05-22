import unittest

from logic import solve_row


class TestSolver(unittest.TestCase):
    def test_solveRow_EightMissing_Fill(self):
        row = [7, 0, 9, 6, 2, 3, 1, 5, 4]
        solved = [7, 8, 9, 6, 2, 3, 1, 5, 4]
        self.assertEqual(solved, solve_row(row))

    def test_solveRow_OneMissing_Fill(self):
        row = [2, 0, 6, 8, 5, 4, 9, 7, 3]
        solved = [2, 1, 6, 8, 5, 4, 9, 7, 3]
        self.assertEqual(solved, solve_row(row))
