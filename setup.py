from setuptools import setup
from Cython.Build import cythonize

mods = ["src/binary_search/cy_binary_search.py", "src/binary_search/px_bin_search.pyx"]

setup(
        ext_modules = cythonize(mods)
        )
