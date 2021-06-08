import unittest

import numpy

from sudoku.logic._solver import create_candidates_stack
from sudoku.logic.heuristics.multiple_lines import process_multiple_lines


class MultipleLineHeuristicTest(unittest.TestCase):
    def test_ProcessMultipleLines_CandidatesFormLinesAlongCols0And1_RemoveCandidatesInMiddleBox(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[4, :, :] = numpy.array([
            [5, 5, 0,    0, 0, 0,   0, 0, 0],
            [5, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [5, 0, 5,    0, 0, 0,   0, 0, 0],
            [0, 5, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [5, 0, 0,    0, 0, 0,   0, 0, 0],
            [5, 5, 0,    0, 0, 0,   0, 0, 0],
        ])

        expected = numpy.array([
            [5, 5, 0,    0, 0, 0,   0, 0, 0],
            [5, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 5,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [5, 0, 0,    0, 0, 0,   0, 0, 0],
            [5, 5, 0,    0, 0, 0,   0, 0, 0],
        ])

        process_multiple_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[4, :, :])

    def test_ProcessMultipleLines_CandidatesFormLinesAlongCols1And2_RemoveCandidatesInMiddleBox(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[4, :, :] = numpy.array([
            [0, 5, 5,    0, 0, 0,   0, 0, 0],
            [0, 0, 5,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [5, 0, 5,    0, 0, 0,   0, 0, 0],
            [0, 5, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 5, 0,    0, 0, 0,   0, 0, 0],
            [0, 5, 5,    0, 0, 0,   0, 0, 0],
        ])

        expected = numpy.array([
            [0, 5, 5,    0, 0, 0,   0, 0, 0],
            [0, 0, 5,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [5, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 5, 0,    0, 0, 0,   0, 0, 0],
            [0, 5, 5,    0, 0, 0,   0, 0, 0],
        ])

        process_multiple_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[4, :, :])

    def test_ProcessMultipleLines_CandidatesFormLinesAlongCols3And5_RemoveCandidatesInLastBox(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[4, :, :] = numpy.array([
            [0, 0, 0,   5, 0, 5,    0, 0, 0],
            [0, 0, 0,   0, 0, 5,    0, 0, 0],
            [0, 0, 0,   0, 0, 0,    0, 0, 0],

            [0, 0, 0,   0, 0, 0,    0, 0, 0],
            [0, 0, 0,   5, 0, 0,    0, 0, 0],
            [0, 0, 0,   0, 0, 5,    0, 0, 0],

            [0, 0, 0,   0, 0, 0,    0, 0, 0],
            [0, 0, 0,   5, 0, 5,    0, 0, 0],
            [0, 0, 0,   0, 5, 0,    0, 0, 0],
        ])

        expected = numpy.array([
            [0, 0, 0,   5, 0, 5,    0, 0, 0],
            [0, 0, 0,   0, 0, 5,    0, 0, 0],
            [0, 0, 0,   0, 0, 0,    0, 0, 0],

            [0, 0, 0,   0, 0, 0,    0, 0, 0],
            [0, 0, 0,   5, 0, 0,    0, 0, 0],
            [0, 0, 0,   0, 0, 5,    0, 0, 0],

            [0, 0, 0,   0, 0, 0,    0, 0, 0],
            [0, 0, 0,   0, 0, 0,    0, 0, 0],
            [0, 0, 0,   0, 5, 0,    0, 0, 0],
        ])

        process_multiple_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[4, :, :])

    def test_ProcessMultipleLines_CandidatesFormLinesAlongCols7And8Layer5_RemoveCandidatesInFirstBox(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[5, :, :] = numpy.array([
            [0, 0, 0,   0, 0, 0,    0, 6, 0],
            [0, 0, 0,   0, 0, 0,    6, 6, 6],
            [0, 0, 0,   0, 0, 0,    0, 0, 0],

            [0, 0, 0,   0, 0, 0,    0, 0, 6],
            [0, 0, 0,   0, 0, 0,    0, 6, 0],
            [0, 0, 0,   0, 0, 0,    0, 0, 0],

            [0, 0, 0,   0, 0, 0,    0, 6, 6],
            [0, 0, 0,   0, 0, 0,    0, 0, 0],
            [0, 0, 0,   0, 0, 0,    0, 0, 0],
        ])

        expected = numpy.array([
            [0, 0, 0,   0, 0, 0,    0, 0, 0],
            [0, 0, 0,   0, 0, 0,    6, 0, 0],
            [0, 0, 0,   0, 0, 0,    0, 0, 0],

            [0, 0, 0,   0, 0, 0,    0, 0, 6],
            [0, 0, 0,   0, 0, 0,    0, 6, 0],
            [0, 0, 0,   0, 0, 0,    0, 0, 0],

            [0, 0, 0,   0, 0, 0,    0, 6, 6],
            [0, 0, 0,   0, 0, 0,    0, 0, 0],
            [0, 0, 0,   0, 0, 0,    0, 0, 0],
        ])

        process_multiple_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[5, :, :])

    def test_ProcessMultipleLines_CandidatesFormLinesAlongRows7And8Layer5_RemoveCandidatesInFirstBox(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[5, :, :] = numpy.array([
            [6, 0, 0,   0, 6, 0,    0, 6, 0],
            [0, 6, 0,   6, 0, 0,    0, 6, 6],
            [0, 0, 6,   0, 0, 0,    0, 0, 0],

            [0, 0, 0,   0, 0, 0,    0, 0, 0],
            [0, 0, 0,   0, 0, 0,    0, 0, 0],
            [0, 0, 0,   0, 0, 0,    0, 0, 0],

            [0, 0, 0,   0, 0, 0,    0, 0, 0],
            [0, 0, 0,   0, 0, 0,    0, 0, 0],
            [0, 0, 0,   0, 0, 0,    0, 0, 0],
        ])

        expected = numpy.array([
            [0, 0, 0,   0, 6, 0,    0, 6, 0],
            [0, 0, 0,   6, 0, 0,    0, 6, 6],
            [0, 0, 6,   0, 0, 0,    0, 0, 0],

            [0, 0, 0,   0, 0, 0,    0, 0, 0],
            [0, 0, 0,   0, 0, 0,    0, 0, 0],
            [0, 0, 0,   0, 0, 0,    0, 0, 0],

            [0, 0, 0,   0, 0, 0,    0, 0, 0],
            [0, 0, 0,   0, 0, 0,    0, 0, 0],
            [0, 0, 0,   0, 0, 0,    0, 0, 0],
        ])

        process_multiple_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[5, :, :])