mimesniff
=========
.. image:: https://travis-ci.org/corona10/mimesniff.svg?branch=master
   :target: https://travis-ci.org/corona10/mimesniff

.. image:: https://img.shields.io/pypi/v/mimesniff.svg?style=flat
   :target: https://pypi.python.org/pypi/mimesniff

Pure python mimesniff implementation of
`https://mimesniff.spec.whatwg.org`_

API interface is similar with `API of python standard library`_

Install
-------

.. code:: bash

   pip install mimesniff

Usage
-----

.. code:: python

   import mimesniff

   res = mimesniff.what('sample.mp3')
   print(res)
   # audio/mpeg
   with open('sample.mp3', 'rb') as fin:
       res = mimesniff.what(fin)
       print(res)
       # audio/mpeg

   with open('sample.mp3', 'rb') as fin:
       header = fin.read(512)
       res = mimesniff.what(header)
       print(res)
       # audio/mpeg

.. _`https://mimesniff.spec.whatwg.org`: https://mimesniff.spec.whatwg.org
.. _API of python standard library: https://docs.python.org/3/library/sndhdr.html
