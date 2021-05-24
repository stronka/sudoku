from functools import reduce

import numpy


def check_row_correct(row):
    return len(set(row)) == 9 and sum(row) == sum(range(1, 10))


def check_box_correct(box: numpy.array):
    return check_row_correct(box.flatten())


def check_sudoku_correct(sudoku: numpy.array):
    boxes = True

    for m in range(3):
        for n in range(3):
            box = sudoku[3*n:3*n+3, 3*m:3*m+3]
            boxes = boxes and box.size == len(set(box.flatten()).difference({0}))

    return boxes and \
           reduce(lambda x, y: x and check_row_correct(y), sudoku, True) and \
           reduce(lambda x, y: x and check_row_correct(y), sudoku.transpose(), True)
