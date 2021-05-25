import unittest


class TestEliminationHeuristic(unittest.TestCase):
    def test_ApplyCandidateElimination_SudokuEmptyWithOne_CrossOutRow(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[0, 0] = 1
        expected = numpy.array([0, 0, 0,  0, 0, 0,  0, 0, 0])

        apply_candidate_elimination(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[0, 0, :])

    def test_ApplyCandidateElimination_SudokuEmptyWithOneAndTwo_CrossOutSecondRow(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[0, 0] = 1
        sudoku[0, 1] = 2
        expected = numpy.array([0, 0, 0,  0, 0, 0,  0, 0, 0])

        apply_candidate_elimination(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[1, 0, :])

    def test_ApplyCandidateElimination_SudokuEmptyWithOne_CrossOutFirstCol(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[0, 0] = 1
        expected = numpy.array([0, 0, 0,  0, 0, 0,  0, 0, 0])

        apply_candidate_elimination(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[0, :, 0])

    def test_ApplyCandidateElimination_SudokuEmptyWithOneAndTwo_CrossOutSecondCol(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[0, 0] = 1
        sudoku[0, 1] = 2
        expected = numpy.array([0, 0, 0,  0, 0, 0,  0, 0, 0])

        apply_candidate_elimination(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[1, :, 1])

    def test_ApplyCandidateElimination_SudokuEmptyWithOne_CrossOutBox(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[0, 0] = 1
        expected = numpy.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

        apply_candidate_elimination(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[0, 0:3, 0:3])

    def test_ApplyCandidateElimination_SudokuEmptyWithOneAndTwo_CrossOutSecondBox(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[0, 0] = 1
        sudoku[0, 1] = 2
        expected = numpy.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

        apply_candidate_elimination(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[1, 0:3, 0:3])

    def test_ApplyCandidateElimination_SudokuEmptyWithOneAndTwoInFirstRow_CrossOutSecondBox(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[0, 0] = 1
        sudoku[1, 1] = 2
        expected = numpy.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

        apply_candidate_elimination(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[1, 0:3, 0:3])

    def test_ApplyCandidateElimination_SudokuEmptyWithOneAndTwoInSecondRow_CrossOutSecondBox(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[0, 0] = 1
        sudoku[1, 4] = 2
        expected = numpy.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

        apply_candidate_elimination(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[1, 0:3, 3:6])

    def test_ApplyCandidateElimination_SudokuEmptyWithOne_CrossWholeStack(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[0, 0] = 1
        expected = numpy.array([0, 0, 0,  0, 0, 0,  0, 0, 0])
        apply_candidate_elimination(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[:, 0, 0])

    def test_ApplyCandidateElimination_SudokuEmptyWithOneAndTwoInFourthRow_CrossOutSecondBox(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[0, 0] = 1
        sudoku[3, 4] = 2
        expected = numpy.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

        apply_candidate_elimination(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[1, 3:6, 3:6])

    def test_ApplyCandidateElimination_SudokuWithOneAndEmptyFirstCell_CandidateStackOverFirstCellIsCorrect(self):
        candidate_stack = create_candidates_stack()
        sudoku = numpy.zeros((9, 9))
        sudoku[1, 1] = 1
        expected = numpy.array([0, 2, 3,  4, 5, 6,  7, 8, 9])

        apply_candidate_elimination(candidate_stack, sudoku)
        self.assertNumpyEqual(expected, candidate_stack[:, 0, 0])
    @staticmethod
    def assertNumpyEqual(first: numpy.array, second: numpy):
        numpy.testing.assert_equal(first, second)

