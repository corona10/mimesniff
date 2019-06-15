import os
from os import path
from setuptools import setup

VERSION = '1.0.0'

DESCRIPTION = (
    'Pure python mimesniff implementation of https://mimesniff.spec.whatwg.org'
)

KEYWORDS = [
  'mime-type',
  'mimesniff'
]

CLASSIFIERS = [
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
]

readme_dir = path.abspath(path.dirname(__file__))
with open(path.join(readme_dir, 'README.rst')) as f:
        LONG_DESCRIPTION = f.read()

setup(name='mimesniff',
      py_modules = ['mimesniff.mimesniff'],
      version=VERSION,
      long_description=LONG_DESCRIPTION,
      author='Dong-hee Na',
      author_email='donghee.na92@gmail.com',
      url='https://github.com/corona10/mimesniff',
      description=DESCRIPTION,
      classifiers=CLASSIFIERS,
      python_requires='>=3.4'
)
