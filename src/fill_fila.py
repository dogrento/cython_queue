import random

from src.simple_queue import Fila

def fill_fila(n):
    fila = Fila()

    for i in range(n):
        random_value = random.randint(0, n)

        if random_value not in fila.data:
            fila.append_to_fila(random_value)

    return fila
