import numpy


def process_candidate_lines(stack: numpy.array, *args, **kwargs) -> None:
    for row in range(9):
        box_row = stack[3, row, 0:3]
        if box_row.sum() / box_row.max() == 2:
            stack[3, row, 3:9] = 0

    return