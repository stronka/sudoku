import numpy


def parse(filename: str, unmarshaller_func) -> numpy.array:
    with open(filename, "r") as f:
        data = f.read()

    return unmarshaller_func(data)


def dump(data: numpy.array, filename: str, marshaller_func) -> None:
    marshalled_data = marshaller_func(data)

    with open(filename, "w+") as f:
        f.write(marshalled_data)

    return
