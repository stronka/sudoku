import numpy


def solve_row(row):
    missing = set(range(1, 10)).difference(set(row))
    return list(map(lambda x: x if x != 0 else missing.pop(), row))


def solve_box(box):
    return numpy.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])