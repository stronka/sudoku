import unittest

import numpy

from sudoku.logic._solver import create_candidates_stack
from sudoku.logic.heuristics.multiple_lines import process_multiple_lines
from sudoku.logic.meta.solution_log import SolutionLog


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

    def test_ProcessMultipleLines_CandidatesFormLinesAlongRows7And8Layer5_LogSolution(self):
        candidate_stack = create_candidates_stack()
        solution_log = SolutionLog()
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

        expected = [
            {
                'cell': (0, 0),
                'action': "Remove 6",
                'reason': "Multiple lines: candidates form lines along rows 0 and 1"
            },
            {
                'cell': (1, 1),
                'action': "Remove 6",
                'reason': "Multiple lines: candidates form lines along rows 0 and 1"
            },
        ]

        process_multiple_lines(candidate_stack, solution_log=solution_log)
        self.assertListEqual(expected, solution_log.get_steps())

    def test_ProcessMultipleLines_CandidatesFormLinesAlongCols3And5_LogSolution(self):
        candidate_stack = create_candidates_stack()
        solution_log = SolutionLog()
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

        expected = [
            {
                'cell': (7, 3),
                'action': "Remove 5",
                'reason': "Multiple lines: candidates form lines along columns 3 and 5"
            },
            {
                'cell': (7, 5),
                'action': "Remove 5",
                'reason': "Multiple lines: candidates form lines along columns 3 and 5"
            },
        ]

        process_multiple_lines(candidate_stack, solution_log=solution_log)
        self.assertListEqual(expected, solution_log.get_steps())
