import functools
from itertools import product

import numpy

from sudoku.logic.utils.utils import find_box_coords

_ACTION_FORMAT = "Remove: {}"

_NUMBER_FORMAT = "Number {} present in cell ({}, {})"
_REASON_ROW = "Candidate elimination: present in row. " + _NUMBER_FORMAT
_REASON_COL = "Candidate elimination: present in column. " + _NUMBER_FORMAT
_REASON_BOX = "Candidate elimination: present in box. " + _NUMBER_FORMAT


def apply_candidate_elimination(stack: numpy.array, sudoku: numpy.array, *args, **kwargs) -> None:
    solution = kwargs.setdefault('solution_log', None)

    for i, j in product(range(9), range(9)):
        number = int(sudoku[i, j])
        if number:
            log_solution_steps(stack, number, i, j, solution)
            eliminate_candidates(stack, number, i, j)


def eliminate_candidates(stack, number, i, j):
    i1, i2 = find_box_coords(i)
    j1, j2 = find_box_coords(j)
    k = number - 1

    stack[:, i, j] = 0
    stack[k, i, :] = 0
    stack[k, :, j] = 0
    stack[k, i1:i2, j1:j2] = 0


def log_solution_steps(stack, number, i, j, solution=None):
    if not solution:
        return

    def _log(candidate_cell, reason):
        log_solution_step(solution, stack, (i, j), number, candidate_cell, reason)

    for i_ in range(9):
        if i_ != i:
            _log((i_, j), _REASON_COL)

    for j_ in range(9):
        if j_ != j:
            _log((i, j_), _REASON_ROW)

    i1, i2 = find_box_coords(i)
    j1, j2 = find_box_coords(j)

    for i_, j_ in product(range(i1, i2), range(j1, j2)):
        if i_ != i and j_ != j:
            _log((i_, j_), _REASON_BOX)


def log_solution_step(solution, stack, number_cell, number, candidate_cell, reason):
    if stack[number-1, candidate_cell[0], candidate_cell[1]] != 0:
        solution.add_step(
            candidate_cell,
            _ACTION_FORMAT.format(number),
            reason.format(number, number_cell[0], number_cell[1])
        )
