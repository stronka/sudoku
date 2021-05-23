import numpy
from itertools import product
from functools import reduce

from logic import check_sudoku_correct


def create_candidates_stack():
    return numpy.array([numpy.ones((9, 9))*k for k in range(1, 10)])


def cross_out_sudoku(stack: numpy.array, sudoku: numpy.array) -> None:
    for i, j in product(range(0, 9), range(0, 9)):
        number = sudoku[i, j]

        k = int(number - 1)
        i1, i2 = find_box_coords(i)
        j1, j2 = find_box_coords(j)

        stack[k, i, :] = 0
        stack[k, :, j] = 0
        stack[k, i1:i2, j1:j2] = 0

        stack[k, i, j] = number

    return


def find_box_coords(i):
    i_lo, i_hi = 0, 0
    bounds = [0, 3, 6, 9]

    for b in bounds:
        if i < b:
            i_hi = b
            break
        i_lo = b

    return i_lo, i_hi


def fill_sudoku(stack: numpy.array, sudoku: numpy.array) -> None:
    pass


def solve_sudoku(sudoku):
    return sudoku
