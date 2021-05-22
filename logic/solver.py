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


def process_last_pairs(annotate):
    def process(sudoku: numpy.array):
        filtered_annotations = annotate(sudoku)

        for j in range(0, 9):
            ks = []
            indices = []
            for k in range(0, 9):
                    col = filtered_annotations[k, :, j]
                    for n in range(0, 3):
                        subcol = filtered_annotations[k, 3*n:3*(n+1), j]
                        if subcol.sum()/subcol.max() == 2 and col.sum()/col.max() == 2:
                            ks.append(k)
                            indices.append(col.nonzero())

            if len(ks) == 2:
                for k in range(0, 9):
                    if k not in ks:
                        filtered_annotations[k, indices[0], j] = 0

        return filtered_annotations

    return process


@process_last_pairs
def annotate_sudoku(sudoku: numpy.array) -> numpy.array:
    return numpy.array(list(map(lambda x: solve_sudoku_for(sudoku, x), range(1, 10))))


def find_definitive_annotations(sudoku):
    annotated_sudoku = annotate_sudoku(sudoku)
    result = numpy.zeros((9, 9))

    for i, j in itertools.product(range(0, 9), range(0, 9)):
        if sudoku[i, j] == 0:
            result[i, j] = _get_definite_annotation(annotated_sudoku, i, j)

    return result


def _get_definite_annotation(annotation, i, j):
    annotation_stack = annotation[:, i, j]
    if annotation_stack.sum()/annotation_stack.max() == 1:
        return annotation_stack.max()

    box_bounds = [0, 3, 6, 9]
    i_lower, i_upper, j_lower, j_upper = 0, 0, 0, 0

    for bound in box_bounds:
        if i < bound:
            i_upper = bound
            break
        i_lower = bound

    for bound in box_bounds:
        if j < bound:
            j_upper = bound
            break
        j_lower = bound

    for k in range(0, 9):
        annotation_box = annotation[k, i_lower:i_upper, j_lower:j_upper].flatten()
        if annotation_box.sum()/annotation_box.max() == 1 and annotation_box.max() == annotation_stack[k]:
            return annotation_box.max()

        annotation_col = annotation[k, i, :]
        if annotation_col.sum()/annotation_col.max() == 1 and annotation_col.max() == annotation_stack[k]:
            return annotation_col.max()

        annotation_row = annotation[k, :, j]
        if annotation_row.sum()/annotation_row.max() == 1 and annotation_row.max() == annotation_stack[k]:
            return annotation_row.max()

    return 0


def solve_sudoku(sudoku: numpy.array) -> numpy.array:
    result = sudoku

    while not check_sudoku_correct(result):
        annotations = find_definitive_annotations(result)
        if annotations.any():
            result = numpy.add(result, annotations)
        else:
            raise Exception("No more annotations found, but sudoku is still unsolved!")

    return result

