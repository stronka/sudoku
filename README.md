# sudoku

### A heuristic based sudoku solver

This is a simple python sudoku solver. It employs heuristic based approach for solving sudoku.
Heuristics may be implemented and configured independently in a plugin manner.

### Installation
```commandline
python -m pip install git+git://github.com/stronka/sudoku.git
```

### Usage
You can use sudoku from commandline. Currently it is possible to read input sudoku from a json file. 

Basic usage :
```commandline
python -m sudoku -o path/to/file.json
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

For more help on CLI:
```commandline
python -m sudoku -h
```


You can also use solver in your own code:
```python
from sudoku.logic import solve_sudoku
import numpy


data = numpy.array([...])
result = solve_sudoku(data)
```

### Solution querying:
You can query the solution for explanation on given cells or number.

#### Example queries:

Get solution for cell 0, 0 (top left):
```commandline
python -m sudoku --query "cell == (0, 0)" resources/sudoku.json
```
Get solution for cells 0, 0 and cell 8, 8 (bottom right):
```commandline
python -m sudoku --query "cell == (0, 0) or cell == (8, 8)" resources/sudoku.json
``` 
All actions on number one:
```commandline
python -m sudoku --query "\"1\" in action" resources/sudoku.json
```
All actions performed by elimination heuristic:
```commandline
python -m sudoku --query "\"elimination\" in reason" resources/sudoku.json 
```

#### Querying in your own python code:
```python
import numpy
from pprint import pprint

from sudoku.logic import solve_sudoku
from sudoku.logic.meta.solution_log import SolutionLog


data = numpy.array([...])
solution = SolutionLog()
result = solve_sudoku(data, solution)

pprint(solution.where.query("cell == (0, 0").get_steps())

complex_query = solution\
    .where\
    .query('cell == (1, 1)')\
    .query('"elimination" in reason')\
    .query('"1" in action or "2" in action')

pprint(complex_query.get_steps())
```

### TODO:

* Make solver configurable

In the future

* Add web API
