from src.simple_queue import Fila, fill_fila
from src.binary_search.binary_search import binarySearch

def test_binary_search():
    fila = Fila()
    fill_fila(fila, 10)
    element = 4

    got = binarySearch(fila, element, 0, fila.len_fila() - 1)
    want = True

    assert got == want
