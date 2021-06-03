import itertools

import numpy

from sudoku.logic.utils.utils import assert_line_count

_ACTION = "Remove {}"

_REASON_ROW = "Double pair: candidates in cells ({0}, {2}), ({0}, {3}), ({1}, {2}), ({1}, {3}) form a line along row {4}."
_REASON_COL = "Double pair: candidates in cells ({2}, {0}), ({3}, {0}), ({2}, {1}), ({3}, {1}) form a line along column {4}."


def process_double_pairs(stack: numpy.array, *args, **kwargs) -> None:
    solution_log = kwargs.setdefault('solution_log', None)

    for candidate in range(9):
        candidate_layer = stack[candidate, :, :]
        bands = ((0, 3), (3, 6), (6, 9))

        for band in bands:
            for ids1, ids2, ids3 in itertools.permutations(bands):
                _scan_box_lines(candidate, ids1, ids2, ids3, band, candidate_layer, solution_log, _extract_box_along_rows, _scan_line_across_rows)
                _scan_box_lines(candidate, ids1, ids2, ids3, band, candidate_layer, solution_log, _extract_box_along_columns, _scan_across_columns)


def _scan_box_lines(candidate, ids1, ids2, ids3, band, candidate_layer, solution_log, extract_method, scan_method):
    first_box, second_box, third_box = extract_method(ids1, ids2, ids3, band, candidate_layer)

    if assert_line_count(first_box.flatten(), 2) and assert_line_count(second_box.flatten(), 2):
        for first_line, second_line, _ in itertools.permutations((0, 1, 2)):
            scan_method(candidate, band, ids1, ids2, ids3, first_line, second_line, first_box, second_box, third_box, solution_log)


def _extract_box_along_rows(ids1, ids2, ids3, band, candidate_layer):
    band_slice = slice(*band)
    first_box = candidate_layer[band_slice, slice(*ids1)]
    second_box = candidate_layer[band_slice, slice(*ids2)]
    third_box = candidate_layer[band_slice, slice(*ids3)]
    return first_box, second_box, third_box


def _extract_box_along_columns(ids1, ids2, ids3, band, candidate_layer):
    band_slice = slice(*band)
    first_box = candidate_layer[slice(*ids1), band_slice]
    second_box = candidate_layer[slice(*ids2), band_slice]
    third_box = candidate_layer[slice(*ids3), band_slice]
    return first_box, second_box, third_box


def _scan_line_across_rows(candidate, row_band, first_band, second_band, third_band, first_line_id, second_line_id, first_box, second_box, third_box, solution_log):
    first_line = numpy.hstack((first_box[first_line_id, :], second_box[first_line_id, :]))
    second_line = numpy.hstack((first_box[second_line_id, :], second_box[second_line_id, :]))

    if assert_line_count(first_line, 2) and assert_line_count(second_line, 2):
        nonzeros_first_line = numpy.argwhere(third_box[first_line_id, :] != 0)
        third_box[first_line_id, nonzeros_first_line] = 0

        nonzeros_second_line = numpy.argwhere(third_box[second_line_id, :] != 0)
        third_box[second_line_id, nonzeros_second_line] = 0

        if solution_log:
            global_first_line_id = row_band[0] + first_line_id
            global_second_line_id = row_band[0] + second_line_id
            global_first_pair_col_id = first_band[0] + first_box[first_line_id, :].nonzero()[0][0]
            global_second_pair_col_id = second_band[0] + second_box[first_line_id, :].nonzero()[0][0]

            _log_row_remove(solution_log, candidate, global_first_line_id, nonzeros_first_line, global_first_line_id,
                            global_first_pair_col_id, global_second_line_id, global_second_pair_col_id, third_band)

            _log_row_remove(solution_log, candidate, global_second_line_id, nonzeros_second_line, global_first_line_id,
                            global_first_pair_col_id, global_second_line_id, global_second_pair_col_id, third_band)


def _log_row_remove(solution_log, candidate, removed_line_id, nonzeros_first_line, global_first_line_id,
                    global_first_pair_col_id, global_second_line_id, global_second_pair_col_id, third_band):
    for _id in nonzeros_first_line:
        global_removed_id = third_band[0] + _id[0]

        fmt_reason = _REASON_ROW.format(global_first_line_id, global_second_line_id, global_first_pair_col_id,
                                        global_second_pair_col_id, removed_line_id)

        solution_log.add_step(
            (removed_line_id, global_removed_id), _ACTION.format(int(candidate + 1)), fmt_reason
        )


def _scan_across_columns(candidate, col_band, first_band, second_band, third_band, first_line_id, second_line_id, first_box, second_box, third_box, solution_log):
    first_line = numpy.hstack((first_box[:, first_line_id], second_box[:, first_line_id]))
    second_line = numpy.hstack((first_box[:, second_line_id], second_box[:, second_line_id]))

    if assert_line_count(first_line, 2) and assert_line_count(second_line, 2):
        nonzeros_first_line = numpy.argwhere(third_box[:, first_line_id] != 0)
        third_box[nonzeros_first_line, first_line_id] = 0

        nonzeros_second_line = numpy.argwhere(third_box[:, second_line_id] != 0)
        third_box[nonzeros_second_line, second_line_id] = 0

        if solution_log:
            global_first_line_id = col_band[0] + first_line_id
            global_second_line_id = col_band[0] + second_line_id
            global_first_pair_row_id = first_band[0] + first_box[:, first_line_id].nonzero()[0][0]
            global_second_pair_row_id = second_band[0] + second_box[:, first_line_id].nonzero()[0][0]

            _log_col_remove(solution_log, candidate, global_first_line_id, nonzeros_first_line, global_first_line_id,
                            global_first_pair_row_id, global_second_line_id, global_second_pair_row_id, third_band)

            _log_col_remove(solution_log, candidate, global_second_line_id, nonzeros_second_line, global_first_line_id,
                            global_first_pair_row_id, global_second_line_id, global_second_pair_row_id, third_band)


def _log_col_remove(solution_log, candidate, removed_line_id, nonzeros_first_line, global_first_line_id,
                    global_first_pair_row_id, global_second_line_id, global_second_pair_row_id, third_band):
    for _id in nonzeros_first_line:
        global_removed_id = third_band[0] + _id[0]

        fmt_reason = _REASON_COL.format(global_first_line_id, global_second_line_id, global_first_pair_row_id,
                                        global_second_pair_row_id, removed_line_id)

        solution_log.add_step(
            (global_removed_id, removed_line_id), _ACTION.format(int(candidate + 1)), fmt_reason
        )