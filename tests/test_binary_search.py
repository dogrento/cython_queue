from src.simple_queue import Fila, fill_fila
from src.binary_search.binary_search import binarySearch, mergeSort, isOrdered

def test_binary_search():
    fila = Fila()
    fill_fila(fila, 10)
    element = 4

    got = binarySearch(fila, element, 0, fila.len_fila() - 1)
    want = True

    assert got == want

def test_merge_sort():
    fila = Fila()
    fill_fila(fila, 5)

    mergeSort(fila.data)
    got = fila.data
    want = [0, 1, 2, 3, 4]

    assert got == want

def test_check_if_ordered():
    fila = Fila()
    fill_fila(fila, 5)

    got = isOrdered(fila.data)
    want = True

    assert got == want

# def test_sort_fila():
#     fila = Fila()
#     fill_fila(fila, 5)

#     got = sortFila(fila)
#     want = [0, 1, 2, 3, 4]

#     assert got == want

    
