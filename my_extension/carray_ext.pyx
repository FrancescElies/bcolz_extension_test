import cython
import bcolz as bz
from bcolz.carray_ext cimport carray as origin_carray
from numpy cimport ndarray, npy_int64

cdef class carray(origin_carray):
    def factorize(self):
        pass


    @cython.overflowcheck(True)
    @cython.boundscheck(False)
    @cython.wraparound(False)
    cpdef my_function(self):
        """
            Function for example purposes
            
            >>> import bcolz as bz
            >>> import my_extension.example_ext as my_mod
            >>> c = bz.carray([i for i in range(1000)], dtype='i8')
            >>> my_mod.my_function(c)
            499500

        """

        cdef:
            ndarray ca_segment
            Py_ssize_t len_ca_segment
            npy_int64 sum=0

        for ca_segment in bz.iterblocks(self):
            len_ca_segment = len(ca_segment)
            for i in range(len_ca_segment):
                sum = sum + ca_segment[i]
            
        return sum
