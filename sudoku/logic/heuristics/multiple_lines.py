import itertools
import numpy


def process_multiple_lines(stack: numpy.array):
    candidate_layer = stack[4, :, :]
    bands = (numpy.arange(0, 3), numpy.arange(3, 6), numpy.arange(6, 9))

    for b1, b2, b3 in itertools.permutations(bands):
        full_band = candidate_layer[numpy.array([b1, b2]).flatten(), 0:3]
        for i, j in itertools.combinations(range(3), 2):
            sub_band = full_band[:, (i, j)]

            if full_band.max() and full_band.sum() == sub_band.sum():
                candidate_layer[b3[:, numpy.newaxis], (i, j)] = 0



