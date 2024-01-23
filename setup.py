from setuptools import setup, Extension
from Cython.Build import cythonize

mods = ["src/binary_search/cy_binary_search.py", "src/binary_search/px_bin_search.pyx"]
exts = cythonize(
        [Extension(
            'wrapper',
            sources=['src/sorts/merge.c', 'src/wrapper.pyx']
            )
         ]
        )

setup(
        ext_modules = exts,
        py_modules = mods
        )
