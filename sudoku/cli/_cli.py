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

query_help = '''
Query to filter out and print solution process. Currently querying supports:
    - cell
    - action
    - reason
Example queries:
    Get solution for cell 0, 0 (top left):
    __main__.py --query \"cell == (0, 0)\" resources/sudoku.json 
    
    Get solution for cells 0, 0 and cell 8, 8 (bottom right):
    __main__.py --query \"cell == (0, 0) or cell == (8, 8)\" resources/sudoku.json
     
    All actions on number one:
    __main__.py --query \"\\\"1\\\" in action\" resources/sudoku.json
    
    All actions performed by elimination heuristic:
    __main__.py --query \"\\\"elimination\\\" in reason\" resources/sudoku.json 
'''


def create_parser():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('--query', help=query_help)
    parser.add_argument('input', help=input_file_help)
    parser.add_argument(
        'output',
        nargs='?',
        default='',
        help='Output file name. If provided results will be writen to that file in JSON format.'
    )

    return parser
