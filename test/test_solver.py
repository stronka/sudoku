import unittest
import numpy

from logic._solver import *


class TestSolver(unittest.TestCase):
    def test_CreateCandidatesStack_ReturnCorrectStack(self):
        candidate_stack = create_candidates_stack()
        self.assertNumpyEqual(numpy.array(range(1, 10)), candidate_stack[:, 0, 0])

    def test_CrossOutSudoku_SudokuEmptyWithOne_CrossOutRow(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[0, 0] = 1
        expected = numpy.array([0, 0, 0,  0, 0, 0,  0, 0, 0])

        cross_out_sudoku(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[0, 0, :])

    def test_CrossOutSudoku_SudokuEmptyWithOneAndTwo_CrossOutSecondRow(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[0, 0] = 1
        sudoku[0, 1] = 2
        expected = numpy.array([0, 0, 0,  0, 0, 0,  0, 0, 0])

        cross_out_sudoku(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[1, 0, :])

    def test_CrossOutSudoku_SudokuEmptyWithOne_CrossOutFirstCol(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[0, 0] = 1
        expected = numpy.array([0, 0, 0,  0, 0, 0,  0, 0, 0])

        cross_out_sudoku(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[0, :, 0])

    def test_CrossOutSudoku_SudokuEmptyWithOneAndTwo_CrossOutSecondCol(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[0, 0] = 1
        sudoku[0, 1] = 2
        expected = numpy.array([0, 0, 0,  0, 0, 0,  0, 0, 0])

        cross_out_sudoku(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[1, :, 1])

    def test_CrossOutSudoku_SudokuEmptyWithOne_CrossOutBox(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[0, 0] = 1
        expected = numpy.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

        cross_out_sudoku(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[0, 0:3, 0:3])

    def test_CrossOutSudoku_SudokuEmptyWithOneAndTwo_CrossOutSecondBox(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[0, 0] = 1
        sudoku[0, 1] = 2
        expected = numpy.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

        cross_out_sudoku(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[1, 0:3, 0:3])

    def test_CrossOutSudoku_SudokuEmptyWithOneAndTwoInFirstRow_CrossOutSecondBox(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[0, 0] = 1
        sudoku[1, 1] = 2
        expected = numpy.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

        cross_out_sudoku(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[1, 0:3, 0:3])

    def test_CrossOutSudoku_SudokuEmptyWithOneAndTwoInSecondRow_CrossOutSecondBox(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[0, 0] = 1
        sudoku[1, 4] = 2
        expected = numpy.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

        cross_out_sudoku(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[1, 0:3, 3:6])

    def test_CrossOutSudoku_SudokuEmptyWithOne_CrossWholeStack(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[0, 0] = 1
        expected = numpy.array([0, 0, 0,  0, 0, 0,  0, 0, 0])
        cross_out_sudoku(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[:, 0, 0])

    def test_CrossOutSudoku_SudokuEmptyWithOneAndTwoInFourthRow_CrossOutSecondBox(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[0, 0] = 1
        sudoku[3, 4] = 2
        expected = numpy.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

        cross_out_sudoku(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[1, 3:6, 3:6])

    def test_CrossOutSudoku_SudokuWithOneAndEmptyFirstCell_CandidateStackOverFirstCellIsCorrect(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[1, 1] = 1
        expected = numpy.array([0, 2, 3,  4, 5, 6,  7, 8, 9])

        cross_out_sudoku(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[:, 0, 0])

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

    def test_ProcessLastElements_LastElementNotFound_DoNothing(self):
        candidate_stack = create_candidates_stack()
        expected = candidate_stack

        process_last_elements(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack)

    def test_ProcessLastElements_LastElementInRowFound_WipeAlongStack(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[4, 0, :] = 0
        candidate_stack[4, 0, 4] = 5

        expected = numpy.array([0, 0, 0,  0, 5, 0,  0, 0, 0])

        process_last_elements(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 0, 4])

    def test_ProcessLastElements_LastElementInOtherLayerFound_WipeAlongStack(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[5, 0, :] = 0
        candidate_stack[5, 0, 4] = 6

        expected = numpy.array([0, 0, 0,  0, 0, 6,  0, 0, 0])

        process_last_elements(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 0, 4])

    def test_ProcessLastElements_LastElementInOtherLayerOtherColumnFound_WipeAlongStack(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[5, 0, :] = 0
        candidate_stack[5, 0, 5] = 6

        expected = numpy.array([0, 0, 0,  0, 0, 6,  0, 0, 0])

        process_last_elements(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 0, 5])

    def test_ProcessLastElements_LastElementInOtherLayerOtherColumnOtherRowFound_WipeAlongStack(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[5, 1, :] = 0
        candidate_stack[5, 1, 5] = 6

        expected = numpy.array([0, 0, 0,  0, 0, 6,  0, 0, 0])

        process_last_elements(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 1, 5])

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
        numpy.testing.assert_equal(first, second)
