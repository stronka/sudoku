from flask import Flask, request, jsonify

from sudoku.logic import solve_sudoku
from sudoku.marshalling import json

_app = Flask('sudoku')


def serve():
    _app.run()


@_app.route("/sudoku/solve", methods=['POST'])
def solve():
    sudoku = json.unmarshall(request.data)
    result = solve_sudoku(sudoku)

    return jsonify({'sudoku': result.tolist()})
