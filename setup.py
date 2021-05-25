from setuptools import setup

setup(
    name='sudoku',
    version='0.1',
    description='Heuristic sudoku solver',
    author='stronka',
    author_email='stronka.k@gmail.com',
    packages=[
        'sudoku'
    ],
    install_requires=[
        'numpy'
    ],
)