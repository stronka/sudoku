import unittest
import numpy

from sudoku.logic._solver import create_candidates_stack
from sudoku.logic.heuristics.candidate_lines import process_candidate_lines


class TestLastElementsHeuristic(unittest.TestCase):
    def test_ProcessLastElements_FullCandidateStack_DoNothing(self):
        candidate_stack = create_candidates_stack()
        expected = candidate_stack

        process_candidate_lines(candidate_stack)
        numpy.testing.assert_equal(expected, candidate_stack)