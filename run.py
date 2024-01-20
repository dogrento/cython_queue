import random

from timeit import timeit

value = 1000

timed = timeit(
        'fill_fila(1000)',
        number=value,
        setup='from src.fill_fila import fill_fila'
        )

print(f'Time {timed}')

