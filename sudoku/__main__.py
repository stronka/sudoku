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

    solution_log = SolutionLog() if args.log else None
    result = solve_sudoku(sudoku, solution_log=solution_log)

    if args.output:
        dump(result, args.output, json.marshall)
    else:
        print(result)


if __name__ == "__main__":
    run_cli()
