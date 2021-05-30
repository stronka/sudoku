import functools
from itertools import product

import numpy

from sudoku.logic.utils.utils import find_box_coords

CANDIDATE_ELIMINATION_ACTION = "Remove: "

_NUMBER_FORMAT = "Number {} present in cell ({}, {})"
_REASON_TAKEN = "Candidate elimination: already taken. " + _NUMBER_FORMAT
_REASON_ROW = "Candidate elimination: present in row. " + _NUMBER_FORMAT
_REASON_COL = "Candidate elimination: present in column. " + _NUMBER_FORMAT
_REASON_BOX = "Candidate elimination: present in box. " + _NUMBER_FORMAT


def apply_candidate_elimination(stack: numpy.array, sudoku: numpy.array, *args, **kwargs) -> None:
    solution = kwargs.setdefault('solution_log', None)

    for i, j in product(range(9), range(9)):
        number = int(sudoku[i, j])
        if number:
            log_solution_steps(stack, i, j, number, solution)
            eliminate_candidates(stack, number, i, j)


def eliminate_candidates(stack, number, i, j):
    i1, i2 = find_box_coords(i)
    j1, j2 = find_box_coords(j)
    k = number - 1

    stack[:, i, j] = 0
    stack[k, i, :] = 0
    stack[k, :, j] = 0
    stack[k, i1:i2, j1:j2] = 0


def log_solution_steps(stack, i, j, number, solution=None):
    if not solution:
        return

    def _log(candidate_cell, candidate_, reason):
        log_solution_step(solution, stack, (i, j), number, candidate_cell, candidate_, reason)

    for candidate in range(9):
        _log((i, j), candidate, _REASON_TAKEN)

    candidate = number

    for i_ in range(9):
        _log((i_, j), candidate, _REASON_COL)

    for j_ in range(9):
        _log((i, j_), candidate, _REASON_ROW)

    i1, i2 = find_box_coords(i)
    j1, j2 = find_box_coords(j)

    for i_, j_ in product(range(i1, i2), range(j1, j2)):
        _log((i_, j_), candidate, _REASON_BOX)


def log_solution_step(solution, stack, number_cell, number, candidate_cell, candidate, reason):
    if stack[candidate-1, candidate_cell[0], candidate_cell[1]] != 0:
        solution.add_step(
            candidate_cell,
            CANDIDATE_ELIMINATION_ACTION + str(candidate),
            reason.format(number, number_cell[0], number_cell[1])
        )
