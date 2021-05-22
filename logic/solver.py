from functools import reduce

import numpy


def solve_row(row):
    missing = set(range(1, 10)).difference(set(row))
    return list(map(lambda x: x if x != 0 else missing.pop(), row))


def solve_row_for(row, number):
    return list(map(lambda x: number if x == int(number in row)*number else 0, row))


def solve_box(box: numpy.array) -> numpy.array:
    return numpy.array(solve_row(box.flatten())).reshape((3, 3))


def solve_box_for(box: numpy.array, number: int):
    return numpy.array(solve_row_for(box.flatten(), number)).reshape((3, 3))


def solve_sudoku_for(sudoku: numpy.array, number: int) -> numpy.array:
    row_mask = _apply_mask(sudoku, number)
    col_mask = _apply_mask(sudoku.transpose(), number).transpose()
    return numpy.where(row_mask == col_mask, row_mask, 0)


def solve_sudoku(sudoku: numpy.array) -> numpy.array:
    masks = map(lambda x: solve_sudoku_for(sudoku, x), range(1, 10))
    return reduce(lambda x, y: numpy.add(x, y), masks)


def _apply_mask(sudoku: numpy.array, number: int) -> numpy.array:
    return numpy.array([solve_row_for(row, number) for row in sudoku])