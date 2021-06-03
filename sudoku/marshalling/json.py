import json
import numpy


def unmarshall(data) -> numpy.array:
    parsed = json.loads(data)
    return numpy.array(parsed['sudoku'])


def marshall(data: numpy.array) -> str:
    json_dict = {
        'sudoku': numpy.ndarray.tolist(data)
    }
    return json.dumps(json_dict)