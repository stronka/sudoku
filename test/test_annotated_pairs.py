import unittest

from logic.heuristics.identical_pairs import process_identical_pairs
from logic._solver import *


class TestAnnotatedPairsHeuristic(unittest.TestCase):
    def test_ProcessAnnotatedPairs_FullStack_DoNothing(self):
        candidate_stack = create_candidates_stack()
        expected = candidate_stack

        process_annotated_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack)

    def test_ProcessAnnotatedPairs_OnlyPairsIncolumn_DoNothing(self):
        candidate_stack = numpy.zeros((9, 9, 9))
        candidate_stack[4, 0:2, 0] = 5
        candidate_stack[5, 0:2, 0] = 6

        expected = numpy.array([
            [0, 0, 0,  0, 5, 6,  0, 0, 0],
            [0, 0, 0,  0, 5, 6,  0, 0, 0],
        ]).transpose()

        process_annotated_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 0:2, 0])

    def test_ProcessAnnotatedPairs_OtherNumbersWithPairedColumn_WipeNonPairs(self):
        candidate_stack = numpy.zeros((9, 9, 9))
        candidate_stack[4, 0:2, 0] = 5
        candidate_stack[5, 0:2, 0] = 6
        candidate_stack[6, 0, 0] = 7

        expected = numpy.array([
            [0, 0, 0,  0, 5, 6,  0, 0, 0],
            [0, 0, 0,  0, 5, 6,  0, 0, 0],
        ]).transpose()

        process_annotated_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 0:2, 0])

    def test_ProcessAnnotatedPairs_OtherNumbersWithPairedColumnPairInSecondRow_WipeNonPairs(self):
        candidate_stack = numpy.zeros((9, 9, 9))
        candidate_stack[4, 1:3, 0] = 5
        candidate_stack[5, 1:3, 0] = 6
        candidate_stack[6, 1, 0] = 7

        expected = numpy.array([
            [0, 0, 0,  0, 5, 6,  0, 0, 0],
            [0, 0, 0,  0, 5, 6,  0, 0, 0],
        ]).transpose()

        process_annotated_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 1:3, 0])

    def test_ProcessAnnotatedPairs_OtherNumbersWithPairedColumnPairInSecondRowSecondColumn_WipeNonPairs(self):
        candidate_stack = numpy.zeros((9, 9, 9))
        candidate_stack[4, 1:3, 1] = 5
        candidate_stack[5, 1:3, 1] = 6
        candidate_stack[6, 1, 1] = 7

        expected = numpy.array([
            [0, 0, 0,  0, 5, 6,  0, 0, 0],
            [0, 0, 0,  0, 5, 6,  0, 0, 0],
        ]).transpose()

        process_annotated_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 1:3, 1])

    def test_ProcessAnnotatedPairs_PairSpansAlongBoxes_DoNothing(self):
        candidate_stack = numpy.zeros((9, 9, 9))
        candidate_stack[4, 2:4, 1] = 5
        candidate_stack[5, 2:4, 1] = 6
        candidate_stack[6, 2, 1] = 7

        expected = numpy.array([
            [0, 0, 0,  0, 5, 6,  7, 0, 0],
            [0, 0, 0,  0, 5, 6,  0, 0, 0],
        ]).transpose()

        process_annotated_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 2:4, 1])

    def test_ProcessAnnotatedPairs_PairInSecondBox_WipeOthers(self):
        candidate_stack = numpy.zeros((9, 9, 9))
        candidate_stack[4, 3:5, 1] = 5
        candidate_stack[5, 3:5, 1] = 6
        candidate_stack[6, 3, 1] = 7

        expected = numpy.array([
            [0, 0, 0,  0, 5, 6,  0, 0, 0],
            [0, 0, 0,  0, 5, 6,  0, 0, 0],
        ]).transpose()

        process_annotated_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 3:5, 1])

    def test_ProcessAnnotatedPairs_AlongRow_WipeOthers(self):
        candidate_stack = numpy.zeros((9, 9, 9))
        candidate_stack[4, 1, 3:5] = 5
        candidate_stack[5, 1, 3:5] = 6
        candidate_stack[6, 1, 3] = 7

        expected = numpy.array([
            [0, 0, 0,  0, 5, 6,  0, 0, 0],
            [0, 0, 0,  0, 5, 6,  0, 0, 0],
        ]).transpose()

        process_annotated_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 1, 3:5])

    def test_ProcessAnnotatedPairs_AlongRowSpansTwoBoxes_DoNothing(self):
        candidate_stack = numpy.zeros((9, 9, 9))
        candidate_stack[4, 1, 2:4] = 5
        candidate_stack[5, 1, 2:4] = 6
        candidate_stack[6, 1, 2] = 7

        expected = numpy.array([
            [0, 0, 0,  0, 5, 6,  7, 0, 0],
            [0, 0, 0,  0, 5, 6,  0, 0, 0],
        ]).transpose()

        process_annotated_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 1, 2:4])

    def test_ProcessAnnotatedPairs_AlongRowOneElementIsPresentMoreThanTwiceInRow_DoNothing(self):
        candidate_stack = numpy.zeros((9, 9, 9))
        candidate_stack[4, 1, 3:6] = 5
        candidate_stack[5, 1, 3:5] = 6
        candidate_stack[6, 1, 3] = 7

        expected = numpy.array([
            [0, 0, 0,  0, 5, 6,  7, 0, 0],
            [0, 0, 0,  0, 5, 6,  0, 0, 0],
        ]).transpose()

        process_annotated_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 1, 3:5])

    def test_ProcessAnnotatedPairs_PairInSecondRowMidBoxFirstAndSecondColumnHorizontally_WipeOthers(self):
        candidate_stack = numpy.zeros((9, 9, 9))
        candidate_stack[:, 1, 3:6] = numpy.array([
            [0, 0, 0,  0, 5, 6,  7, 0, 0],
            [0, 0, 0,  0, 5, 6,  0, 0, 0],
            [0, 0, 0,  0, 0, 0,  0, 0, 0],
        ]).transpose()

        expected = numpy.array([
            [0, 0, 0,  0, 5, 6,  0, 0, 0],
            [0, 0, 0,  0, 5, 6,  0, 0, 0],
            [0, 0, 0,  0, 0, 0,  0, 0, 0],
        ]).transpose()

        process_annotated_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 1, 3:6])

    def test_ProcessAnnotatedPairs_PairInSecondRowMidBoxFirstAndThirdColumnHorizontally_WipeOthers(self):
        candidate_stack = numpy.zeros((9, 9, 9))
        candidate_stack[:, 1, 3:6] = numpy.array([
            [0, 0, 0,  0, 5, 6,  7, 0, 0],
            [0, 0, 0,  0, 0, 0,  0, 0, 0],
            [0, 0, 0,  0, 5, 6,  0, 0, 0],
        ]).transpose()

        expected = numpy.array([
            [0, 0, 0,  0, 5, 6,  0, 0, 0],
            [0, 0, 0,  0, 0, 0,  0, 0, 0],
            [0, 0, 0,  0, 5, 6,  0, 0, 0],
        ]).transpose()

        process_annotated_pairs(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 1, 3:6])

    @staticmethod
    def assertNumpyEqual(first: numpy.array, second: numpy):
        numpy.testing.assert_equal(first, second)

