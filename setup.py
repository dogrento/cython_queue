from setuptools import setup, Extension
from Cython.Build import cythonize

mods = ["src/binary_search/cy_binary_search.py", "src/binary_search/px_bin_search.pyx"]
exts = cythonize(
        [Extension(
            'wrapper',
            sources=['src/sorts/merge.c', 'src/wrapper.pyx']
            ),
         Extension(
             'cy_binary_search',
             [mods[0]]
             ),
         Extension(
             'px_bin_search',
             [mods[1]]
             )
         ]
        )

setup(
        ext_modules = exts,
        py_modules = mods
        )
