import numpy

_ACTION = "Remove {}"
_REASON_ROW = "Last position in row: Cell ({}, {}) is last possible location for number {}"
_REASON_COL = "Last position in column: Cell ({}, {}) is last possible location for number {}"


def process_last_elements(stack: numpy.array, *args, **kwargs) -> None:
    solution_log = kwargs.setdefault('solution_log', None)

    for k in range(0, 9):
        for i in range(0, 9):
            row = stack[k, i, :]
            if row.sum() and row.sum()/row.max() == 1:
                ind = numpy.nonzero(row)[0]
                number = int(k+1)

                log_solution_steps(solution_log, number, (i, ind[0]), _REASON_ROW)

                stack[:, i, ind] = 0
                stack[k, i, ind] = number

        for j in range(0, 9):
            col = stack[k, :, j]
            if col.sum() and col.sum()/col.max() == 1:
                ind = numpy.nonzero(col)[0]
                number = int(k+1)

                log_solution_steps(solution_log, number, (ind[0], j), _REASON_COL)

                stack[:, ind, j] = 0
                stack[k, ind, j] = number
    return


def log_solution_steps(solution, number, cell, reason):
    if solution:
        for candidate in range(1, 10):
            if candidate != number:
                solution.add_step(cell, _ACTION.format(candidate), reason.format(cell[0], cell[1], number))
