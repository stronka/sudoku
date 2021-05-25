# sudoku

### A heuristic based sudoku solver

This is a simple python sudoku solver. It employs heuristic based approach for solving sudoku.
Heuristics may be implemented and configured independently in a plugin manner.

### Installation
```commandline
python -m pip install git+git://github.com/stronka/sudoku.git
```

### Usage
Currently it is possible to read input sudoku from a json file. 

```commandline
python -m sudoku path/to/file.json
```

Input file should look like this:

```json
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
}
```

### TODO:

* Make solver configurable
* Add solution tracking
* Add explain feature where solution for i.e. given cell can be backtracked

In the future

* Add some gui
* Add web interface
* Add web client
