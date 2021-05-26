import unittest
import numpy
from numpy.testing import assert_equal

from sudoku.marshalling.json import unmarshall_json, marshall_json


class TestUnmarshallJson(unittest.TestCase):
    def test_Unmarshall_Alawys_ReturnsNumpyArray(self):
        data = '''
        {
          "sudoku": [
            [0, 0, 2,    0, 0, 0,   0, 0, 8],
            [0, 5, 0,    0, 0, 0,   7, 0, 0],
            [4, 0, 0,    0, 0, 1,   6, 3, 0],
        
            [0, 0, 0,    4, 0, 0,   3, 7, 2],
            [0, 0, 0,    9, 0, 3,   0, 0, 0],
            [1, 2, 3,    0, 0, 6,   0, 0, 0],
        
            [0, 8, 9,    5, 0, 0,   0, 0, 4],
            [0, 0, 5,    0, 0, 0,   0, 9, 0],
            [2, 0, 0,    0, 0, 0,   5, 0, 0]
          ]
        }
        '''
        expected = numpy.array([
            [0, 0, 2,    0, 0, 0,   0, 0, 8],
            [0, 5, 0,    0, 0, 0,   7, 0, 0],
            [4, 0, 0,    0, 0, 1,   6, 3, 0],

            [0, 0, 0,    4, 0, 0,   3, 7, 2],
            [0, 0, 0,    9, 0, 3,   0, 0, 0],
            [1, 2, 3,    0, 0, 6,   0, 0, 0],

            [0, 8, 9,    5, 0, 0,   0, 0, 4],
            [0, 0, 5,    0, 0, 0,   0, 9, 0],
            [2, 0, 0,    0, 0, 0,   5, 0, 0]
        ])
        assert_equal(expected, unmarshall_json(data))


    def test_Marshall_Always_ReturnJson(self):
        data = numpy.array([
            [0, 0, 2,    0, 0, 0,   0, 0, 8],
            [0, 5, 0,    0, 0, 0,   7, 0, 0],
            [4, 0, 0,    0, 0, 1,   6, 3, 0],

            [0, 0, 0,    4, 0, 0,   3, 7, 2],
            [0, 0, 0,    9, 0, 3,   0, 0, 0],
            [1, 2, 3,    0, 0, 6,   0, 0, 0],

            [0, 8, 9,    5, 0, 0,   0, 0, 4],
            [0, 0, 5,    0, 0, 0,   0, 9, 0],
            [2, 0, 0,    0, 0, 0,   5, 0, 0]
        ])
        expected = \
            '{"sudoku": ' \
                '[' \
                    '[0, 0, 2, 0, 0, 0, 0, 0, 8], ' \
                    '[0, 5, 0, 0, 0, 0, 7, 0, 0], ' \
                    '[4, 0, 0, 0, 0, 1, 6, 3, 0], ' \
                    '[0, 0, 0, 4, 0, 0, 3, 7, 2], ' \
                    '[0, 0, 0, 9, 0, 3, 0, 0, 0], ' \
                    '[1, 2, 3, 0, 0, 6, 0, 0, 0], ' \
                    '[0, 8, 9, 5, 0, 0, 0, 0, 4], ' \
                    '[0, 0, 5, 0, 0, 0, 0, 9, 0], ' \
                    '[2, 0, 0, 0, 0, 0, 5, 0, 0]' \
                ']' \
            '}'
        self.assertEqual(expected, marshall_json(data))