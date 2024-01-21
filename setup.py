from setuptools import setup
from Cython.Build import cythonize

setup(
        ext_modules = cythonize("src/compiled_simple_queue.pyx")
        )
