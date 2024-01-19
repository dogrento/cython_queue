from src.simple_queue import Fila

def test_fila_class_data_attr():
    fila = Fila()
    got = fila.data
    want = [] 
    assert got == want

def test_is_Fila_empty():
    fila = Fila()
    got = fila.is_empty()
    want = True

    assert got == want

