import unittest

from logic.heuristics.identical_pairs import process_identical_pairs
from logic._solver import *


class TestSolver(unittest.TestCase):
    def test_CreateCandidatesStack_ReturnCorrectStack(self):
        candidate_stack = create_candidates_stack()
        self.assertNumpyEqual(numpy.array(range(1, 10)), candidate_stack[:, 0, 0])

    def test_CreateSudokuFill_StackIsNonDefinitive_FillEmpty(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[:, 0, 0] = [0, 2, 3,  0, 0, 0,  0, 0, 0]
        sudoku = numpy.zeros((9, 9))

        expected = numpy.zeros((9, 9))

        fill = create_sudoku_fill(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, fill)

    def test_CreateSudokuFill_StackIsDefinitive_FillCorrect(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[:, 0, 0] = [0, 0, 0,  0, 5, 0,  0, 0, 0]
        sudoku = numpy.zeros((9, 9))

        expected = numpy.zeros((9, 9))
        expected[0, 0] = 5

        fill = create_sudoku_fill(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, fill)

    def test_CreateSudokuFill_StackIsNonDefiniteOverNonEmptyCell_FillEmpty(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[:, 0, 0] = [0, 0, 0,  0, 5, 0,  0, 0, 0]
        sudoku = numpy.zeros((9, 9))
        sudoku[0, 0] = 1

        expected = numpy.zeros((9, 9))
        fill = create_sudoku_fill(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, fill)

    def test_SolveSudoku_Regular_SudokuCorrect(self):
        sudoku = self.get_regular_sudoku()
        self.assertTrue(check_sudoku_correct(solve_sudoku(sudoku)))

    def test_SolveSudoku_Hard_SudokuCorrect(self):
        sudoku = self.get_hard_sudoku()
        self.assertTrue(check_sudoku_correct(solve_sudoku(sudoku)))

    def test_SolveSudoku_Hard2_SudokuCorrect(self):
        sudoku = self.get_hard_sudoku2()
        self.assertTrue(check_sudoku_correct(solve_sudoku(sudoku)))

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

    @staticmethod
    def get_hard_sudoku2():
        return numpy.array([
            [0, 0, 2,    0, 0, 0,   0, 0, 8],
            [0, 5, 0,    0, 0, 0,   7, 0, 0],
            [4, 0, 0,    0, 0, 1,   6, 3, 0],

            [0, 0, 0,    4, 0, 0,   3, 7, 2],
            [0, 0, 0,    9, 0, 3,   0, 0, 0],
            [1, 2, 3,    0, 0, 6,   0, 0, 0],

            [0, 8, 9,    5, 0, 0,   0, 0, 4],
            [0, 0, 5,    0, 0, 0,   0, 9, 0],
            [2, 0, 0,    0, 0, 0,   5, 0, 0],
        ])

    @staticmethod
    def assertNumpyEqual(first: numpy.array, second: numpy):
        numpy.testing.assert_equal(first, second)

