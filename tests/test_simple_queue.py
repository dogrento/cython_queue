from pytest import raises

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

def test_appending_data_to_Fila():
    fila = Fila()

    fila.append_to_fila('a')
    fila.append_to_fila('b')
    fila.append_to_fila('c')

    got = fila.is_empty()
    want = False

    assert got == want

def test_data_integrity():
    fila = Fila()

    fila.append_to_fila('a')
    fila.append_to_fila('b')
    fila.append_to_fila('c')

    got = fila.data
    want = ['a', 'b', 'c']

    assert got == want

def test_data_integrity_after_pop():
    fila = Fila()

    fila.append_to_fila('a')
    fila.append_to_fila('b')
    fila.append_to_fila('c')

    fila.pop_from_fila()
    fila.pop_from_fila()

    got = fila.data 
    want = ['c'] 

    assert got == want

def test_pop_err():
    fila = Fila()

    with raises(IndexError):
        fila.pop_from_fila()

