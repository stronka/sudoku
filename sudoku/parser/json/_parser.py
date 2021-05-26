import numpy
from ...marshalling.json import unmarshall_json


def parse(filename: str) -> numpy.array:
    with open(filename, "r") as f:
        data = f.read()

    return unmarshall_json(data)
