# sudoku

### A heuristic based sudoku solver

This is a simple python sudoku solver. It employs heuristic based approach for solving sudoku.
Heuristics may be implemented and configured independently in a plugin manner.

### Installation
```commandline
pip install git+git://github.com/stronka/sudoku.git
```

### Usage
Currently it is possible to read input sudoku from a json file. 
See sudoku/resources/sudoku.json for structure.

```commandline
python -m sudoku path/to/file.json
```

### TODO:

* Make solver configurable
* Add solution tracking
* Add explain feature where solution for i.e. given cell can be backtracked

In the future

* Add some gui
* Add web interface
* Add web client
