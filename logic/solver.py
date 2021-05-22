import itertools
from functools import reduce

import numpy

from logic import check_sudoku_correct


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

    box_mask = numpy.zeros((9, 9))
    for i in range(0, 3):
        for j in range(0, 3):
            box_mask[3*i:3*(i+1), 3*j:3*(j+1)] = solve_box_for(sudoku[3*i:3*(i+1), 3*j:3*(j+1)], number)

    row_col_mask = numpy.where(row_mask == col_mask, row_mask, 0)
    return numpy.where(row_col_mask == box_mask, row_col_mask, 0)


def _apply_mask(sudoku: numpy.array, number: int) -> numpy.array:
    return numpy.array([solve_row_for(row, number) for row in sudoku])


def annotate_sudoku(sudoku: numpy.array) -> numpy.array:
    return numpy.array(list(map(lambda x: solve_sudoku_for(sudoku, x), range(1, 10))))


def find_definitive_annotations(sudoku):
    annotated_sudoku = annotate_sudoku(sudoku)
    result = numpy.zeros((9, 9))

    for i, j in itertools.product(range(0, 9), range(0, 9)):
        result[i, j] = _get_definite_annotation(annotated_sudoku[:, i, j]) if sudoku[i, j] == 0 else 0

    return result


def _get_definite_annotation(annotation):
    return annotation.max() if annotation.sum()/annotation.max() == 1 else 0


def solve_sudoku(sudoku: numpy.array) -> numpy.array:
    result = sudoku

    while not check_sudoku_correct(result):
        annotations = find_definitive_annotations(result)
        if annotations.any():
            result = numpy.add(result, annotations)
        else:
            raise Exception("No more annotations found, but sudoku is still unsolved!")

    return result

