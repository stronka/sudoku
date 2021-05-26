import argparse

input_file_help = '''
Currently only reading from json files is supported.

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
}'''


def create_parser():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('input', help=input_file_help)
    parser.add_argument(
        'output',
        nargs='?',
        default='',
        help='Output file name. If provided results will be writen to that file in JSON format.'
    )

    return parser
