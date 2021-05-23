from functools import reduce

import numpy


def check_row_correct(row):
    return len(set(row)) == 9 and sum(row) == sum(range(1, 10))


def check_box_correct(box: numpy.array):
    return check_row_correct(box.flatten())


def check_sudoku_correct(sudoku: numpy.array):
    return reduce(lambda x, y: x and check_row_correct(y), sudoku, True)

