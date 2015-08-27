#!python
#cython: embedsignature=True

import cython
import bcolz
from bcolz.carray_ext cimport carray
from numpy cimport ndarray, npy_int64
from khash cimport kh_str_t, kh_int64_t, kh_int32_t, kh_float64_t, \
        kh_get_str, kh_get_int64, kh_get_int32, kh_float64_t, \
        kh_put_str, kh_put_int64, kh_put_int32, kh_put_int64


  
cdef class CarrayOnSteroids(carray):
    
    def factorize(self, id=None, rootdir=None):
        #TODO: rootdir
        ret = id
        print ret
        return ret

    @cython.overflowcheck(True)
    @cython.boundscheck(False)
    @cython.wraparound(False)
    cpdef my_function(self):
        """
            Function for example purposes
            
            >>> import bcolz as bcolz
            >>> import my_extension.example_ext as my_mod
            >>> c = bcolz.carray([i for i in range(1000)], dtype='i8')
            >>> my_mod.my_function(c)
            499500

        """

        cdef:
            ndarray ca_segment
            Py_ssize_t len_ca_segment
            npy_int64 sum=0

        for ca_segment in bcolz.iterblocks(self):
            len_ca_segment = len(ca_segment)
            for i in range(len_ca_segment):
                sum = sum + ca_segment[i]
            
        return sum
