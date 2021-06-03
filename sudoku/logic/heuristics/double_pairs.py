import itertools

import numpy

from sudoku.logic.utils.utils import assert_line_count


def process_double_pairs(stack: numpy.array) -> None:
    for candidate in range(9):
        candidate_layer = stack[candidate, :, :]
        bands = ((0, 3), (3, 6), (6, 9))

        for band in bands:
            for ids1, ids2, ids3 in itertools.permutations(bands):
                scan_box_lines(ids1, ids2, ids3, band, candidate_layer, extract_box_along_rows, scan_rows)
                scan_box_lines(ids1, ids2, ids3, band, candidate_layer, extract_box_along_columns, scan_columns)


def scan_box_lines(ids1, ids2, ids3, band, candidate_layer, extract_method, scan_method):
    first_box, second_box, third_box = extract_method(ids1, ids2, ids3, band, candidate_layer)

    if assert_line_count(first_box.flatten(), 2) and assert_line_count(second_box.flatten(), 2):
        for first_line, second_line, _ in itertools.permutations((0, 1, 2)):
            scan_method(ids1, ids2, ids3, first_line, second_line, first_box, second_box, third_box)


def extract_box_along_rows(ids1, ids2, ids3, band, candidate_layer):
    band_slice = slice(*band)
    first_box = candidate_layer[band_slice, slice(*ids1)]
    second_box = candidate_layer[band_slice, slice(*ids2)]
    third_box = candidate_layer[band_slice, slice(*ids3)]
    return first_box, second_box, third_box


def extract_box_along_columns(ids1, ids2, ids3, band, candidate_layer):
    band_slice = slice(*band)
    first_box = candidate_layer[slice(*ids1), band_slice]
    second_box = candidate_layer[slice(*ids2), band_slice]
    third_box = candidate_layer[slice(*ids3), band_slice]
    return first_box, second_box, third_box


def scan_rows(first_band, second_band, third_band, first_line_id, second_line_id, first_box, second_box, third_box):
    first_line = numpy.hstack((first_box[first_line_id, :], second_box[first_line_id, :]))
    second_line = numpy.hstack((first_box[second_line_id, :], second_box[second_line_id, :]))

    if assert_line_count(first_line, 2) and assert_line_count(second_line, 2):
        third_box[first_line_id, :] = 0
        third_box[second_line_id, :] = 0


def scan_columns(first_band, second_band, third_band, first_line_id, second_line_id, first_box, second_box, third_box):
    first_line = numpy.hstack((first_box[:, first_line_id], second_box[:, first_line_id]))
    second_line = numpy.hstack((first_box[:, second_line_id], second_box[:, second_line_id]))

    if assert_line_count(first_line, 2) and assert_line_count(second_line, 2):
        third_box[:, first_line_id] = 0
        third_box[:, second_line_id] = 0
