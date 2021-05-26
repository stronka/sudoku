import numpy


def parse(filename: str, unmarshaller_func) -> numpy.array:
    with open(filename, "r") as f:
        data = f.read()

    return unmarshaller_func(data)
