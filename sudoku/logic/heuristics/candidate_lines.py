import copy

import numpy


def process_candidate_lines(stack: numpy.array, *args, **kwargs) -> None:
    for candidate in range(9):
        for row in range(9):

            done = False
            rollback = False
            initial_stack_row = copy.copy(stack[candidate, row, :])

            for b in range(3):
                box_row = initial_stack_row[3*b:3*b+3]

                if box_row.sum() / box_row.max() == 2:
                    if done:
                        rollback = True
                        break

                    stack[candidate, row, 0:3*b] = 0
                    stack[candidate, row, 3*b+3:9] = 0
                    done = True

            if rollback:
                stack[candidate, row, :] = initial_stack_row

        for col in range(9):

            done = False
            rollback = False
            initial_stack_col = copy.copy(stack[candidate, :, col])

            for b in range(3):
                box_col = initial_stack_col[3*b:3*b+3]

                if box_col.sum() / box_col.max() == 2:
                    if done:
                        rollback = True
                        break

                    stack[candidate, 0:3*b, col] = 0
                    stack[candidate, 3*b+3:9, col] = 0
                    done = True

            if rollback:
                stack[candidate, :, col] = initial_stack_col

    return
