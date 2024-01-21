import random

from timeit import timeit

value = 100

timed = timeit(
        'fill_fila(1000)',
        number=value,
        setup='from src.simple_queue import fill_fila'
        )
compiled_py = timeit(
        'fill_fila(1000)',
        number=value,
        setup='from src.compiled_simple_queue import fill_fila'
        )

print(f'Time {timed}')
print(f'Time {compiled_py}')

