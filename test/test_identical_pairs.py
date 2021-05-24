import unittest

from logic.heuristics.identical_pairs import process_identical_pairs
from logic._solver import *


class TestSolver(unittest.TestCase):
    def test_ProcessIdenticalPairs_FullStack_DoNothing(self):
        candidate_stack = create_candidates_stack()
        expected = candidate_stack

        process_identical_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack)

    def test_ProcessIdenticalPairs_NumbersOccurOnlyInPairs_DoNothing(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[4:6, :, 0] = numpy.array([
            [5, 5, 0,  0, 0, 0,  0, 0, 0],
            [6, 6, 0,  0, 0, 0,  0, 0, 0]
        ])

        expected = numpy.array([
            [5, 5, 0,  0, 0, 0,  0, 0, 0],
            [6, 6, 0,  0, 0, 0,  0, 0, 0]
        ])

        process_identical_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[4:6, :, 0])

    def test_ProcessIdenticalPairs_NumbersOccurOutsidePairs_WipeOthers(self):
        candidate_stack = numpy.zeros((9, 9, 9))
        candidate_stack[4:6, :, 0] = numpy.array([
            [5, 5, 0,  0, 5, 0,  0, 0, 0],
            [6, 6, 0,  0, 0, 0,  0, 0, 0]
        ])

        expected = numpy.array([
            [5, 5, 0,  0, 0, 0,  0, 0, 0],
            [6, 6, 0,  0, 0, 0,  0, 0, 0]
        ])

        process_identical_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[4:6, :, 0])

    def test_ProcessIdenticalPairs_PairInSecondRowNumbersOccurOutsidePairs_WipeOthers(self):
        candidate_stack = numpy.zeros((9, 9, 9))
        candidate_stack[4:6, :, 0] = numpy.array([
            [0, 5, 5,  0, 5, 0,  0, 0, 0],
            [0, 6, 6,  0, 0, 0,  0, 0, 0]
        ])

        expected = numpy.array([
            [0, 5, 5,  0, 0, 0,  0, 0, 0],
            [0, 6, 6,  0, 0, 0,  0, 0, 0]
        ])

        process_identical_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[4:6, :, 0])

    def test_ProcessIdenticalPairs_PairInFirstAndSecondRowNumbersOccurOutsidePair_WipeOthers(self):
        candidate_stack = numpy.zeros((9, 9, 9))
        candidate_stack[4:6, :, 0] = numpy.array([
            [5, 0, 5,  0, 5, 0,  0, 0, 0],
            [6, 0, 6,  0, 0, 0,  0, 0, 0]
        ])

        expected = numpy.array([
            [5, 0, 5,  0, 0, 0,  0, 0, 0],
            [6, 0, 6,  0, 0, 0,  0, 0, 0]
        ])

        process_identical_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[4:6, :, 0])

    def test_ProcessIdenticalPairs_TripletOccursInBox_DoNothing(self):
        candidate_stack = numpy.zeros((9, 9, 9))
        candidate_stack[4:6, :, 0] = numpy.array([
            [5, 5, 5,  0, 5, 0,  0, 0, 0],
            [6, 6, 6,  0, 0, 0,  0, 0, 0]
        ])

        expected = numpy.array([
            [5, 5, 5,  0, 5, 0,  0, 0, 0],
            [6, 6, 6,  0, 0, 0,  0, 0, 0]
        ])

        process_identical_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[4:6, :, 0])

    def test_ProcessIdenticalPairs_PairNotInOneBox_DoNothing(self):
        candidate_stack = numpy.zeros((9, 9, 9))
        candidate_stack[4:6, :, 0] = numpy.array([
            [5, 0, 5,  0, 5, 0,  0, 0, 0],
            [6, 0, 0,  6, 6, 0,  0, 0, 0]
        ])

        expected = numpy.array([
            [5, 0, 5,  0, 5, 0,  0, 0, 0],
            [6, 0, 0,  6, 6, 0,  0, 0, 0]
        ])

        process_identical_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[4:6, :, 0])

    def test_ProcessIdenticalPairs_PairInFourthAndFifthRowNumbersOutsidePairExist_WipeOthers(self):
        candidate_stack = numpy.zeros((9, 9, 9))
        candidate_stack[4:6, :, 0] = numpy.array([
            [5, 0, 5,  5, 5, 0,  0, 0, 0],
            [6, 0, 0,  6, 6, 0,  0, 0, 0]
        ])

        expected = numpy.array([
            [0, 0, 0,  5, 5, 0,  0, 0, 0],
            [0, 0, 0,  6, 6, 0,  0, 0, 0]
        ])

        process_identical_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[4:6, :, 0])

    def test_ProcessIdenticalPairs_TwoPairsExistsAndNumbersOutsidePairExist_DoNothing(self):
        candidate_stack = numpy.zeros((9, 9, 9))
        candidate_stack[4:6, :, 0] = numpy.array([
            [5, 0, 5,  5, 5, 0,  0, 0, 5],
            [6, 0, 6,  6, 6, 0,  6, 0, 0]
        ])

        expected = numpy.array([
            [5, 0, 5,  5, 5, 0,  0, 0, 5],
            [6, 0, 6,  6, 6, 0,  6, 0, 0]
        ])

        process_identical_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[4:6, :, 0])

    def test_ProcessIdenticalPairs_PairInFourthAndFifthRowAndFourthColumnNumbersOutsidePairExist_WipeOthers(self):
        candidate_stack = numpy.zeros((9, 9, 9))
        candidate_stack[4:6, :, 4] = numpy.array([
            [5, 0, 5,  5, 5, 0,  0, 0, 0],
            [6, 0, 0,  6, 6, 0,  0, 0, 0]
        ])

        expected = numpy.array([
            [0, 0, 0,  5, 5, 0,  0, 0, 0],
            [0, 0, 0,  6, 6, 0,  0, 0, 0]
        ])

        process_identical_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[4:6, :, 4])

    @staticmethod
    def assertNumpyEqual(first: numpy.array, second: numpy):
        numpy.testing.assert_equal(first, second)

