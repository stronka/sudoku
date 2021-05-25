import unittest
import numpy
from sudoku.parser.json.convert import convert_json_to_numpy
from numpy.testing import assert_equal


class TestParserJsonConvert(unittest.TestCase):
    def test_Convert_Alawys_ReturnsNumpyArray(self):
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
        assert_equal(expected, convert_json_to_numpy(data))
