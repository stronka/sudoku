import numpy
from ._convert import convert_json_to_numpy


def parse(filename: str) -> numpy.array:
    with open(filename, "r") as f:
        data = f.read()

    return convert_json_to_numpy(data)
