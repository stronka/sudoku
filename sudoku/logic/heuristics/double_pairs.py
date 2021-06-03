import numpy

from sudoku.logic.utils.utils import assert_line_count


def process_double_pairs(stack: numpy.array) -> None:
    candidate_layer = stack[1, :, :]
    top_box = candidate_layer[0:3, 3:6]
    mid_box = candidate_layer[3:6, 3:6]
    bottom_box = candidate_layer[6:9, 3:6]

    if assert_line_count(top_box.flatten(), 2):
        if assert_line_count(mid_box.flatten(), 2):
            first_line = numpy.hstack((top_box[:, 0], mid_box[:, 0]))
            third_line = numpy.hstack((top_box[:, 2], mid_box[:, 2]))
            if assert_line_count(first_line, 2) and assert_line_count(third_line, 2):
                bottom_box[:, 0] = 0
                bottom_box[:, 2] = 0
    #
    # stack[1, :, :] = numpy.array([
    #     [0, 0, 0,    2, 0, 2,   0, 0, 0],
    #     [0, 0, 0,    0, 0, 0,   0, 0, 0],
    #     [0, 0, 0,    0, 0, 0,   0, 0, 0],
    #
    #     [0, 0, 0,    0, 0, 0,   0, 0, 0],
    #     [0, 0, 0,    2, 0, 2,   0, 0, 0],
    #     [0, 0, 0,    0, 0, 0,   0, 0, 0],
    #
    #     [0, 0, 0,    0, 0, 0,   0, 0, 0],
    #     [0, 0, 0,    0, 2, 0,   0, 0, 0],
    #     [0, 0, 0,    0, 2, 0,   0, 0, 0],
    # ])
