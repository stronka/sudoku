import unittest
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
        result = solve_sudoku(sudoku)
        self.assertSudokuCorrect(result)

    def test_SolveSudoku_Hard_SudokuCorrect(self):
        sudoku = self.get_hard_sudoku()
        result = solve_sudoku(sudoku)
        self.assertSudokuCorrect(result)

    def test_SolveSudoku_Hard2_SudokuCorrect(self):
        sudoku = self.get_hard_sudoku2()
        result = solve_sudoku(sudoku)
        self.assertSudokuCorrect(result)

    def test_BruteForceSudoku_SudokuCorrectAlready_ReturnThisSudoku(self):
        sudoku = numpy.array([
            [7, 2, 5,    6, 4, 3,   9, 1, 8],
            [8, 3, 1,    7, 9, 2,   4, 6, 5],
            [9, 6, 4,    1, 8, 5,   3, 2, 7],

            [3, 1, 6,    5, 2, 7,   8, 4, 9],
            [2, 4, 7,    9, 6, 8,   1, 5, 3],
            [5, 9, 8,    3, 1, 4,   6, 7, 2],

            [4, 8, 9,    2, 7, 6,   5, 3, 1],
            [1, 5, 2,    4, 3, 9,   7, 8, 6],
            [6, 7, 3,    8, 5, 1,   2, 9, 4],
        ])
        self.assertSudokuCorrect(brute_force_sudoku(sudoku))

    def test_BruteForceSudoku_SudokuMissingOneElement_SolveThisElement(self):
        sudoku = numpy.array([
            [7, 2, 5,    6, 4, 3,   9, 1, 8],
            [8, 3, 1,    7, 9, 2,   4, 6, 5],
            [9, 6, 4,    1, 8, 5,   3, 2, 7],

            [3, 1, 6,    5, 2, 7,   8, 4, 9],
            [2, 4, 7,    9, 6, 8,   1, 5, 3],
            [5, 9, 8,    3, 1, 4,   6, 7, 2],

            [4, 8, 9,    2, 7, 6,   5, 3, 1],
            [1, 5, 2,    4, 3, 9,   7, 8, 6],
            [6, 7, 3,    8, 5, 1,   2, 9, 0],
        ])
        self.assertSudokuCorrect(brute_force_sudoku(sudoku))

    def assertSudokuCorrect(self, result):
        self.assertTrue(check_sudoku_correct(result))

    @staticmethod
    def assertNumpyEqual(first: numpy.array, second: numpy):
        numpy.testing.assert_equal(first, second)

    @staticmethod
    def get_regular_sudoku():
        return numpy.array([
            [0, 6, 0,   3, 0, 5,   0, 8, 0],
            [8, 0, 0,   0, 0, 0,   0, 0, 9],
            [4, 5, 0,   0, 0, 0,   0, 6, 7],

            [0, 0, 0,   2, 0, 4,   0, 0, 0],
            [2, 7, 0,   9, 0, 8,   0, 4, 3],
            [0, 0, 0,   7, 0, 1,   0, 0, 0],

            [9, 2, 0,   0, 0, 0,   0, 3, 1],
            [1, 0, 0,   0, 0, 0,   0, 0, 4],
            [0, 4, 0,   1, 0, 7,   0, 2, 0]
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
    def get_hard_sudoku_for_brute_force():
        return numpy.array([
            [7, 0, 0,    6, 4, 3,   0, 1, 0],
            [0, 3, 0,    7, 0, 0,   0, 0, 0],
            [0, 0, 4,    1, 0, 0,   3, 0, 7],

            [0, 1, 6,    0, 0, 7,   8, 0, 0],
            [2, 4, 7,    9, 6, 8,   1, 5, 3],
            [0, 0, 0,    0, 0, 0,   6, 7, 0],

            [0, 0, 9,    0, 7, 6,   5, 0, 0],
            [0, 0, 0,    0, 0, 9,   7, 8, 0],
            [0, 7, 0,    0, 5, 0,   0, 0, 4],
        ])

