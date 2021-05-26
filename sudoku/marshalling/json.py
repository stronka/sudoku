import json

import numpy


def unmarshall_json(data: str) -> numpy.array:
    parsed = json.loads(data)
    return numpy.array(parsed['sudoku'])


def marshall_json(data: numpy.array) -> str:
    json_dict = {
        'sudoku': numpy.ndarray.tolist(data)
    }
    return json.dumps(json_dict)