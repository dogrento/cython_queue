from src.simple_queue import inferno

def test_add():
    result = inferno(2, 3)
    assert result == 5
