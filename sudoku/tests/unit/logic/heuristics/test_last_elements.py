import unittest
import numpy
from sudoku.logic._solver import create_candidates_stack
from sudoku.logic.heuristics.last_elements import process_last_elements
from sudoku.logic.meta.solution_log import SolutionLog


class TestLastElementsHeuristic(unittest.TestCase):
    def test_ProcessLastElements_LastElementNotFound_DoNothing(self):
        candidate_stack = create_candidates_stack()
        expected = candidate_stack

        process_last_elements(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack)

    def test_ProcessLastElements_LastElementInRowFound_WipeAlongStack(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[4, 0, :] = 0
        candidate_stack[4, 0, 4] = 5

        expected = numpy.array([0, 0, 0,  0, 5, 0,  0, 0, 0])

        process_last_elements(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 0, 4])

    def test_ProcessLastElements_LastElementInOtherLayerFound_WipeAlongStack(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[5, 0, :] = 0
        candidate_stack[5, 0, 4] = 6

        expected = numpy.array([0, 0, 0,  0, 0, 6,  0, 0, 0])

        process_last_elements(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 0, 4])

    def test_ProcessLastElements_LastElementInOtherLayerOtherColumnFound_WipeAlongStack(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[5, 0, :] = 0
        candidate_stack[5, 0, 5] = 6

        expected = numpy.array([0, 0, 0,  0, 0, 6,  0, 0, 0])

        process_last_elements(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 0, 5])

    def test_ProcessLastElements_LastElementInOtherLayerOtherColumnOtherRowFound_WipeAlongStack(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[5, 1, :] = 0
        candidate_stack[5, 1, 5] = 6

        expected = numpy.array([0, 0, 0,  0, 0, 6,  0, 0, 0])

        process_last_elements(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 1, 5])

    def test_ProcessLastElements_LastElementInColumnFound_WipeAlongStack(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[4, :, 4] = 0
        candidate_stack[4, 0, 4] = 5

        expected = numpy.array([0, 0, 0,  0, 5, 0,  0, 0, 0])

        process_last_elements(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 0, 4])

    def test_ProcessLastElements_LastElementInColumnInOtherLayerFound_WipeAlongStack(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[5, :, 5] = 0
        candidate_stack[5, 0, 5] = 6

        expected = numpy.array([0, 0, 0,  0, 0, 6,  0, 0, 0])

        process_last_elements(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 0, 5])

    def test_ProcessLastElements_LastElementInOtherLayerFoundOtherRow_WipeAlongStack(self):
        candidate_stack = create_candidates_stack()
        candidate_stack[5, :, 5] = 0
        candidate_stack[5, 4, 5] = 6

        expected = numpy.array([0, 0, 0,  0, 0, 6,  0, 0, 0])

        process_last_elements(candidate_stack)
        self.assertNumpyEqual(expected, candidate_stack[:, 4, 5])

    def test_ProcessLastElements_LastElementInRowFound_LogWipeAlongStack(self):
        candidate_stack = create_candidates_stack()
        solution_log = SolutionLog()
        candidate_stack[4, 0, :] = 0
        candidate_stack[4, 0, 4] = 5

        expected = [
            {'cell': (0, 4), 'action': "Remove 1", 'reason': "Last position in row: Cell (0, 4) is last possible location for number 5"},
            {'cell': (0, 4), 'action': "Remove 2", 'reason': "Last position in row: Cell (0, 4) is last possible location for number 5"},
            {'cell': (0, 4), 'action': "Remove 3", 'reason': "Last position in row: Cell (0, 4) is last possible location for number 5"},
            {'cell': (0, 4), 'action': "Remove 4", 'reason': "Last position in row: Cell (0, 4) is last possible location for number 5"},
            {'cell': (0, 4), 'action': "Remove 6", 'reason': "Last position in row: Cell (0, 4) is last possible location for number 5"},
            {'cell': (0, 4), 'action': "Remove 7", 'reason': "Last position in row: Cell (0, 4) is last possible location for number 5"},
            {'cell': (0, 4), 'action': "Remove 8", 'reason': "Last position in row: Cell (0, 4) is last possible location for number 5"},
            {'cell': (0, 4), 'action': "Remove 9", 'reason': "Last position in row: Cell (0, 4) is last possible location for number 5"},
        ]

        process_last_elements(candidate_stack, solution_log=solution_log)
        self.assertListEqual(expected, solution_log.where.query('cell == (0, 4)').get_steps())

    def test_ProcessLastElements_LastElementInColumnFound_LogWipeAlongStack(self):
        candidate_stack = create_candidates_stack()
        solution_log = SolutionLog()
        candidate_stack[4, :, 4] = 0
        candidate_stack[4, 0, 4] = 5

        expected = [
            {'cell': (0, 4), 'action': "Remove 1", 'reason': "Last position in column: Cell (0, 4) is last possible location for number 5"},
            {'cell': (0, 4), 'action': "Remove 2", 'reason': "Last position in column: Cell (0, 4) is last possible location for number 5"},
            {'cell': (0, 4), 'action': "Remove 3", 'reason': "Last position in column: Cell (0, 4) is last possible location for number 5"},
            {'cell': (0, 4), 'action': "Remove 4", 'reason': "Last position in column: Cell (0, 4) is last possible location for number 5"},
            {'cell': (0, 4), 'action': "Remove 6", 'reason': "Last position in column: Cell (0, 4) is last possible location for number 5"},
            {'cell': (0, 4), 'action': "Remove 7", 'reason': "Last position in column: Cell (0, 4) is last possible location for number 5"},
            {'cell': (0, 4), 'action': "Remove 8", 'reason': "Last position in column: Cell (0, 4) is last possible location for number 5"},
            {'cell': (0, 4), 'action': "Remove 9", 'reason': "Last position in column: Cell (0, 4) is last possible location for number 5"},
        ]

        process_last_elements(candidate_stack, solution_log=solution_log)
        self.assertListEqual(expected, solution_log.where.query('cell == (0, 4)').get_steps())

    def test_ProcessLastElements_LastElementInRowFound_DoNotLogWipeOnEmptyCandidates(self):
        candidate_stack = create_candidates_stack()
        solution_log = SolutionLog()
        candidate_stack[4, 0, :] = 0
        candidate_stack[4, 0, 4] = 5

        candidate_stack[5, 0, 4] = 0
        candidate_stack[6, 0, 4] = 0

        expected = [
            {'cell': (0, 4), 'action': "Remove 1", 'reason': "Last position in row: Cell (0, 4) is last possible location for number 5"},
            {'cell': (0, 4), 'action': "Remove 2", 'reason': "Last position in row: Cell (0, 4) is last possible location for number 5"},
            {'cell': (0, 4), 'action': "Remove 3", 'reason': "Last position in row: Cell (0, 4) is last possible location for number 5"},
            {'cell': (0, 4), 'action': "Remove 4", 'reason': "Last position in row: Cell (0, 4) is last possible location for number 5"},
            {'cell': (0, 4), 'action': "Remove 8", 'reason': "Last position in row: Cell (0, 4) is last possible location for number 5"},
            {'cell': (0, 4), 'action': "Remove 9", 'reason': "Last position in row: Cell (0, 4) is last possible location for number 5"},
        ]

        process_last_elements(candidate_stack, solution_log=solution_log)
        self.assertListEqual(expected, solution_log.where.query('cell == (0, 4)').get_steps())

    @staticmethod
    def assertNumpyEqual(first: numpy.array, second: numpy):
        numpy.testing.assert_equal(first, second)

