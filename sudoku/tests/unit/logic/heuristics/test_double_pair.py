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

    def test_DoublePairs_DoublePairsInRowsZeroAndFive_WipeAlongStack(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[1, :, :] = numpy.array([
            [0, 0, 0,    2, 0, 2,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    2, 0, 2,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 2, 2,   0, 0, 0],
            [0, 0, 0,    2, 2, 2,   0, 0, 0],
        ])

        expected = numpy.array([
            [0, 0, 0,    2, 0, 2,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    2, 0, 2,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 2, 0,   0, 0, 0],
            [0, 0, 0,    0, 2, 0,   0, 0, 0],
        ])

        process_double_pairs(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[1, :, :])

    def test_DoublePairs_DoublePairsInRowsZeroAndFiveColumnsThreeAndFour_WipeAlongStack(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[1, :, :] = numpy.array([
            [0, 0, 0,    2, 2, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    2, 2, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 2, 2,   0, 0, 0],
            [0, 0, 0,    2, 2, 2,   0, 0, 0],
        ])

        expected = numpy.array([
            [0, 0, 0,    2, 2, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    2, 2, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 2,   0, 0, 0],
            [0, 0, 0,    0, 0, 2,   0, 0, 0],
        ])

        process_double_pairs(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[1, :, :])

    def test_DoublePairs_DoublePairsInRowsZeroAndFiveColumnsFourAndFive_WipeAlongStack(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[1, :, :] = numpy.array([
            [0, 0, 0,    0, 2, 2,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 2, 2,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 2, 2,   0, 0, 0],
            [0, 0, 0,    2, 2, 2,   0, 0, 0],
        ])

        expected = numpy.array([
            [0, 0, 0,    0, 2, 2,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 2, 2,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    2, 0, 0,   0, 0, 0],
        ])

        process_double_pairs(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[1, :, :])

    def test_DoublePairs_DoublePairsInRowsZeroAndEightColumnsFourAndFive_WipeAlongStack(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[1, :, :] = numpy.array([
            [0, 0, 0,    0, 2, 2,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 2, 0,   0, 0, 0],
            [0, 0, 0,    0, 2, 2,   0, 0, 0],
            [0, 0, 0,    2, 2, 2,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 2, 2,   0, 0, 0],
        ])

        expected = numpy.array([
            [0, 0, 0,    0, 2, 2,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    2, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 2, 2,   0, 0, 0],
        ])

        process_double_pairs(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[1, :, :])


    def test_DoublePairs_DoublePairsInRowsZeroAndEightColumnsSevenAndEight_WipeAlongStack(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[1, :, :] = numpy.array([
            [0, 0, 0,    0, 0, 0,   0, 2, 2],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 2, 0],
            [0, 0, 0,    0, 0, 0,   0, 2, 2],
            [0, 0, 0,    0, 0, 0,   2, 2, 2],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 2, 2],
        ])

        expected = numpy.array([
            [0, 0, 0,    0, 0, 0,   0, 2, 2],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   2, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 2, 2],
        ])

        process_double_pairs(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[1, :, :])

    def test_DoublePairs_DoublePairsInRowsZeroAndEightColumnsSevenAndEightLayerTwo_WipeAlongStack(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[2, :, :] = numpy.array([
            [0, 0, 0,    0, 0, 0,   0, 3, 3],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 3, 0],
            [0, 0, 0,    0, 0, 0,   0, 3, 3],
            [0, 0, 0,    0, 0, 0,   3, 3, 3],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 3, 3],
        ])

        expected = numpy.array([
            [0, 0, 0,    0, 0, 0,   0, 3, 3],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   3, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 3, 3],
        ])

        process_double_pairs(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[2, :, :])