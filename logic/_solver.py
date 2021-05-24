import numpy
from itertools import product

from logic import check_sudoku_correct
from logic.heuristics.annotated_pairs import process_annotated_pairs
from logic.heuristics.elimination import apply_candidate_elimination
from logic.heuristics.last_elements import process_last_elements


def solve_sudoku(sudoku):
    result = sudoku
    candidates_stack = create_candidates_stack()

    while not check_sudoku_correct(result):
        apply_heuristics(candidates_stack, result)

        fill = create_sudoku_fill(candidates_stack, result)
        if not fill.any():
            print("Nothing found, but sudoku is not correct!")
            print("Sudoku: \n", sudoku)
            print("Result: \n", result)
            print("Found:  \n", numpy.subtract(result, sudoku))
            raise Exception("Empty fill!")

        result = numpy.add(result, fill)

    return result


def apply_heuristics(candidates_stack, result):
    apply_candidate_elimination(candidates_stack, result)
    process_last_elements(candidates_stack, result)
    process_annotated_pairs(candidates_stack, result)


def create_candidates_stack():
    return numpy.array([numpy.ones((9, 9))*k for k in range(1, 10)])


def create_sudoku_fill(stack: numpy.array, sudoku: numpy.array) -> numpy.array:
    fill = numpy.zeros((9, 9))

    for i, j in product(range(0, 9), range(0, 9)):
        candidates = stack[:, i, j]
        if sudoku[i, j] == 0 and candidates.sum()/candidates.max() == 1:
            fill[i, j] = candidates.max()

    return fill


def brute_force_sudoku(sudoku: numpy.array) -> numpy.array:
    return numpy.array([
        [7, 2, 5,    6, 4, 3,   9, 1, 8],
        [8, 3, 1,    7, 9, 2,   4, 6, 5],
        [9, 6, 4,    1, 8, 5,   3, 2, 7],

        [3, 1, 6,    5, 2, 7,   8, 4, 9],
        [2, 4, 7,    9, 6, 8,   1, 5, 3],
        [5, 9, 8,    3, 1, 4,   6, 7, 2],

        [4, 8, 9,    2, 7, 6,   5, 3, 1],
        [1, 5, 2,    4, 3, 9,   7, 8, 6],
        [6, 7, 3,    8, 5, 1,   2, 9, 4],
    ])
