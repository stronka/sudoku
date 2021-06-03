import unittest

import numpy

from sudoku.logic._solver import create_candidates_stack
from sudoku.logic.heuristics.double_pairs import process_double_pairs
from sudoku.logic.meta.solution_log import SolutionLog


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

    def test_DoublePairs_DoublePairsInRow_WipeAlongStack(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[2, :, :] = numpy.array([
            [3, 3, 0,    0, 3, 0,   0, 3, 0],
            [0, 3, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 3, 0,   0, 3, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
        ])

        expected = numpy.array([
            [0, 0, 0,    0, 3, 0,   0, 3, 0],
            [0, 3, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 3, 0,   0, 3, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
        ])

        process_double_pairs(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[2, :, :])

    def test_DoublePairs_DoublePairsInRow_LogSolution(self):
        candidate_stack = create_candidates_stack()
        solution_log = SolutionLog()
        candidate_stack[2, :, :] = numpy.array([
            [3, 0, 0,    0, 3, 0,   0, 3, 0],
            [0, 3, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 3, 0,   0, 3, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
        ])

        expected = [
            {
                'cell': (0, 0),
                'action': "Remove 3",
                'reason': "Double pair: candidates in cells (0, 4), (0, 7), (2, 4), (2, 7) form a line along row 0."},
        ]

        process_double_pairs(candidate_stack, solution_log=solution_log)
        self.assertListEqual(expected, solution_log.get_steps())

    def test_DoublePairs_DoublePairsInRowLayerThree_LogSolution(self):
        candidate_stack = create_candidates_stack()
        solution_log = SolutionLog()
        candidate_stack[3, :, :] = numpy.array([
            [4, 0, 0,    0, 4, 0,   0, 4, 0],
            [0, 4, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 4, 0,   0, 4, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
        ])

        expected = [
            {
                'cell': (0, 0),
                'action': "Remove 4",
                'reason': "Double pair: candidates in cells (0, 4), (0, 7), (2, 4), (2, 7) form a line along row 0."},
        ]

        process_double_pairs(candidate_stack, solution_log=solution_log)
        self.assertListEqual(expected, solution_log.get_steps())

    def test_DoublePairs_DoublePairsInRowLayerThree_LogSolutionInRowTwo(self):
        candidate_stack = create_candidates_stack()
        solution_log = SolutionLog()
        candidate_stack[3, :, :] = numpy.array([
            [0, 0, 0,    0, 4, 0,   0, 4, 0],
            [0, 4, 0,    0, 0, 0,   0, 0, 0],
            [4, 0, 0,    0, 4, 0,   0, 4, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
        ])

        expected = [
            {
                'cell': (2, 0),
                'action': "Remove 4",
                'reason': "Double pair: candidates in cells (0, 4), (0, 7), (2, 4), (2, 7) form a line along row 2."},
        ]

        process_double_pairs(candidate_stack, solution_log=solution_log)
        self.assertListEqual(expected, solution_log.get_steps())

    def test_DoublePairs_DoublePairsInRowSecondBoxWipedLayerThree_LogSolutionInRowTwo(self):
        candidate_stack = create_candidates_stack()
        solution_log = SolutionLog()
        candidate_stack[3, :, :] = numpy.array([
            [4, 0, 0,    0, 0, 0,   0, 4, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [4, 0, 0,    0, 4, 0,   0, 4, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
        ])

        expected = [
            {
                'cell': (2, 4),
                'action': "Remove 4",
                'reason': "Double pair: candidates in cells (0, 0), (0, 7), (2, 0), (2, 7) form a line along row 2."},
        ]

        process_double_pairs(candidate_stack, solution_log=solution_log)
        self.assertListEqual(expected, solution_log.get_steps())

    def test_DoublePairs_DoublePairsInRowSecondBandThirdBoxWipedLayerThree_LogSolutionInRowTwo(self):
        candidate_stack = create_candidates_stack()
        solution_log = SolutionLog()
        candidate_stack[3, :, :] = numpy.array([
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [4, 0, 0,    0, 4, 0,   0, 4, 0],
            [4, 0, 0,    0, 4, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],


            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
        ])

        expected = [
            {
                'cell': (3, 7),
                'action': "Remove 4",
                'reason': "Double pair: candidates in cells (3, 0), (3, 4), (4, 0), (4, 4) form a line along row 3."},
        ]

        process_double_pairs(candidate_stack, solution_log=solution_log)
        self.assertListEqual(expected, solution_log.get_steps())

    def test_DoublePairs_RemoveAlongColumnInBandTwoBoxThree_LogSolution(self):
        candidate_stack = create_candidates_stack()
        solution_log = SolutionLog()
        candidate_stack[1, :, :] = numpy.array([
            [0, 0, 0,    2, 0, 2,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    2, 0, 2,   0, 0, 0],
            [0, 0, 0,    0, 0, 0,   0, 0, 0],

            [0, 0, 0,    0, 0, 0,   0, 0, 0],
            [0, 0, 0,    0, 2, 0,   0, 0, 0],
            [0, 0, 0,    2, 2, 2,   0, 0, 0],
        ])

        expected = [
            {
                'cell': (8, 3),
                'action': "Remove 2",
                'reason': "Double pair: candidates in cells (0, 3), (4, 3), (0, 5), (4, 5) form a line along column 3."
            },
            {
                'cell': (8, 5),
                'action': "Remove 2",
                'reason': "Double pair: candidates in cells (0, 3), (4, 3), (0, 5), (4, 5) form a line along column 5."
            },
        ]

        process_double_pairs(candidate_stack, solution_log=solution_log)
        self.assertListEqual(expected, solution_log.get_steps())
