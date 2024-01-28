import numpy as np

from src.binary_search.binary_search import isOrdered
from src.simple_queue import Fila, fill_fila
from wrapper import c_merge

def test_c_merge():
    fila = Fila()
    fill_fila(fila, 10)

    aux = np.array(fila.data, dtype=np.int32)
    arr_view = memoryview(aux)

    c_merge(arr_view, 0, 10)

    got = isOrdered(aux.tolist()) 
    want = True 

    assert got == want

def test_py_quickSort():
    fila = Fila()
    fill_fila(fila, 10)

    py_quickMerge(fila.data)

    got = isOrdered(fila.data)
    want = True

    assert got == want
