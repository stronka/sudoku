import copy
import itertools

import numpy

from sudoku.logic.utils.utils import find_box_coords

_ACTION = "Remove {}"
_REASON_ROW = "Candidate line: candidates in cells ({0}, {1}) and ({0}, {2}) form a line."
_REASON_COL = "Candidate line: candidates in cells ({1}, {0}) and ({2}, {0}) form a line."


def process_candidate_lines(stack: numpy.array, *args, **kwargs) -> None:
    solution_log = kwargs.setdefault("solution_log", None)

    for candidate in range(9):
        initial_candidate_layer = copy.copy(stack[candidate, :, :])

        for row in range(9):
            initial_stack_row = initial_candidate_layer[row, :]

            done = False
            rollback = False
            if solution_log:
                solution_log.begin_transaction()

            for b in range(3):
                box_row = initial_stack_row[3*b:3*b+3]

                i1, i2 = find_box_coords(row)

                box_row_sum = box_row.sum()
                box_sum = initial_candidate_layer[i1:i2, 3*b:3*b+3].flatten().sum()

                if box_sum == box_row_sum and box_row_sum / box_row.max() == 2:
                    if done:
                        rollback = True
                        break

                    stack[candidate, row, 0:3*b] = 0
                    stack[candidate, row, 3*b+3:9] = 0

                    if solution_log:
                        for j in numpy.argwhere(initial_candidate_layer[row, :] > stack[candidate, row, :]).flatten():
                            solution_log.add_step(
                                (row, j),
                                _ACTION.format(int(candidate + 1)),
                                _REASON_ROW.format(
                                    row, *numpy.argwhere(stack[candidate, row, :] > 0).flatten()
                                )
                            )

                    done = True

            if rollback:
                if solution_log:
                    solution_log.rollback()
                stack[candidate, row, :] = initial_stack_row

        for col in range(9):
            initial_stack_col = initial_candidate_layer[:, col]

            done = False
            rollback = False
            if solution_log:
                solution_log.begin_transaction()

            for b in range(3):
                box_col = initial_stack_col[3*b:3*b+3]

                j1, j2 = find_box_coords(col)

                box_col_sum = box_col.sum()
                box_sum = initial_candidate_layer[3*b:3*b+3, j1:j2].flatten().sum()

                if box_col_sum == box_sum and box_col_sum / box_col.max() == 2:
                    if done:
                        rollback = True
                        break

                    stack[candidate, 0:3*b, col] = 0
                    stack[candidate, 3*b+3:9, col] = 0

                    if solution_log:
                        for i in numpy.argwhere(initial_candidate_layer[:, col] > stack[candidate, :, col]).flatten():
                            solution_log.add_step(
                                (i, col),
                                _ACTION.format(int(candidate + 1)),
                                _REASON_COL.format(
                                    col, *numpy.argwhere(stack[candidate, :, col] > 0).flatten()
                                )
                            )

                    done = True

            if rollback:
                if solution_log:
                    solution_log.rollback()
                stack[candidate, :, col] = initial_stack_col

    return
