mimesniff
=========

Pure python mimesniff implementation of
`https://mimesniff.spec.whatwg.org`_

API interface is same with `API of python standard library`_

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

.. _`https://mimesniff.spec.whatwg.org`: https://mimesniff.spec.whatwg.org
.. _API of python standard library: https://docs.python.org/3/library/sndhdr.html