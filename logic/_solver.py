import numpy
from itertools import product
from functools import reduce

from logic import check_sudoku_correct


def create_candidates_stack():
    return numpy.array([numpy.ones((9, 9))*k for k in range(1, 10)])


def cross_out_sudoku(stack: numpy.array, sudoku: numpy.array) -> None:
    _cross_out_rows(stack, sudoku)

    return


def _cross_out_rows(stack, sudoku):
    for i, j in product(range(0, 9), range(0, 9)):
        number = sudoku[i, j]
        k = int(number - 1)

        stack[k, i, :] = 0
        stack[k, :, j] = 0
        stack[k, i, j] = number


def solve_sudoku(sudoku):
    return sudoku
