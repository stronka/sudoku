import numpy


def process_annotated_pairs(stack: numpy.array, *args) -> None:
    for b in range(3):
        for i in range(9):
            for n, m in ((3*b, 3*b+1), (3*b+1, 3*b+2), (3*b, 3*b+2)):
                non_pair_ks = list(range(9))

                for k in range(9):
                    candidate = stack[k, i, (n, m)]
                    candidate_row = stack[k, i, :]
                    if candidate_row.sum() == candidate.sum() != 0 and candidate.sum()/candidate.max() == 2:
                        non_pair_ks.remove(k)

                if len(non_pair_ks) == 7:
                    stack[non_pair_ks, i, n] = 0
                    stack[non_pair_ks, i, m] = 0

        for j in range(9):
            for n, m in ((3*b, 3*b+1), (3*b+1, 3*b+2), (3*b, 3*b+2)):
                non_pair_ks = list(range(9))

                for k in range(9):
                    candidate = stack[k, (n, m), j]
                    candidate_col = stack[k, :, j]
                    if candidate_col.sum() == candidate.sum() != 0 and candidate.sum()/candidate.max() == 2:
                        non_pair_ks.remove(k)
                if len(non_pair_ks) == 7:
                    stack[non_pair_ks, n, j] = 0
                    stack[non_pair_ks, m, j] = 0
    return