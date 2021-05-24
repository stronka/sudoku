import unittest
from logic._logic import *


class TestLogic(unittest.TestCase):
    def test_checkRowCorrect_RowIsCorrect_ReturnTrue(self):
        row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertTrue(check_row_correct(row))

    def test_checkRowCorrect_RowHasDuplicatedNumber_ReturnFalse(self):
        row = [1, 2, 3, 3, 5, 6, 7, 8, 9]
        self.assertFalse(check_row_correct(row))

    def test_checkRowCorrect_RowHasNumberOutOfBounds_ReturnFalse(self):
        row = [1, 2, 3, 11, 5, 6, 7, 8, 9]
        self.assertFalse(check_row_correct(row))

    def test_checkBoxCorrect_BoxIsCorrect_ReturnTrue(self):
        box = numpy.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        self.assertTrue(check_box_correct(box))

    def test_checkBoxCorrect_BoxHasDuplicatedNumber_ReturnFalse(self):
        box = numpy.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 5, 9]
        ])
        self.assertFalse(check_box_correct(box))

    def test_checkBoxCorrect_BoxHasNumberOutOfBounds_ReturnFalse(self):
        box = numpy.array([
            [1, 2, 3],
            [4, 51, 6],
            [7, 5, 9]
        ])
        self.assertFalse(check_box_correct(box))

    def test_checkSudokuCorrect_SudokuCorrect_ReturnTrue(self):
        sudoku = numpy.array([
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
        self.assertTrue(check_sudoku_correct(sudoku))

    def test_checkSudokuCorrect_SudokuIsNotCorrect_ReturnFalse(self):
        sudoku = numpy.array([
            [7, 8, 9, 6, 2, 3, 1, 5, 4],
            [2, 1, 6, 8, 5, 4, 9, 7, 3],
            [5, 4, 3, 9, 7, 1, 6, 2, 8],
            [9, 3, 4, 7, 1, 2, 8, 6, 5],
            [8, 6, 5, 3, 5, 9, 7, 1, 2],
            [1, 7, 2, 5, 6, 8, 4, 3, 9],
            [4, 5, 1, 2, 8, 7, 3, 9, 6],
            [3, 2, 8, 1, 9, 6, 5, 4, 7],
            [6, 9, 7, 4, 3, 5, 2, 8, 1]
        ])
        self.assertFalse(check_sudoku_correct(sudoku))
