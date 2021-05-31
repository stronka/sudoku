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
You can query the solution for explanation on given cells or number:

```commandline
$ python -m sudoku -io --query "cell == (0, 1) or (cell[1] == 1 and \"1\" in action)" sudoku92.json
Input sudoku:
array([[2, 0, 9, 0, 0, 0, 8, 0, 6],
       [0, 0, 5, 1, 0, 4, 3, 0, 0],
       [0, 0, 6, 0, 0, 0, 5, 0, 0],
       [3, 0, 0, 7, 0, 5, 0, 0, 4],
       [0, 0, 0, 4, 0, 6, 0, 0, 0],
       [5, 0, 0, 2, 0, 9, 0, 0, 3],
       [0, 0, 3, 0, 0, 0, 9, 0, 0],
       [0, 0, 1, 3, 0, 7, 4, 0, 0],
       [9, 0, 2, 0, 0, 0, 7, 0, 5]])
Solution:
array([[2, 1, 9, 5, 7, 3, 8, 4, 6],
       [8, 7, 5, 1, 6, 4, 3, 2, 9],
       [4, 3, 6, 9, 2, 8, 5, 1, 7],
       [3, 2, 8, 7, 1, 5, 6, 9, 4],
       [1, 9, 7, 4, 3, 6, 2, 5, 8],
       [5, 6, 4, 2, 8, 9, 1, 7, 3],
       [7, 4, 3, 8, 5, 2, 9, 6, 1],
       [6, 5, 1, 3, 9, 7, 4, 8, 2],
       [9, 8, 2, 6, 4, 1, 7, 3, 5]])
Solution query result:
[{'action': 'Remove: 2', 'cell': (0, 1), 'reason': 'Candidate elimination: present in row. Number 2 present in cell (0, 0)'},
 {'action': 'Remove: 9', 'cell': (0, 1), 'reason': 'Candidate elimination: present in row. Number 9 present in cell (0, 2)'},
 {'action': 'Remove: 8', 'cell': (0, 1), 'reason': 'Candidate elimination: present in row. Number 8 present in cell (0, 6)'},
 {'action': 'Remove: 6', 'cell': (0, 1), 'reason': 'Candidate elimination: present in row. Number 6 present in cell (0, 8)'},
 {'action': 'Remove: 5', 'cell': (0, 1), 'reason': 'Candidate elimination: present in box. Number 5 present in cell (1, 2)'},
 {'action': 'Remove: 1', 'cell': (1, 1), 'reason': 'Candidate elimination: present in row. Number 1 present in cell (1, 3)'},
 {'action': 'Remove: 1', 'cell': (7, 1), 'reason': 'Candidate elimination: present in row. Number 1 present in cell (7, 2)'},
 {'action': 'Remove: 1', 'cell': (6, 1), 'reason': 'Candidate elimination: present in box. Number 1 present in cell (7, 2)'},
 {'action': 'Remove: 1', 'cell': (8, 1), 'reason': 'Candidate elimination: present in box. Number 1 present in cell (7, 2)'},
 {'action': 'Remove: 1', 'cell': (3, 1), 'reason': 'Annotated pairs: (9, 2) pair in cells (3, 1) and (4, 1)'},
 {'action': 'Remove: 1', 'cell': (4, 1), 'reason': 'Annotated pairs: (9, 2) pair in cells (3, 1) and (4, 1)'},
 {'action': 'Remove: 3', 'cell': (0, 1), 'reason': 'Candidate elimination: present in row. Number 3 present in cell (0, 5)'},
 {'action': 'Remove 1', 'cell': (2, 1), 'reason': 'Last position in row: Cell (2, 1) is last possible location for number 3'},
 {'action': 'Remove: 7', 'cell': (0, 1), 'reason': 'Candidate elimination: present in row. Number 7 present in cell (0, 4)'},
 {'action': 'Remove: 1', 'cell': (5, 1), 'reason': 'Candidate elimination: present in box. Number 1 present in cell (4, 0)'},
 {'action': 'Remove 4', 'cell': (0, 1), 'reason': 'Last position in column: Cell (0, 1) is last possible location for number 1'},
 {'action': 'Fill: 1', 'cell': (0, 1), 'reason': 'Number 1 is the last possible candidate in cell (0, 1)'}]
```

#### Example queries with explanation:

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
