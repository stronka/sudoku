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