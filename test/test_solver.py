import unittest
import numpy

from logic import solve_row, solve_box, solve_row_for, solve_box_for, solve_sudoku_for, solve_sudoku, \
    check_sudoku_correct, mask_sudoku_for, annotate_sudoku, find_definitive_annotations


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

    def test_solveRowFor_ForOneWithEmptyArray_ReturnFullOnes(self):
        row = [0]*9
        expected = [1]*9
        self.assertEqual(expected, solve_row_for(row, 1))

    def test_solveRowFor_ForTwoWithEmptyArray_ReturnFullOnes(self):
        row = [0]*9
        expected = [2]*9
        self.assertEqual(expected, solve_row_for(row, 2))

    def test_solveRowFor_NonEmpyArray_ReturnNumberMask(self):
        row = [1, 2, 3, 0, 0, 0, 7, 8, 9]
        expected = [0, 0, 0, 5, 5, 5, 0, 0, 0]
        self.assertEqual(expected, solve_row_for(row, 5))

    def test_solveRowFor_NumberExistsAlready_ReturnPreciseMask(self):
        row = [1, 2, 3, 0, 0, 0, 7, 8, 9]
        expected = [0, 0, 3, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected, solve_row_for(row, 3))

    def test_solveBoxFor_ForOneWithEmptyBox_ReturnFullOnes(self):
        box = numpy.zeros((3, 3))
        expected = numpy.ones((3, 3))
        self.assertNumpyEqual(expected, solve_box_for(box, 1))

    def test_solveBoxFor_ForTwoWithMissingSpaces_ReturnNumberMask(self):
        box = numpy.array([
            [0, 2, 3],
            [4, 0, 6],
            [7, 8, 9]
        ])
        expected = numpy.array([
            [5, 0, 0],
            [0, 5, 0],
            [0, 0, 0]
        ])
        self.assertNumpyEqual(expected, solve_box_for(box, 5))

    def test_solveBoxFor_ForEightWithEightPresent_ReturnPreciseMask(self):
        box = numpy.array([
            [0, 2, 3],
            [4, 0, 6],
            [7, 8, 9]
        ])
        expected = numpy.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 8, 0]
        ])
        self.assertNumpyEqual(expected, solve_box_for(box, 8))

    def test_solveSudokuFor_ForEightWithOneGap_ReturnPreciseMask(self):
        sudoku = numpy.array([
            [7, 0, 9, 6, 2, 3, 1, 5, 4],
            [2, 1, 6, 8, 5, 4, 9, 7, 3],
            [5, 4, 3, 9, 7, 1, 6, 2, 8],
            [9, 3, 4, 7, 1, 2, 8, 6, 5],
            [8, 6, 5, 3, 4, 9, 7, 1, 2],
            [1, 7, 2, 5, 6, 8, 4, 3, 9],
            [4, 5, 1, 2, 8, 7, 3, 9, 6],
            [3, 2, 8, 1, 9, 6, 5, 4, 7],
            [6, 9, 7, 4, 3, 5, 2, 8, 1]
        ])
        expected = numpy.array([
            [0, 8, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 8, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 8],
            [0, 0, 0, 0, 0, 0, 8, 0, 0],
            [8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 8, 0, 0, 0],
            [0, 0, 0, 0, 8, 0, 0, 0, 0],
            [0, 0, 8, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 8, 0]
        ])
        self.assertNumpyEqual(expected, solve_sudoku_for(sudoku, 8))

    def test_solveSudokuFor_ForEightWithEightsMissing_ReturnPreciseMask(self):
        sudoku = numpy.array([
            [7, 0, 9, 6, 2, 3, 1, 5, 4],
            [2, 1, 6, 0, 5, 4, 9, 7, 3],
            [5, 4, 3, 9, 7, 1, 6, 2, 8],
            [9, 3, 4, 7, 1, 2, 8, 6, 5],
            [8, 6, 5, 3, 4, 9, 7, 1, 2],
            [1, 7, 2, 5, 6, 8, 4, 3, 9],
            [4, 5, 1, 2, 8, 7, 3, 9, 6],
            [3, 2, 8, 1, 9, 6, 5, 4, 7],
            [6, 9, 7, 4, 3, 5, 2, 8, 1]
        ])
        expected = numpy.array([
            [0, 8, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 8, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 8],
            [0, 0, 0, 0, 0, 0, 8, 0, 0],
            [8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 8, 0, 0, 0],
            [0, 0, 0, 0, 8, 0, 0, 0, 0],
            [0, 0, 8, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 8, 0]
        ])
        self.assertNumpyEqual(expected, solve_sudoku_for(sudoku, 8))

    def test_solveSudokuFor_ForEightWithEightsDeductibleFromColumn_ReturnPreciseMask(self):
        sudoku = numpy.array([
            [7, 0, 0, 6, 2, 3, 1, 5, 4],
            [2, 1, 6, 0, 5, 4, 9, 7, 3],
            [5, 4, 3, 9, 7, 1, 6, 2, 8],
            [9, 3, 4, 7, 1, 2, 8, 6, 5],
            [8, 6, 5, 3, 4, 9, 7, 1, 2],
            [1, 7, 2, 5, 6, 8, 4, 3, 9],
            [4, 5, 1, 2, 8, 7, 3, 9, 6],
            [3, 2, 8, 1, 9, 6, 5, 4, 7],
            [6, 9, 7, 4, 3, 5, 2, 8, 1]
        ])
        expected = numpy.array([
            [0, 8, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 8, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 8],
            [0, 0, 0, 0, 0, 0, 8, 0, 0],
            [8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 8, 0, 0, 0],
            [0, 0, 0, 0, 8, 0, 0, 0, 0],
            [0, 0, 8, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 8, 0]
        ])
        self.assertNumpyEqual(expected, solve_sudoku_for(sudoku, 8))

    def test_solveSudoku_EightMissing_ReturnSudoku(self):
        sudoku = numpy.array([
            [7, 0, 9, 6, 2, 3, 1, 5, 4],
            [2, 1, 6, 8, 5, 4, 9, 7, 3],
            [5, 4, 3, 9, 7, 1, 6, 2, 8],
            [9, 3, 4, 7, 1, 2, 8, 6, 5],
            [8, 6, 5, 3, 4, 9, 7, 1, 2],
            [1, 7, 2, 5, 6, 8, 4, 3, 9],
            [4, 5, 1, 2, 8, 7, 3, 9, 6],
            [3, 2, 8, 1, 9, 6, 5, 4, 7],
            [6, 9, 7, 4, 3, 5, 2, 8, 1]
        ])
        expected = numpy.array([
            [7, 8, 9, 6, 2, 3, 1, 5, 4],
            [2, 1, 6, 8, 5, 4, 9, 7, 3],
            [5, 4, 3, 9, 7, 1, 6, 2, 8],
            [9, 3, 4, 7, 1, 2, 8, 6, 5],
            [8, 6, 5, 3, 4, 9, 7, 1, 2],
            [1, 7, 2, 5, 6, 8, 4, 3, 9],
            [4, 5, 1, 2, 8, 7, 3, 9, 6],
            [3, 2, 8, 1, 9, 6, 5, 4, 7],
            [6, 9, 7, 4, 3, 5, 2, 8, 1]
        ])
        self.assertNumpyEqual(expected, solve_sudoku(sudoku))

    def test_solveSudoku_NineMissing_ReturnSudoku(self):
        sudoku = numpy.array([
            [7, 8, 0, 6, 2, 3, 1, 5, 4],
            [2, 1, 6, 8, 5, 4, 9, 7, 3],
            [5, 4, 3, 9, 7, 1, 6, 2, 8],
            [9, 3, 4, 7, 1, 2, 8, 6, 5],
            [8, 6, 5, 3, 4, 9, 7, 1, 2],
            [1, 7, 2, 5, 6, 8, 4, 3, 9],
            [4, 5, 1, 2, 8, 7, 3, 9, 6],
            [3, 2, 8, 1, 9, 6, 5, 4, 7],
            [6, 9, 7, 4, 3, 5, 2, 8, 1]
        ])
        expected = numpy.array([
            [7, 8, 9, 6, 2, 3, 1, 5, 4],
            [2, 1, 6, 8, 5, 4, 9, 7, 3],
            [5, 4, 3, 9, 7, 1, 6, 2, 8],
            [9, 3, 4, 7, 1, 2, 8, 6, 5],
            [8, 6, 5, 3, 4, 9, 7, 1, 2],
            [1, 7, 2, 5, 6, 8, 4, 3, 9],
            [4, 5, 1, 2, 8, 7, 3, 9, 6],
            [3, 2, 8, 1, 9, 6, 5, 4, 7],
            [6, 9, 7, 4, 3, 5, 2, 8, 1]
        ])
        self.assertNumpyEqual(expected, solve_sudoku(sudoku))

    def test_MaskSudoku_RegularSudoku_ReturnCorrectEightMaskAt02(self):
        sudoku = self.get_regular_sudoku()
        expected = numpy.array((
            0,  # row mask
            8,  # col mask
            0   # box mask
        ))
        self.assertNumpyEqual(expected, mask_sudoku_for(sudoku, 8)[:, 0, 2])

    def test_MaskSudoku_RegularSudoku_ReturnCorrectEightMaskAt10(self):
        sudoku = self.get_regular_sudoku()
        expected = numpy.array((
            8,  # row mask
            8,  # col mask
            8   # box mask
        ))
        self.assertNumpyEqual(expected, mask_sudoku_for(sudoku, 8)[:, 1, 0])

    def test_MaskSudoku_RegularSudoku_ReturnCorrectFiveMaskAt10(self):
        sudoku = self.get_regular_sudoku()
        expected = numpy.array((
            0,  # row mask
            0,  # col mask
            0   # box mask
        ))
        self.assertNumpyEqual(expected, mask_sudoku_for(sudoku, 5)[:, 1, 0])

    def test_MaskSudoku_RegularSudoku_ReturnCorrectFiveMaskAt11(self):
        sudoku = self.get_regular_sudoku()
        expected = numpy.array((
            5,  # row mask
            0,  # col mask
            0   # box mask
        ))
        self.assertNumpyEqual(expected, mask_sudoku_for(sudoku, 5)[:, 1, 1])

    def test_AnnotateSudoku_RegularSudoku_ReturnCorrectMaskAt11(self):
        sudoku = self.get_regular_sudoku()
        expected = numpy.array([1, 0, 3, 0, 0, 0, 0, 0, 0])
        self.assertNumpyEqual(expected, annotate_sudoku(sudoku)[:, 1, 1])

    def test_SolveSudoku_RegularSudoku_ReturnSudoku(self):
        sudoku = self.get_regular_sudoku()
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

    def assertNumpyEqual(self, first: numpy.array, second: numpy):
        self.assertTrue((first == second).all())
