import json

import numpy


def unmarshall_json(data: str) -> numpy.array:
    parsed = json.loads(data)
    return numpy.array(parsed['sudoku'])
