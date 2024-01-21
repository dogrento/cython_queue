import random

class Fila():
    def __init__(self):
        self.data = []

    def is_empty(self) -> bool:
        if len(self.data) == 0:
            return True

        return False

    def append_to_fila(self, item):
        self.data.append(item)

    def pop_from_fila(self):
        if self.is_empty():
            raise IndexError("Fila is Empty.")

        self.data.pop(0)

    def len_fila(self):
        return len(self.data)


def fill_fila(fila, n):

    while fila.len_fila() < n:
        random_value = random.randint(0, n)

        if random_value not in fila.data:
            fila.append_to_fila(random_value)

    return fila
