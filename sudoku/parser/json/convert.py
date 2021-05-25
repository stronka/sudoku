import numpy
import json


def convert_json_to_numpy(data: str) -> numpy.array:
    parsed = json.loads(data)
    return numpy.array(parsed['sudoku'])
