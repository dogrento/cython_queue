import random

from timeit import timeit

from src.simple_queue import Fila, fill_fila
# from compiled_simple_queue import Fila as comp_Fila, fill_fila as comp_fill_fila
from px_bin_search import mergeSort as pxMergeSort
from cy_binary_search import mergeSort as cyMergeSort
from src.binary_search.binary_search import mergeSort

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
    fila = fill_test(1000) 
    mergeSort(fila)

def compiled_py():
    fila = fill_test(1000) 
    cyMergeSort(fila)

def px_py():
    fila = fill_test(1000) 
    pxMergeSort(fila)

def fill_test(n):
    arr = []
    while len(arr) < n:
        random_value = random.randint(0, n)

        if random_value not in arr:
            arr.append(random_value)

    return fila

if __name__ == "__main__":
    main()
