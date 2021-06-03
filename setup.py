from distutils.core import setup

from setuptools import find_packages

setup(
    name='sudoku',
    description='Heuristic based solver',
    url='https://github.com/stronka/sudoku',
    author='stronka',
    author_email='stronka.k@gmail.com',
    version='0.2',
    packages=find_packages(),
    license='',
    install_requires=[
        'numpy',
        'Flask'
    ]
)
