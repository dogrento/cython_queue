import random

from timeit import timeit

from src.simple_queue import Fila, fill_fila
# from compiled_simple_queue import Fila as comp_Fila, fill_fila as comp_fill_fila
from px_bin_search import mergeSort as pxMergeSort
from cy_binary_search import mergeSort as cyMergeSort
from src.binary_search.binary_search import mergeSort

fila = Fila()
fill_fila(fila, 1000)

def main():

    value = 1_000_000

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
    px = timeit(
            'px_py',
            number=value,
            setup="from __main__ import px_py"
            )

    print(f'PY Merge sort: {py}')
    print(f'cy merge sort: {cy}')
    print(f'px merge sort: {px}')

def pure_py():
    mergeSort(fila.data)

def compiled_py():
    cyMergeSort(fila.data)

def px_py():
    pxMergeSort(fila.data)

if __name__ == "__main__":
    main()
