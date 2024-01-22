import random

from timeit import timeit

from src.simple_queue import Fila, fill_fila
from compiled_simple_queue import Fila as comp_Fila, fill_fila as comp_fill_fila
from src.binary_search.binary_search import mergeSort

def main():

    value = 1_000_000_000

    py = timeit(
            'pure_py',
            number=value,
            setup="from __main__ import pure_py"
            )
    # cy = timeit(
    #         'compiled_py',
    #         number=value,
    #         setup="from __main__ import compiled_py"
    #         )
    print(f'Merge sort PY: {py}')
    # print(f'Time {cy}')

def pure_py():
    fill_fila(Fila(), value)
    mergeSort(fila.data)

# def compiled_py():
#     comp_fill_fila(comp_Fila, value)

if __name__ == "__main__":
    main()
