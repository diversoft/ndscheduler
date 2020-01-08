from Cython.Build import cythonize
from distutils.core import setup

setup(name='scheduler app',
      ext_modules=cythonize('scheduler.py'))
