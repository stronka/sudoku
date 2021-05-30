import numpy


_REASON = "Annotated pairs: ({}, {}) pair in cells ({}, {}) and ({}, {})"
_ACTION = "Remove: {}"


# TODO: refactor this function because it's long and ugly
def process_annotated_pairs(stack: numpy.array, *args, **kwargs) -> None:
    solution_log = kwargs.setdefault('solution_log')

    def log(pair_cells, non_pair_ks_):
        if solution_log:
            pair = tuple(set(range(0, 9)).difference(set(non_pair_ks_)))
            for cell in pair_cells:
                for k_ in non_pair_ks_:
                    if stack[k_, cell[0], cell[1]] != 0:
                        solution_log.add_step(
                            cell,
                            _ACTION.format(k_+1),
                            _REASON.format(pair[0]+1, pair[1]+1, pair_cells[0][0], pair_cells[0][1], pair_cells[1][0], pair_cells[1][1])
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
                    log(((i, n), (i, m)), non_pair_ks)

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
                    log(((n, j), (m, j)), non_pair_ks)

                    stack[non_pair_ks, n, j] = 0
                    stack[non_pair_ks, m, j] = 0
    return