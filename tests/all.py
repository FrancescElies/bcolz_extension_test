import numpy
import bcolz
from my_extension import carray, ctable


def test_01():
    a = bcolz.carray([1, 2, 3, 4])
