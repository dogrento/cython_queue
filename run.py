import random

from timeit import timeit

from src.simple_queue import Fila, fill_fila
from px_bin_search import mergeSort as pxMergeSort
from cy_binary_search import mergeSort as cyMergeSort
from src.binary_search.binary_search import mergeSort
from wrapper import c_merge

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
    px = timeit(
            'px_py',
            number=value,
            setup="from __main__ import px_py"
            )
    pc = timeit(
            'merge_c',
            number=value,
            setup="from __main__ import merge_c"
            )
    fill_test = timeit(
            'just_fill',
            number=value,
            setup="from __main__ import just_fill"
            )

    print(f'PY Merge sort: {py}')
    print(f'cy merge sort: {cy}')
    print(f'px merge sort: {px}')
    print(f'c merge sort: {pc}')
    print(f'just filling: {fill_test}')

def pure_py():
    # fila = fill_test(1000) 
    mergeSort(fila1)

def compiled_py():
    # fila = fill_test(1000) 
    cyMergeSort(fila2)

def px_py():
    # fila = fill_test(1000) 
    pxMergeSort(fila3)

def merge_c():
    # fila = fill_test(1000)
    c_merge(fila4)

def just_fill():
    fila = fill_test(1000)

def fill_test(n):
    arr = []
    while len(arr) < n:
        random_value = random.randint(0, n)

        if random_value not in arr:
            arr.append(random_value)

    return arr
fila1 = fill_test(1000) 
fila2 = fill_test(1000) 
fila3 = fill_test(1000) 
fila4 = fill_test(1000) 

if __name__ == "__main__":
    main()
