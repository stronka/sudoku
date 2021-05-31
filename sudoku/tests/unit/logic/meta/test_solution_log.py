import unittest
from sudoku.logic.meta.solution_log import SolutionLog


class TestSolutionLog(unittest.TestCase):
    def test_getSteps_NoStepsAdded_ReturnEmptyDict(self):
        solution = SolutionLog()
        result = solution.get_steps()
        self.assertEqual(0, len(result))

    def test_getSteps_HasStepsList_ReturnThatDict(self):
        solution = SolutionLog()
        steps = {
            (0, 0): [
                {
                    'action': "Cross out 3",
                    'reason': "Present in box"
                }
            ],
            (1, 0): [
                {
                    'action': "Cross out 4",
                    'reason': "Present in box"
                }
            ],
        }

        expected = [
            {
                'cell': (0, 0),
                'action': "Cross out 3",
                'reason': "Present in box"
            },
            {
                'cell': (1, 0),
                'action': "Cross out 4",
                'reason': "Present in box"
            }
        ]

        solution._steps = steps

        result = solution.get_steps()
        self.assertEqual(expected, result)

    def test_addStep_Always_AddThatStepUnderCellKey(self):
        solution = SolutionLog()
        solution.add_step((0, 0), "Cross out 3", "Present in box")
        expected = [
            {
                'cell': (0, 0),
                'action': "Cross out 3",
                'reason': "Present in box"
            },
        ]

        self.assertListEqual(expected, solution.get_steps())

    def test_addStep_AddTwoSteps_AddThatStepToListUnderCellKey(self):
        solution = SolutionLog()
        solution.add_step((0, 0), "Cross out 3", "Present in box")
        solution.add_step((0, 0), "Cross out 4", "Present in box")

        expected = [
            {
                'cell': (0, 0),
                'action': "Cross out 3",
                'reason': "Present in box"
            },
            {
                'cell': (0, 0),
                'action': "Cross out 4",
                'reason': "Present in box"
            }
        ]

        self.assertListEqual(expected, solution.get_steps())

    def test_addStep_AddTwoStepsUnderDifferentKeys_AddStepsToListUnderCellKey(self):
        solution = SolutionLog()
        solution.add_step((0, 0), "Cross out 3", "Present in box")
        solution.add_step((1, 0), "Cross out 4", "Present in box")

        expected = [
            {
                'cell': (0, 0),
                'action': "Cross out 3",
                'reason': "Present in box"
            },
            {
                'cell': (1, 0),
                'action': "Cross out 4",
                'reason': "Present in box"
            }
        ]

        self.assertListEqual(expected, solution.get_steps())

    def test_query_EmptyQuery_ReturnAllSteps(self):
        solution = SolutionLog()
        solution.add_step((0, 0), "Cross out 3", "Present in box")
        solution.add_step((1, 0), "Cross out 4", "Present in box")

        expected = [
            {
                'cell': (0, 0),
                'action': "Cross out 3",
                'reason': "Present in box"
            },
            {
                'cell': (1, 0),
                'action': "Cross out 4",
                'reason': "Present in box"
            }
        ]

        self.assertListEqual(expected, solution.where.query().get_steps())

    def test_query_QueryCell_ReturnAllStepsUnderThatCell(self):
        solution = SolutionLog()
        solution.add_step((0, 0), "Cross out 3", "Present in box")
        solution.add_step((1, 0), "Cross out 4", "Present in box")

        expected = [
            {
                'cell': (0, 0),
                'action': "Cross out 3",
                'reason': "Present in box"
            }
        ]

        self.assertListEqual(expected, solution.where.query('cell == (0, 0)').get_steps())

    def test_query_QueryAction_ReturnAllStepsUnderThatCell(self):
        solution = SolutionLog()
        solution.add_step((0, 0), "Cross out 3", "Present in box")
        solution.add_step((1, 0), "Cross out 4", "Present in box")

        expected = [
            {
                'cell': (0, 0),
                'action': "Cross out 3",
                'reason': "Present in box"
            }
        ]

        self.assertListEqual(expected, solution.where.query('"3" in action').get_steps())

    def test_query_QueryReason_ReturnAllStepsUnderThatCell(self):
        solution = SolutionLog()
        solution.add_step((0, 0), "Cross out 3", "Present in box")
        solution.add_step((1, 0), "Cross out 4", "Present in box")

        expected = [
            {
                'cell': (0, 0),
                'action': "Cross out 3",
                'reason': "Present in box"
            },
            {
                'cell': (1, 0),
                'action': "Cross out 4",
                'reason': "Present in box"
            }
        ]

        self.assertListEqual(expected, solution.where.query('reason == "Present in box"').get_steps())

    def test_query_QueryActionAndReason_ReturnCorrect(self):
        solution = SolutionLog()
        solution.add_step((0, 0), "Cross out 3", "Present in box")
        solution.add_step((1, 0), "Cross out 4", "Present in box")

        expected = [
            {
                'cell': (0, 0),
                'action': "Cross out 3",
                'reason': "Present in box"
            }
        ]

        result = solution.where \
            .query('reason == "Present in box"') \
            .query('"3" in action')

        self.assertListEqual(expected, result.get_steps())

    def test_query_QueryCellActionAndReason_ReturnCorrect(self):
        solution = SolutionLog()
        solution.add_step((0, 0), "Cross out 3", "Present in box")
        solution.add_step((0, 2), "Cross out 3", "Present in box")
        solution.add_step((0, 2), "Cross out 4", "Present in box")
        solution.add_step((1, 0), "Cross out 4", "Present in box")

        expected = [
            {
                'cell': (0, 2),
                'action': "Cross out 3",
                'reason': "Present in box"
            }
        ]

        solution = solution.where \
            .query('cell == (0, 2)') \
            .query('reason == "Present in box"') \
            .query('"3" in action')

        self.assertListEqual(expected, solution.get_steps())
