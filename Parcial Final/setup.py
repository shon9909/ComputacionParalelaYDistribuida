from setuptools import setup
from distutils.core import setup
from Cython.Build import cythonize
import numpy

exts = (cythonize('heatCy.pyx', language_level="3", annotate=True))

setup(ext_modules=exts,
      include_dirs=[numpy.get_include()],
      )