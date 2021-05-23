import itertools
import numpy
from functools import reduce

from logic import check_sudoku_correct


def solve_sudoku(sudoku):
    return sudoku