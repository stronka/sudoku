import unittest
import numpy

from sudoku.logic._solver import create_candidates_stack
from sudoku.logic.heuristics.candidate_lines import process_candidate_lines
from sudoku.logic.meta.solution_log import SolutionLog


class TestLastElementsHeuristic(unittest.TestCase):
    def test_ProcessCandidateLines_FullCandidateStack_DoNothing(self):
        candidate_stack = create_candidates_stack()
        expected = candidate_stack

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack)

    def test_ProcessCandidateLines_CandidateLinePresent_RemoveOtherInThatRow(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[3, :, :] = 0
        candidate_stack[3, 0, :] = [4, 4, 0,  0, 4, 0,  0, 0, 4]

        expected = [4, 4, 0,  0, 0, 0,  0, 0, 0]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[3, 0, :])

    def test_ProcessCandidateLines_CandidateLinePresentInSecondRow_RemoveOtherInThatRow(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[3, :, :] = 0
        candidate_stack[3, 1, :] = [4, 4, 0,  0, 4, 0,  0, 0, 4]

        expected = [4, 4, 0,  0, 0, 0,  0, 0, 0]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[3, 1, :])

    def test_ProcessCandidateLines_CandidatesFormingLinePresentInSecondRowSecondThirdCol_RemoveOtherInThatRow(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[3, :, :] = 0
        candidate_stack[3, 1, :] = [0, 4, 4,  0, 4, 0,  0, 0, 4]

        expected = [0, 4, 4,  0, 0, 0,  0, 0, 0]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[3, 1, :])

    def test_ProcessCandidateLines_CandidatesFormingLinePresentInSecondRowSecondBox_RemoveOtherInThatRow(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[3, :, :] = 0
        candidate_stack[3, 1, :] = [0, 4, 0,  4, 4, 0,  0, 0, 4]

        expected = [0, 0, 0,  4, 4, 0,  0, 0, 0]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[3, 1, :])

    def test_ProcessCandidateLines_CandidatesFormingLinePresentInSecondRowSecondBox_RemoveOtherInThatRow(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[3, :, :] = 0
        candidate_stack[3, 1, :] = [0, 4, 0,  4, 4, 0,  0, 0, 4]

        expected = [0, 0, 0,  4, 4, 0,  0, 0, 0]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[3, 1, :])

    def test_ProcessCandidateLines_CandidatesFormingLineInMoreBoxes_DoNothing(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[3, :, :] = 0
        candidate_stack[3, 1, :] = [0, 4, 4,  4, 4, 0,  0, 0, 4]

        expected = [0, 4, 4,  4, 4, 0,  0, 0, 4]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[3, 1, :])

    def test_ProcessCandidateLines_CandidatesFormingLineInMoreBoxes2_DoNothing(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[3, :, :] = 0
        candidate_stack[3, 1, :] = [0, 4, 4,  4, 4, 0,  4, 0, 4]

        expected = [0, 4, 4,  4, 4, 0,  4, 0, 4]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[3, 1, :])

    def test_ProcessCandidateLines_CandidatesFormingLineLastBox_WipeOthersInRow(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[3, :, :] = 0
        candidate_stack[3, 1, :] = [0, 4, 0,  0, 4, 0,  4, 0, 4]

        expected = [0, 0, 0,  0, 0, 0,  4, 0, 4]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[3, 1, :])

    def test_ProcessCandidateLines_OtherCandidateNumber_WipeOthersInRow(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[4, :, :] = 0
        candidate_stack[4, 1, :] = [0, 5, 0,  0, 5, 0,  5, 0, 5]

        expected = [0, 0, 0,  0, 0, 0,  5, 0, 5]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[4, 1, :])

    def test_ProcessCandidateLines_LineInColumn_WipeOthersInColumn(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[4, :, :] = 0
        candidate_stack[4, :, 5] = [0, 5, 0,  0, 5, 0,  5, 0, 5]

        expected = [0, 0, 0,  0, 0, 0,  5, 0, 5]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[4, :, 5])

    def test_ProcessCandidateLines_CandidatePairsInTwoBoxes_DoNothing(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[4, :, :] = 0
        candidate_stack[4, :, 3] = [0, 5, 0,  5, 5, 0,  5, 0, 5]

        expected = [0, 5, 0,  5, 5, 0,  5, 0, 5]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[4, :, 3])

    def test_ProcessCandidateLines_OtherCandidatesInBox_DoNothing(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[4, :, 5] = [0, 5, 0,  0, 5, 0,  5, 0, 5]

        expected = [0, 5, 0,  0, 5, 0,  5, 0, 5]

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack[4, :, 5])

    def test_ProcessCandidateLines_LineInColumn_LogInSolution(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[4, :, :] = 0
        candidate_stack[4, :, 5] = [0, 0, 0,  0, 5, 0,  5, 0, 5]
        solution_log = SolutionLog()

        expected = [
            {'cell': (4, 5), 'action': "Remove 5", 'reason': "Candidate line: candidates in cells (6, 5) and (8, 5) form a line."},
        ]

        process_candidate_lines(candidate_stack, solution_log=solution_log)
        self.assertListEqual(expected, solution_log.get_steps())

    def test_ProcessCandidateLines_LineInColumnCandidatesInFirstBox_LogSolutionReasonCorrectly(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[4, :, :] = 0
        candidate_stack[4, :, 5] = [5, 5, 0,  0, 5, 0,  0, 0, 0]
        solution_log = SolutionLog()

        expected = [
            {'cell': (4, 5), 'action': "Remove 5", 'reason': "Candidate line: candidates in cells (0, 5) and (1, 5) form a line."},
        ]

        process_candidate_lines(candidate_stack, solution_log=solution_log)
        self.assertListEqual(expected, solution_log.get_steps())

    def test_ProcessCandidateLines_LineInColumnCandidatesInFirstAndLastBox_NothingAddedToSolutionLog(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[4, :, :] = 0
        candidate_stack[4, :, 5] = [5, 5, 0,  0, 5, 0,  0, 5, 5]
        solution_log = SolutionLog()

        expected = []

        process_candidate_lines(candidate_stack, solution_log=solution_log)
        self.assertListEqual(expected, solution_log.get_steps())

    def test_ProcessCandidateLines_LineInColumnCandidatesInFirstBox_LogSolutionReasonCorrectly(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[3, :, :] = 0
        candidate_stack[3, 0, :] = [4, 4, 0,  0, 4, 0,  0, 0, 4]
        solution_log = SolutionLog()

        expected = [
            {'cell': (0, 4), 'action': "Remove 4", 'reason': "Candidate line: candidates in cells (0, 0) and (0, 1) form a line."},
            {'cell': (0, 8), 'action': "Remove 4", 'reason': "Candidate line: candidates in cells (0, 0) and (0, 1) form a line."},
        ]

        process_candidate_lines(candidate_stack, solution_log=solution_log)
        self.assertListEqual(expected, solution_log.get_steps())
