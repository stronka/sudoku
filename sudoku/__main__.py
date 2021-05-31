from pprint import pprint

from sudoku.cli import create_parser
from sudoku.logic import solve_sudoku
from sudoku.logic.meta.solution_log import SolutionLog
from sudoku.marshalling import json
from sudoku.parser.file import parse, dump


def run_cli():
    parser = create_parser()
    args = parser.parse_args()
    run(args)


def run(args):
    sudoku = parse(args.input, json.unmarshall)

    solution_log = SolutionLog() if args.query else None
    result = solve_sudoku(sudoku, solution_log=solution_log)

    if args.output:
        dump(result, args.output, json.marshall)
    else:
        print(result)

    if args.query:
        solution_output = solution_log.where.query(args.query).get_steps()
        pprint(solution_output, width=160)


if __name__ == "__main__":
    run_cli()
