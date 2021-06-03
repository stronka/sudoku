from pprint import pprint

from sudoku.cli import create_parser
from sudoku.api.rest.server import serve
from sudoku.logic import solve_sudoku
from sudoku.logic.meta.solution_log import SolutionLog
from sudoku.marshalling import json
from sudoku.parser.file import parse, dump


def run():
    parser = create_parser()
    args = parser.parse_args()

    if args.serve:
        serve()
    else:
        run_cli(args)


def run_cli(args):
    if not args.input:
        print("No input file provided!")

    sudoku = parse(args.input, json.unmarshall)

    solution_log = SolutionLog() if args.query else None
    result = solve_sudoku(sudoku, solution_log=solution_log)

    if args.i:
        print("Input sudoku: ")
        pprint(sudoku)

    if args.o:
        print("Solution: ")
        pprint(result)

    if args.query:
        print("Solution query result: ")
        solution_output = solution_log.where.query(args.query).get_steps()
        pprint(solution_output, width=160)

    if args.output:
        dump(result, args.output, json.marshall)


if __name__ == "__main__":
    run()
