import numpy


def solve_row(row):
    missing = set(range(1, 10)).difference(set(row))
    return list(map(lambda x: x if x != 0 else missing.pop(), row))


def solve_box(box: numpy.array) -> numpy.array:
    return numpy.array(solve_row(box.flatten())).reshape((3, 3))
