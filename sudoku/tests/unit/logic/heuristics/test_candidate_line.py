import unittest
import numpy

from sudoku.logic._solver import create_candidates_stack
from sudoku.logic.heuristics.candidate_lines import process_candidate_lines


class TestLastElementsHeuristic(unittest.TestCase):
    def test_ProcessCandidateLines_FullCandidateStack_DoNothing(self):
        candidate_stack = create_candidates_stack()
        expected = candidate_stack

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack)

    def test_ProcessCandidateLines_CandidateLinePresent_RemoveOtherInThatRow(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[3, 0, :] = [4, 4, 0,  0, 4, 0,  0, 0, 4]

        expected = [4, 4, 0,  0, 0, 0,  0, 0, 0]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[3, 0, :])

    def test_ProcessCandidateLines_CandidateLinePresentInSecondRow_RemoveOtherInThatRow(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[3, 1, :] = [4, 4, 0,  0, 4, 0,  0, 0, 4]

        expected = [4, 4, 0,  0, 0, 0,  0, 0, 0]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[3, 1, :])

    def test_ProcessCandidateLines_CandidatesFormingLinePresentInSecondRowSecondThirdCol_RemoveOtherInThatRow(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[3, 1, :] = [0, 4, 4,  0, 4, 0,  0, 0, 4]

        expected = [0, 4, 4,  0, 0, 0,  0, 0, 0]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[3, 1, :])

    def test_ProcessCandidateLines_CandidatesFormingLinePresentInSecondRowSecondBox_RemoveOtherInThatRow(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[3, 1, :] = [0, 4, 0,  4, 4, 0,  0, 0, 4]

        expected = [0, 0, 0,  4, 4, 0,  0, 0, 0]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[3, 1, :])

    def test_ProcessCandidateLines_CandidatesFormingLinePresentInSecondRowSecondBox_RemoveOtherInThatRow(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[3, 1, :] = [0, 4, 0,  4, 4, 0,  0, 0, 4]

        expected = [0, 0, 0,  4, 4, 0,  0, 0, 0]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[3, 1, :])

    def test_ProcessCandidateLines_CandidatesFormingLineInMoreBoxes_DoNothing(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[3, 1, :] = [0, 4, 4,  4, 4, 0,  0, 0, 4]

        expected = [0, 4, 4,  4, 4, 0,  0, 0, 4]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[3, 1, :])

    def test_ProcessCandidateLines_CandidatesFormingLineInMoreBoxes2_DoNothing(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[3, 1, :] = [0, 4, 4,  4, 4, 0,  4, 0, 4]

        expected = [0, 4, 4,  4, 4, 0,  4, 0, 4]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[3, 1, :])

    def test_ProcessCandidateLines_CandidatesFormingLineLastBox_WipeOthersInRow(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[3, 1, :] = [0, 4, 0,  0, 4, 0,  4, 0, 4]

        expected = [0, 0, 0,  0, 0, 0,  4, 0, 4]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[3, 1, :])

    def test_ProcessCandidateLines_OtherCandidateNumber_WipeOthersInRow(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[4, 1, :] = [0, 5, 0,  0, 5, 0,  5, 0, 5]

        expected = [0, 0, 0,  0, 0, 0,  5, 0, 5]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[4, 1, :])

    def test_ProcessCandidateLines_LineInColumn_WipeOthersInColumn(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[4, :, 5] = [0, 5, 0,  0, 5, 0,  5, 0, 5]

        expected = [0, 0, 0,  0, 0, 0,  5, 0, 5]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[4, :, 5])

    def test_ProcessCandidateLines_CandidatePairsInTwoBoxes_DoNothing(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[4, :, 3] = [0, 5, 0,  5, 5, 0,  5, 0, 5]

        expected = [0, 5, 0,  5, 5, 0,  5, 0, 5]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[4, :, 3])