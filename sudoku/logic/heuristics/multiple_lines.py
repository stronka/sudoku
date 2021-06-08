import copy
import itertools
import numpy

_ACTION = "Remove {}"
_REASON_ROWS = "Multiple lines: candidates form lines along columns {} and {}"
_REASON_COLS = "Multiple lines: candidates form lines along rows {} and {}"

_bands = (numpy.arange(0, 3), numpy.arange(3, 6), numpy.arange(6, 9))


def process_multiple_lines(stack: numpy.array, **kwargs):
    for candidate, candidate_layer in enumerate(stack):
        _scan_row_bands_for_multiple_lines(candidate, candidate_layer, kwargs.setdefault('solution_log', None))
        _scan_column_bands_for_multiple_lines(candidate, candidate_layer, kwargs.setdefault('solution_log', None))


def _scan_column_bands_for_multiple_lines(candidate, candidate_layer, solution_log):
    for cols in _bands:
        for row_box1, row_box2, row_box3 in itertools.permutations(_bands):
            box1 = candidate_layer[row_box1[:, numpy.newaxis], cols]
            box2 = candidate_layer[row_box2[:, numpy.newaxis], cols]

            if not (box1.any() and box2.any()):
                continue

            scanned_indices = numpy.hstack((row_box1, row_box2))
            full_band = candidate_layer[scanned_indices[:, numpy.newaxis], cols]

            for i, j in itertools.combinations(cols, 2):
                sub_band = candidate_layer[scanned_indices[:, numpy.newaxis], (i, j)]

                if full_band.max() and full_band.sum() == sub_band.sum():
                    layer_before = copy.copy(candidate_layer)
                    candidate_layer[row_box3[:, numpy.newaxis], (i, j)] = 0

                    if solution_log:
                        _log_solution_steps(_REASON_ROWS, candidate, candidate_layer, i, j, layer_before, solution_log)


def _scan_row_bands_for_multiple_lines(candidate, candidate_layer, solution_log):
    for rows in _bands:
        for col_box1, col_box2, col_box3 in itertools.permutations(_bands):
            box1 = candidate_layer[rows, col_box1[:, numpy.newaxis]]
            box2 = candidate_layer[rows, col_box2[:, numpy.newaxis]]

            if not (box1.any() and box2.any()):
                continue

            scanned_indices = numpy.hstack((col_box1, col_box2))
            full_band = candidate_layer[rows, scanned_indices[:, numpy.newaxis]]

            for i, j in itertools.combinations(rows, 2):
                sub_band = candidate_layer[(i, j), scanned_indices[:, numpy.newaxis]]

                if full_band.max() and full_band.sum() == sub_band.sum():
                    layer_before = copy.copy(candidate_layer)
                    candidate_layer[(i, j), col_box3[:, numpy.newaxis]] = 0

                    if solution_log:
                        _log_solution_steps(_REASON_COLS, candidate, candidate_layer, i, j, layer_before, solution_log)


def _log_solution_steps(reason, candidate, candidate_layer, i, j, layer_before, solution_log):
    removed = numpy.nonzero(layer_before - candidate_layer)

    for cell in zip(removed[0], removed[1]):
        solution_log.add_step(cell, _ACTION.format(candidate + 1), reason.format(i, j))
