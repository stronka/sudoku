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
    result = sudoku

    _brute_force_inplace(result)

    return result


def _brute_force_inplace(sudoku: numpy.array) -> None:
    if check_sudoku_correct(sudoku) or sudoku.all():
        return
    else:
        rows, cols = numpy.where(sudoku == 0)
        cell = rows[0], cols[0]

        for candidate in range(1, 10):
            sudoku[cell] = candidate
            _brute_force_inplace(sudoku)

            if check_sudoku_correct(sudoku):
                return
        else:
            sudoku[cell] = 0
            return
