def solve_row(row):
    missing = set(range(1, 10)).difference(set(row))
    return list(map(lambda x: x if x != 0 else missing.pop(), row))
