from flask import Flask, request, jsonify

from sudoku.logic import solve_sudoku
from sudoku.marshalling import json

app = Flask('sudoku')


def serve():
    app.run()


@app.route("/", methods=['GET'])
def index():
    return jsonify({"status": "ok"})


@app.route("/sudoku/solve", methods=['POST'])
def solve():
    sudoku = json.unmarshall(request.data)
    result = solve_sudoku(sudoku)

    return jsonify({'sudoku': result.tolist()})
