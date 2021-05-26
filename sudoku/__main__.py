from sudoku.logic import solve_sudoku
from sudoku.marshalling import json
from sudoku.parser.file import parse, dump
import sys


def run():
    if len(sys.argv) == 2:
        sudoku = parse(sys.argv[1], json.unmarshall_json)
        print(solve_sudoku(sudoku))
    elif len(sys.argv) == 3:
        sudoku = parse(sys.argv[1], json.unmarshall_json)
        dump(sudoku, sys.argv[2], json.marshall_json)
    else:
        print('''
Currently only reading from json files is supported.
usage: sudoku input_file.json [output_file]

Example json structure expected:
{
  "sudoku": [
    [0, 0, 2,    0, 0, 0,   0, 0, 8],
    [0, 5, 0,    0, 0, 0,   7, 0, 0],
    [4, 0, 0,    0, 0, 1,   6, 3, 0],

    [0, 0, 0,    4, 0, 0,   3, 7, 2],
    [0, 0, 0,    9, 0, 3,   0, 0, 0],
    [1, 2, 3,    0, 0, 6,   0, 0, 0],

    [0, 8, 9,    5, 0, 0,   0, 0, 4],
    [0, 0, 5,    0, 0, 0,   0, 9, 0],
    [2, 0, 0,    0, 0, 0,   5, 0, 0]
  ]
}''')


if __name__ == "__main__":
    run()
