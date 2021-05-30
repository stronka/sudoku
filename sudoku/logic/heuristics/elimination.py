from itertools import product

import numpy

from sudoku.logic.utils.utils import find_box_coords

CANDIDATE_ELIMINATION_ACTION = "Remove: "

CANDIDATE_ELIMINATION_REASON_TAKEN = "Candidate elimination: already taken. Number {} present in cell ({}, {})"
CANDIDATE_ELIMINATION_REASON_ROW = "Candidate elimination: present in row. Number {} present in cell ({}, {})"
CANDIDATE_ELIMINATION_REASON_COL = "Candidate elimination: present in column. Number {} present in cell ({}, {})"
CANDIDATE_ELIMINATION_REASON_BOX = "Candidate elimination: present in box. Number {} present in cell ({}, {})"


def apply_candidate_elimination(stack: numpy.array, sudoku: numpy.array, *args, **kwargs) -> None:
    solution = kwargs.setdefault('solution_log', None)

    def log(cell, k_, reason):
        if solution and stack[k_, cell[0], cell[1]] != 0:
            solution.add_step(
                cell,
                CANDIDATE_ELIMINATION_ACTION + str(k_+1),
                reason
            )

    for i, j in product(range(0, 9), range(0, 9)):
        number = sudoku[i, j]
        if number:
            k = int(number - 1)
            i1, i2 = find_box_coords(i)
            j1, j2 = find_box_coords(j)

            for candidate in range(9):
                log((i, j), candidate, CANDIDATE_ELIMINATION_REASON_TAKEN.format(int(number), i, j))

            stack[:, i, j] = 0

            for j_ in range(9):
                log((i, j_), k, CANDIDATE_ELIMINATION_REASON_ROW.format(int(number), i, j))

            stack[k, i, :] = 0

            for i_ in range(9):
                log((i_, j), k, CANDIDATE_ELIMINATION_REASON_COL.format(int(number), i, j))

            stack[k, :, j] = 0

            for i_, j_ in product(range(i1, i2), range(j1, j2)):
                log((i_, j_), k, CANDIDATE_ELIMINATION_REASON_BOX.format(int(number), i, j))

            stack[k, i1:i2, j1:j2] = 0
