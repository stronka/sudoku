import unittest
from logic._solver import *


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

    @staticmethod
    def assertNumpyEqual(first: numpy.array, second: numpy):
        numpy.testing.assert_equal(first, second)

