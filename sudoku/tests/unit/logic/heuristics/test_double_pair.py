import unittest

import numpy

from sudoku.logic._solver import create_candidates_stack
from sudoku.logic.heuristics.double_pairs import process_double_pairs


class TestDoublePairHeuristic(unittest.TestCase):
    def test_processDoublePairs_DoublePairPresent_WipeAlongDoublePairLines(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[1, :, :] = numpy.array([
            [0, 0, 0,    2, 0, 2,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    2, 0, 2,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 2, 2,   0, 0, 0],
            [0, 0, 0,    2, 2, 2,   0, 0, 0],
        ])

        expected = numpy.array([
            [0, 0, 0,    2, 0, 2,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    2, 0, 2,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 2, 0,   0, 0, 0],
            [0, 0, 0,    0, 2, 0,   0, 0, 0],
        ])

        process_double_pairs(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[1, :, :])
