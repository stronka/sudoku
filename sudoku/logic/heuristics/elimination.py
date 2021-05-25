from itertools import product

import numpy

from sudoku.logic.utils.utils import find_box_coords


def apply_candidate_elimination(stack: numpy.array, sudoku: numpy.array) -> None:
    for i, j in product(range(0, 9), range(0, 9)):
        number = sudoku[i, j]
        if number:
            k = int(number - 1)
            i1, i2 = find_box_coords(i)
            j1, j2 = find_box_coords(j)

            stack[k, i, :] = 0
            stack[k, :, j] = 0
            stack[:, i, j] = 0
            stack[k, i1:i2, j1:j2] = 0
