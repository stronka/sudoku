import numpy


def process_last_elements(stack: numpy.array, *args) -> None:
    for k in range(0, 9):
        for i in range(0, 9):
            row = stack[k, i, :]
            if row.sum() and row.sum()/row.max() == 1:
                ind = numpy.nonzero(row)[0]
                stack[:, i, ind] = 0
                stack[k, i, ind] = k+1

        for j in range(0, 9):
            col = stack[k, :, j]
            if col.sum() and col.sum()/col.max() == 1:
                ind = numpy.nonzero(col)[0]
                stack[:, ind, j] = 0
                stack[k, ind, j] = k+1
    return