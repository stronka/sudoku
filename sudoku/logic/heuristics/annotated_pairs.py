import numpy


ANNOTATED_PAIRS_REASON = "Annotated pairs: "
ANNOTATED_PAIRS_ACTION = "Remove "


def process_annotated_pairs(stack: numpy.array, *args, **kwargs) -> None:
    solution_log = kwargs.setdefault('solution_log')

    def log(cell, non_pair_ks_, reason=""):
        if solution_log:
            for k_ in non_pair_ks_:
                if stack[k_, cell[0], cell[1]] != 0:
                    solution_log.add_step(
                        cell,
                        ANNOTATED_PAIRS_ACTION + str(k_+1),
                        ANNOTATED_PAIRS_REASON + reason
                    )

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
                    log((i, n), non_pair_ks)
                    log((i, m), non_pair_ks)

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
                    log((n, j), non_pair_ks)
                    log((m, j), non_pair_ks)

                    stack[non_pair_ks, n, j] = 0
                    stack[non_pair_ks, m, j] = 0

    return