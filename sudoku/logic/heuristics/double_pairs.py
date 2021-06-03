import itertools

import numpy

from sudoku.logic.utils.utils import assert_line_count


def process_double_pairs(stack: numpy.array) -> None:
    for candidate in range(9):
        candidate_layer = stack[candidate, :, :]
        bands = ((0, 3), (3, 6), (6, 9))

        for band in bands:
            for ids1, ids2, ids3 in itertools.permutations(bands):
                scan_boxes_rowwise(ids1, ids2, ids3, band, candidate_layer)
                scan_boxes_columnwise(ids1, ids2, ids3, band, candidate_layer)


def scan_rows(id1, id2, top_box, mid_box, bottom_box):
    first_line = numpy.hstack((top_box[id1, :], mid_box[id1, :]))
    second_line = numpy.hstack((top_box[id2, :], mid_box[id2, :]))

    if assert_line_count(first_line, 2) and assert_line_count(second_line, 2):
        bottom_box[id1, :] = 0
        bottom_box[id2, :] = 0


def scan_columns(id1, id2, top_box, mid_box, bottom_box):
    first_line = numpy.hstack((top_box[:, id1], mid_box[:, id1]))
    second_line = numpy.hstack((top_box[:, id2], mid_box[:, id2]))

    if assert_line_count(first_line, 2) and assert_line_count(second_line, 2):
        bottom_box[:, id1] = 0
        bottom_box[:, id2] = 0
