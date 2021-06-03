def find_box_coords(i):
    i_lo, i_hi = 0, 0
    bounds = [0, 3, 6, 9]

    for b in bounds:
        if i < b:
            i_hi = b
            break
        i_lo = b

    return i_lo, i_hi


def assert_line_count(line, n):
    return line.max() and line.sum() / line.max() == n