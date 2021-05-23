import numpy
from itertools import product
from functools import reduce

from logic import check_sudoku_correct


def create_candidates_stack():
    return numpy.array([numpy.ones((9, 9))*k for k in range(1, 10)])


def cross_out_sudoku(stack: numpy.array, sudoku: numpy.array) -> None:
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


def process_last_elements(stack: numpy.array) -> None:
    for k in range(0, 9):
        for i in range(0, 9):
            row = stack[k, i, :]
            if row.sum() and row.sum()/row.max() == 1:
                ind = numpy.nonzero(row)[0]
                stack[:, i, ind] = 0
                stack[k, i, ind] = k+1

        for j in range(0, 9):
            col = stack[k, :, j]
            if col.sum() and col.sum()/col.max() == 1:
                ind = numpy.nonzero(col)[0]
                stack[:, ind, j] = 0
                stack[k, ind, j] = k+1
    return


def process_annotated_pairs(stack: numpy.array) -> None:
    for b in range(3):
        for i in range(9):
            for n, m in ((3*b, 3*b+1), (3*b+1, 3*b+2), (3*b, 3*b+2)):
                non_pair_ks = list(range(9))

                for k in range(9):
                    candidate = stack[k, i, (n, m)]
                    candidate_row = stack[k, i, :]
                    if candidate_row.sum() == candidate.sum() != 0 and candidate.sum()/candidate.max() == 2:
                        non_pair_ks.remove(k)

                if len(non_pair_ks) == 7:
                    stack[non_pair_ks, i, n] = 0
                    stack[non_pair_ks, i, m] = 0

        for j in range(9):
            for n, m in ((3*b, 3*b+1), (3*b+1, 3*b+2), (3*b, 3*b+2)):
                non_pair_ks = list(range(9))

                for k in range(9):
                    candidate = stack[k, (n, m), j]
                    candidate_col = stack[k, :, j]
                    if candidate_col.sum() == candidate.sum() != 0 and candidate.sum()/candidate.max() == 2:
                        non_pair_ks.remove(k)
                if len(non_pair_ks) == 7:
                    stack[non_pair_ks, n, j] = 0
                    stack[non_pair_ks, m, j] = 0
    return


def process_identical_pairs(stack: numpy.array) -> None:
    for j in range(9):
        for n in range(2):
            pair_ids = []
            for k in range(9):
                candidate = stack[k, n:n+2, j]
                if candidate.max() and candidate.sum()/candidate.max() == 2:
                    pair_ids.append(k)

            if len(pair_ids) >= 2:
                for k in pair_ids:
                    stack[k, :, j] = 0
                    stack[k, n:n+2, j] = k+1

    return


def create_sudoku_fill(stack: numpy.array, sudoku: numpy.array) -> numpy.array:
    fill = numpy.zeros((9, 9))

    for i, j in product(range(0, 9), range(0, 9)):
        candidates = stack[:, i, j]
        if sudoku[i, j] == 0 and candidates.sum()/candidates.max() == 1:
            fill[i, j] = candidates.max()

    return fill


def solve_sudoku(sudoku):
    result = sudoku
    candidates_stack = create_candidates_stack()

    while not check_sudoku_correct(result):
        cross_out_sudoku(candidates_stack, result)

        process_last_elements(candidates_stack)
        process_annotated_pairs(candidates_stack)

        fill = create_sudoku_fill(candidates_stack, result)
        if not fill.any():
            print("Nothing found, but sudoku is not correct!")
            print("Sudoku: \n", sudoku)
            print("Result: \n", result)
            print("Found:  \n", numpy.subtract(result, sudoku))
            raise Exception("Empty fill!")

        result = numpy.add(result, fill)

    return result
