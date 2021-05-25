import collections

import numpy


def process_identical_pairs(stack: numpy.array) -> None:
    for j in range(9):
        box_pairs = collections.defaultdict(list)
        for b in range(3):
            for n, m in ((3*b, 3*b+1), (3*b+1, 3*b+2), (3*b, 3*b+2)):
                pair_ks = []
                for k in range(9):
                    candidate = stack[k, (n, m), j]
                    box_slice = stack[k, 3*b:3*b+3, j]
                    if candidate.sum() and candidate.sum()/candidate.max() == box_slice.sum()/box_slice.max() == 2:
                        pair_ks.append(k)

                if len(pair_ks) == 2:
                    box_pairs[tuple(pair_ks)].append((n, m))

        for pair_ks, box in box_pairs.items():
            if len(box) == 1:
                for k in pair_ks:
                    n, m = box[0]
                    stack[k, :, j] = 0
                    stack[k, n, j] = k + 1
                    stack[k, m, j] = k + 1