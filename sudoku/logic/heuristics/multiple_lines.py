import itertools
import numpy

_bands = (numpy.arange(0, 3), numpy.arange(3, 6), numpy.arange(6, 9))


def process_multiple_lines(stack: numpy.array):
    for candidate, candidate_layer in enumerate(stack):
        _scan_row_bands_for_multiple_lines(candidate, candidate_layer)
        _scan_column_bands_for_multiple_lines(candidate, candidate_layer)


def _scan_column_bands_for_multiple_lines(candidate, candidate_layer):
    for cols in _bands:
        for row_box1, row_box2, row_box3 in itertools.permutations(_bands):
            scanned_indices = numpy.hstack((row_box1, row_box2))

            full_band = candidate_layer[scanned_indices[:, numpy.newaxis], cols]

            for i, j in itertools.combinations(cols, 2):
                sub_band = candidate_layer[scanned_indices[:, numpy.newaxis], (i, j)]

                if full_band.max() and full_band.sum() == sub_band.sum():
                    candidate_layer[row_box3[:, numpy.newaxis], (i, j)] = 0


def _scan_row_bands_for_multiple_lines(candidate, candidate_layer):
    for rows in _bands:
        for col_box1, col_box2, col_box3 in itertools.permutations(_bands):
            scanned_indices = numpy.hstack((col_box1, col_box2))

            full_band = candidate_layer[rows, scanned_indices[:, numpy.newaxis]]

            for i, j in itertools.combinations(rows, 2):
                sub_band = candidate_layer[(i, j), scanned_indices[:, numpy.newaxis]]

                if full_band.max() and full_band.sum() == sub_band.sum():
                    candidate_layer[(i, j), col_box3[:, numpy.newaxis]] = 0
