import itertools
import numpy


def process_multiple_lines(stack: numpy.array):
    candidate_layer = stack[4, :, :]
    bands = (numpy.arange(0, 3), numpy.arange(3, 6), numpy.arange(6, 9))

    for cols in bands:
        for row_box1, row_box2, row_box3 in itertools.permutations(bands):
            scanned_indices = numpy.hstack((row_box1, row_box2))

            full_band = candidate_layer[scanned_indices[:, numpy.newaxis], cols]

            for i, j in itertools.combinations(cols, 2):
                sub_band = candidate_layer[scanned_indices[:, numpy.newaxis], (i, j)]

                if full_band.max() and full_band.sum() == sub_band.sum():
                    candidate_layer[row_box3[:, numpy.newaxis], (i, j)] = 0


