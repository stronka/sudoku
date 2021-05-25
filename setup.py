from distutils.core import setup

setup(
    name='sudoku',
    version='0.1',
    packages=[
        'sudoku',
        'sudoku.logic',
        'sudoku.logic.utils',
        'sudoku.logic.heuristics',
        'sudoku.tests',
        'sudoku.tests.unit',
        'sudoku.tests.unit.parser',
        'sudoku.tests.unit.parser.json',
        'sudoku.parser',
        'sudoku.parser.json'
    ],
    url='https://github.com/stronka/sudoku',
    license='',
    author='stronka',
    author_email='stronka.k@gmail.com',
    description='Heuristic based solver'
)
