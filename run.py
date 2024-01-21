import random

from timeit import timeit

from src.simple_queue import Fila, fill_fila
from compiled_simple_queue import Fila as comp_Fila, fill_fila as comp_fill_fila

value = 10000

def main():

    value = 1_000_000_000

    py = timeit(
            'pure_py',
            number=value,
            setup="from __main__ import pure_py"
            )
    cy = timeit(
            'compiled_py',
            number=value,
            setup="from __main__ import compiled_py"
            )
    print(f'Time {py}')
    print(f'Time {cy}')

def pure_py():
    fill_fila(Fila(), value)

def compiled_py():
    comp_fill_fila(comp_Fila, value)

if __name__ == "__main__":
    main()
